#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import subprocess
from pathlib import Path
from time import sleep
from lbc_api import get_tag_info, update_tag


def get_unstaged_files(base_dir):
    """获取 git 中未 staged 的 .md 文件"""
    try:
        # 获取已修改但未 staged 的文件
        result = subprocess.run(
            ['git', 'diff', '--name-only'],
            cwd=base_dir,
            capture_output=True,
            text=True,
            check=True
        )

        files = result.stdout.strip().split('\n')
        # 过滤出 .md 文件并转换为完整路径
        md_files = [
            base_dir / file
            for file in files
            if file.endswith('.md') and file
        ]

        return md_files
    except subprocess.CalledProcessError as e:
        print(f"获取 git 状态失败: {e}")
        return []


def process_directory(directory):
    """处理目录下的所有 markdown 文件（包括子目录）"""
    # 递归获取所有 .md 文件（包括子目录）
    md_files = Path(directory).rglob('*.md')

    count = 0
    for file_path in md_files:
        print(f"处理: {file_path}")
        update_tag_from_file(file_path)
        count += 1

    print(f"\n总共处理了 {count} 个文件")


def update_tag_from_file(file_path):
    """更新 TAG"""
    file_path_name = file_path.name
    tag_name = file_path_name.split('/')[-1].replace('.md', '')

    read_file = open(file_path, 'r', encoding='utf-8')
    content = read_file.read()
    read_file.close()

    # print(tag_name, content)

    update_tag(tag_name, content, None)

    sleep(2)


def main():
    parser = argparse.ArgumentParser(
        description='更新 markdown 文件的 TAG 信息',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                          # 处理默认的 solana 目录
  %(prog)s --unstaged               # 处理所有未 staged 的 .md 文件
  %(prog)s solana/核心概念           # 处理指定目录
  %(prog)s solana/Solana.md         # 处理单个文件
  %(prog)s ../evm                   # 处理相对路径目录
        """
    )

    parser.add_argument(
        'path',
        nargs='?',
        default=None,
        help='要处理的文件或目录路径'
    )

    parser.add_argument(
        '--unstaged',
        action='store_true',
        help='处理所有未 staged 的 .md 文件'
    )

    args = parser.parse_args()

    # 确定要处理的路径
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent

    # 如果指定了 --unstaged 选项
    if args.unstaged:
        print("获取未 staged 的 .md 文件...")
        unstaged_files = get_unstaged_files(base_dir)

        if not unstaged_files:
            print("没有找到未 staged 的 .md 文件")
            return 0

        print(f"找到 {len(unstaged_files)} 个未 staged 的 .md 文件:\n")
        for file in unstaged_files:
            print(f"  - {file.relative_to(base_dir)}")

        print("\n开始处理...\n")

        for i, file_path in enumerate(unstaged_files, 1):
            print(f"[{i}/{len(unstaged_files)}] 处理: {file_path.relative_to(base_dir)}")
            try:
                update_tag_from_file(file_path)
                print(f"  ✓ 完成\n")
            except Exception as e:
                print(f"  ✗ 错误: {e}\n")

        print(f"完成! 总共处理了 {len(unstaged_files)} 个文件")
        return 0

    if args.path:
        # 如果提供了参数，解析路径
        target_path = Path(args.path)
        # 如果是相对路径，从脚本父目录解析
        if not target_path.is_absolute():
            target_path = base_dir / target_path
    else:
        # 默认处理 solana 目录
        target_path = base_dir / 'solana'


    # 检查路径是否存在
    if not target_path or not target_path.exists():
        print(f"错误: 路径 {target_path} 不存在")
        return 1

    try:
        # 判断是文件还是目录
        if target_path.is_file():
            # 检查是否是 markdown 文件
            if target_path.suffix != '.md':
                print(f"错误: {target_path} 不是 markdown 文件")
                return 1

            print(f"处理单个文件: {target_path}")
            update_tag_from_file(target_path)
            print("完成!")

        elif target_path.is_dir():
            print(f"处理目录: {target_path}")
            process_directory(target_path)
            print("完成!")

        else:
            print(f"错误: {target_path} 既不是文件也不是目录")
            return 1

    except Exception as e:
        print(f"发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
