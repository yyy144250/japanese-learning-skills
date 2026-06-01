#!/usr/bin/env python3
"""
Collect study session data from the japanese-learning folder.
Scans for all study files created within the given time range and
produces a JSON summary for the weekly-review skill.

Usage:
    python3 collect_study_data.py [DAYS] [FOLDER]

    DAYS   - number of past days to scan (default: 7)
    FOLDER - path to japanese-learning folder (default: ~/japanese-learning)
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    folder = Path(sys.argv[2]).expanduser() if len(sys.argv) > 2 else Path.home() / "japanese-learning"

    if not folder.exists():
        print(json.dumps({"error": f"Folder not found: {folder}", "sessions": []}))
        return

    cutoff = datetime.now() - timedelta(days=days)

    # File type patterns
    patterns = {
        "vocab": "daily-vocab-*.md",
        "kanji": "kanji-*.md",
        "context-vocab": "context-vocab-*.md",
        "grammar": "grammar-*.md",
        "sentences": "sentences-*.md",
        "shadowing": "shadowing-*.md",
        "pitch-accent": "pitch-accent-*.md",
        "reading": "reading-*.md",
        "nhk": "nhk-*.md",
        "roleplay": "roleplay-*.md",
        "journal": "journal-*.md",
        "review": "review-*.md",
        "error-analysis": "error-analysis-*.md",
    }

    sessions = []
    daily_activity = defaultdict(list)

    for activity_type, pattern in patterns.items():
        # Search in subdirectories and root
        for md_file in folder.rglob(pattern):
            stat = md_file.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime)

            if mod_time < cutoff:
                continue

            # Extract date from filename if possible
            name = md_file.stem
            date_str = None
            parts = name.split("-")
            # Look for YYYY-MM-DD pattern
            for i in range(len(parts) - 2):
                try:
                    y, m, d = int(parts[i]), int(parts[i+1]), int(parts[i+2])
                    if 2020 <= y <= 2030 and 1 <= m <= 12 and 1 <= d <= 31:
                        date_str = f"{y:04d}-{m:02d}-{d:02d}"
                        break
                except (ValueError, IndexError):
                    continue

            if not date_str:
                date_str = mod_time.strftime("%Y-%m-%d")

            # Count words in file as rough content measure
            try:
                content = md_file.read_text(encoding="utf-8")
                word_count = len(content.split())
                line_count = len(content.splitlines())
            except Exception:
                word_count = 0
                line_count = 0

            session = {
                "type": activity_type,
                "date": date_str,
                "file": str(md_file),
                "word_count": word_count,
                "line_count": line_count,
            }
            sessions.append(session)
            daily_activity[date_str].append(activity_type)

    # Summary
    summary = {
        "scan_range_days": days,
        "folder": str(folder),
        "total_sessions": len(sessions),
        "activity_types": dict(defaultdict(int)),
        "daily_activity": dict(daily_activity),
        "sessions": sorted(sessions, key=lambda s: s["date"], reverse=True),
    }

    # Count by type
    type_counts = defaultdict(int)
    for s in sessions:
        type_counts[s["type"]] += 1
    summary["activity_types"] = dict(type_counts)

    # Study days
    summary["study_days"] = len(daily_activity)
    summary["total_days"] = days

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
