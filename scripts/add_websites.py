#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

# 已知的官网地址
KNOWN_WEBSITES = {
    # DeFi
    'Jupiter': 'https://jup.ag/',
    'Jupiter Lend': 'https://jup.ag/lend',
    'Kamino Lend': 'https://kamino.finance/',
    'Marginfi': 'https://www.marginfi.com/',
    'Orca': 'https://www.orca.so/',
    'Raydium': 'https://raydium.io/',
    'Saber': 'https://saber.so/',
    'Sanctum': 'https://sanctum.so/',
    'Socean': 'https://www.socean.fi/',

    # DePIN
    'Helium': 'https://www.helium.com/',
    'Hivemapper': 'https://hivemapper.com/',
    'io.net': 'https://io.net/',
    'RENDER': 'https://rendernetwork.com/',

    # 其他
    'Drift': 'https://www.drift.trade/',
    'Magic Eden': 'https://magiceden.io/',
    'Marinade': 'https://marinade.finance/',
    'Meteora': 'https://meteora.ag/',
    'Phoenix': 'https://phoenix.trade/',
    'Save': 'https://save.finance/',
    'Solayer': 'https://solayer.org/',
    'Tensor': 'https://www.tensor.trade/',

    # Meme
    'GMGN.ai': 'https://gmgn.ai/',
    'Pump.fun': 'https://pump.fun/',
    'PumpSwap': 'https://pumpswap.io/',

    # SVM链
    'DoubleZero': 'https://www.double-zero.xyz/',
    'Eclipse': 'https://www.eclipse.xyz/',
    'Sonic': 'https://www.sonic.game/',
    'Soon': 'https://soo.network/',

    # 存储
    'Shadow Drive': 'https://www.shadow.cloud/',

    # 跨链
    'CCIP': 'https://chain.link/cross-chain',

    # 预言机
    'Pyth Network': 'https://pyth.network/',
    'Switchboard': 'https://switchboard.xyz/',
}

def check_has_website(content):
    """检查内容中是否已经有官网地址（仅检查前20行）"""
    lines = content.split('\n')
    first_20_lines = '\n'.join(lines[:20])

    # 检查是否有"官网"、"网站"等关键词后跟URL
    patterns = [
        r'[*_]*官网[*_]*\s*[：:]\s*https?://',
        r'[*_]*网站[*_]*\s*[：:]\s*https?://',
        r'[*_]*Website[*_]*\s*[：:]\s*https?://',
        r'[*_]*官方网站[*_]*\s*[：:]\s*https?://',
        r'官网链接[：:]\s*https?://',
    ]

    for pattern in patterns:
        if re.search(pattern, first_20_lines, re.IGNORECASE):
            return True

    return False

def add_website_to_content(content, name, website):
    """在文档开头添加官网地址"""
    lines = content.split('\n')

    # 找到第一个标题后的位置
    insert_pos = 1
    for i, line in enumerate(lines):
        if line.startswith('## '):
            insert_pos = i + 1
            # 跳过标题后的空行
            while insert_pos < len(lines) and lines[insert_pos].strip() == '':
                insert_pos += 1
            break

    # 在标题后插入官网信息（保持一个空行）
    website_line = f'\n官网：{website}\n'
    lines.insert(insert_pos, website_line)

    return '\n'.join(lines)

def process_file(file_path):
    """处理单个文件"""
    name = file_path.stem  # 文件名（不含扩展名）

    # 检查是否有已知的官网
    if name not in KNOWN_WEBSITES:
        print(f"  ⊘  {name}: 未找到官网信息")
        return False

    website = KNOWN_WEBSITES[name]

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已有官网
    if check_has_website(content):
        print(f"  ✓  {name}: 已有官网")
        return False

    # 添加官网信息
    new_content = add_website_to_content(content, name, website)

    # 写回文件
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ {name}: 已添加官网 {website}")
        return True

    return False

def main():
    script_dir = Path(__file__).parent
    ecosystem_dir = script_dir.parent / 'solana' / '生态应用'

    if not ecosystem_dir.exists():
        print(f"错误: 目录 {ecosystem_dir} 不存在")
        return 1

    print("开始检查和补充官网地址...\n")

    updated_count = 0
    already_has = 0
    no_info = 0
    total_count = 0

    # 递归处理所有 markdown 文件
    for file_path in sorted(ecosystem_dir.rglob('*.md')):
        total_count += 1
        name = file_path.stem

        # 检查是否有已知的官网
        if name not in KNOWN_WEBSITES:
            no_info += 1
            print(f"  ⊘  {name}: 未找到官网信息")
            continue

        website = KNOWN_WEBSITES[name]

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已有官网
        if check_has_website(content):
            already_has += 1
            print(f"  ✓  {name}: 已有官网")
            continue

        # 添加官网信息
        new_content = add_website_to_content(content, name, website)

        # 写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"  ✅ {name}: 已添加官网 {website}")

    print(f"\n处理完成！")
    print(f"  总文件数: {total_count}")
    print(f"  已添加官网: {updated_count}")
    print(f"  已有官网: {already_has}")
    print(f"  未找到官网信息: {no_info}")

if __name__ == '__main__':
    main()
