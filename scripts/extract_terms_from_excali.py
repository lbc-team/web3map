import json
import re
import argparse
import os
from pathlib import Path

def get_all_markdown_files(base_dir='.'):
    """获取所有 markdown 文件的文件名（不含扩展名），转换为小写用于不区分大小写的比较"""
    md_files = set()
    for root, dirs, files in os.walk(base_dir):
        # 跳过隐藏文件夹和脚本环境
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'myenv' and d != 'node_modules']

        for file in files:
            if file.endswith('.md'):
                # 获取不含扩展名的文件名，并转换为小写
                filename = os.path.splitext(file)[0].lower()
                md_files.add(filename)
    return md_files

def extract_original_text(filename):
    # 读取 EVM.excalidraw 文件

    with open(f'excalidraw/{filename}.excalidraw', 'r', encoding='utf-8') as f:
        content = f.read()

    # 尝试直接解析为 JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # 如果直接解析失败,尝试从文本中提取 JSON 部分
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            data = json.loads(match.group())
        else:
            print("无法解析文件内容")
            return

    # 存储符合条件的 originalText
    original_texts = []

    # 遍历所有元素
    for element in data.get("elements", []):
        # 检查是否满足条件:
        # 1. link 为 null
        # 2. 有 originalText 字段

        if element.get("link") is not None and ",," in element.get("link"):
            linkName = element.get("link").split(",,")[0]
            if linkName:  # 确保不是空字符串
                original_texts.append(linkName)

    # 将所有提取的词条写入 temp.txt
    with open('scripts/temp.txt', 'w', encoding='utf-8') as f:
        for text in original_texts:
            f.write(text + '\n')

    print(f"已提取 {len(original_texts)} 个文本项到 scripts/temp.txt")

    # 获取所有已存在的 markdown 文件（小写）
    existing_md_files = get_all_markdown_files('.')

    # 检查哪些词条没有对应的 markdown 文件（不区分大小写）
    missing_terms = []
    for term in original_texts:
        if term.lower() not in existing_md_files:
            missing_terms.append(term)

    # 将缺失的词条写入 need_create_terms.md
    if missing_terms:
        with open('need_create_terms.md', 'w', encoding='utf-8') as f:
            for term in missing_terms:
                f.write(term + '\n')
        print(f"发现 {len(missing_terms)} 个词条缺少 markdown 文件，已保存到 need_create_terms.md")
    else:
        # 如果没有缺失的词条，创建空文件或删除旧文件
        if os.path.exists('need_create_terms.md'):
            os.remove('need_create_terms.md')
        print("所有词条都有对应的 markdown 文件")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='从 Excalidraw 文件中提取文本')
    parser.add_argument('filename', help='Excalidraw 文件名（不需要包含 .excalidraw 扩展名）')
    args = parser.parse_args()
    
    extract_original_text(args.filename) 