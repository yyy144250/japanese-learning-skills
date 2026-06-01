#!/usr/bin/env python3
"""
collect_study_data.py - 收集日语学习数据，生成周报统计

用法：
    python3 collect_study_data.py [days]

参数：
    days: 回溯天数，默认 7

输出：
    打印本周学习统计摘要
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter

STUDY_DIR = Path.home() / "japanese-learning"


def collect_vocab_files(days: int) -> list:
    """收集指定天数内的词汇文件"""
    vocab_dir = STUDY_DIR / "vocab"
    if not vocab_dir.exists():
        return []

    cutoff = datetime.now() - timedelta(days=days)
    files = []

    for f in vocab_dir.glob("daily-vocab-*.md"):
        # 提取日期
        match = re.search(r"daily-vocab-(\d{4}-\d{2}-\d{2})", f.name)
        if match:
            file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
            if file_date >= cutoff:
                files.append(f)

    return sorted(files)


def count_vocab_in_file(filepath: Path) -> int:
    """统计一个词汇文件中的词数"""
    content = filepath.read_text(encoding="utf-8")
    # 每个词以 ### 开头
    return len(re.findall(r"^### ", content, re.MULTILINE))


def collect_journal_files(days: int) -> list:
    """收集指定天数内的日记文件"""
    journal_dir = STUDY_DIR / "journal"
    if not journal_dir.exists():
        return []

    cutoff = datetime.now() - timedelta(days=days)
    files = []

    for f in journal_dir.glob("*.md"):
        match = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
        if match:
            file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
            if file_date >= cutoff:
                files.append(f)

    return sorted(files)


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7

    print(f"📊 日语学习统计（过去 {days} 天）")
    print("=" * 40)

    # 词汇统计
    vocab_files = collect_vocab_files(days)
    total_words = sum(count_vocab_in_file(f) for f in vocab_files)
    print(f"\n📝 词汇")
    print(f"   学习天数: {len(vocab_files)} 天")
    print(f"   总词数: {total_words} 个")
    if vocab_files:
        print(f"   日均: {total_words / len(vocab_files):.1f} 个/天")

    # 日记统计
    journal_files = collect_journal_files(days)
    print(f"\n✍️  日记")
    print(f"   篇数: {len(journal_files)} 篇")

    # 总计
    study_days = len(set(
        [f.stem.split("-")[-3:] for f in vocab_files] +
        [re.search(r"\d{4}-\d{2}-\d{2}", f.name).group() for f in journal_files if re.search(r"\d{4}-\d{2}-\d{2}", f.name)]
    )) if (vocab_files or journal_files) else 0

    print(f"\n📅 总活跃天数: {max(len(vocab_files), len(journal_files))} / {days} 天")
    print("=" * 40)

    if not vocab_files and not journal_files:
        print("\n⚠️  没有找到学习记录！")
        print(f"   请确认学习文件保存在: {STUDY_DIR}")
        print("   建议先运行 daily-vocab 或 lang-journal 模块")


if __name__ == "__main__":
    main()
