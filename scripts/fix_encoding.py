#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UTF-8 编码修复脚本
用于修复 Web3 百科文档中的中文编码问题
"""

import os
import sys
import chardet
from pathlib import Path

def detect_encoding(file_path):
    """检测文件的当前编码"""
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            return result['encoding'], result['confidence']
    except Exception as e:
        print(f"❌ 检测编码失败 {file_path}: {e}")
        return None, 0

def fix_file_encoding(file_path, force_encoding=None):
    """修复单个文件的编码问题"""
    print(f"\n处理文件: {file_path}")

    # 检测当前编码
    detected_encoding, confidence = detect_encoding(file_path)
    print(f"  检测到的编码: {detected_encoding} (置信度: {confidence:.2f})")

    # 尝试多种编码方式读取
    encodings_to_try = [
        detected_encoding,
        'utf-8',
        'gbk',
        'gb2312',
        'gb18030',
        'latin-1',
        'cp1252',
        'iso-8859-1'
    ]

    # 去重并移除None
    encodings_to_try = [e for e in dict.fromkeys(encodings_to_try) if e]

    content = None
    successful_encoding = None

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                # 检查内容是否包含合理的中文字符
                if '##' in content or '###' in content:
                    successful_encoding = encoding
                    print(f"  ✅ 成功使用 {encoding} 读取文件")
                    break
        except (UnicodeDecodeError, Exception) as e:
            continue

    if content is None:
        print(f"  ❌ 无法读取文件，尝试所有编码都失败")
        return False

    # 创建备份
    backup_path = str(file_path) + '.bak'
    try:
        with open(file_path, 'rb') as src:
            with open(backup_path, 'wb') as dst:
                dst.write(src.read())
        print(f"  💾 已创建备份: {backup_path}")
    except Exception as e:
        print(f"  ⚠️  备份创建失败: {e}")

    # 以 UTF-8 编码写入
    try:
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"  ✅ 已修复为 UTF-8 编码")
        return True
    except Exception as e:
        print(f"  ❌ 写入文件失败: {e}")
        # 恢复备份
        if os.path.exists(backup_path):
            os.rename(backup_path, file_path)
            print(f"  ↩️  已从备份恢复")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("Web3 百科文档 UTF-8 编码修复工具")
    print("=" * 60)

    # 要修复的文件列表
    files_to_fix = [
        '去中心化存储/去中心化存储.md',
        '去中心化存储/Filecoin.md',
        '去中心化存储/Arweave.md',
        '去中心化存储/AO.md',
        '去中心化存储/EthStorage.md',
        'eth/kohaku.md'
    ]

    base_dir = Path('/Users/emmett/blockdocs/web3map')

    results = {
        'success': [],
        'failed': [],
        'skipped': []
    }

    for file_rel_path in files_to_fix:
        file_path = base_dir / file_rel_path

        if not file_path.exists():
            print(f"\n⚠️  文件不存在: {file_path}")
            results['skipped'].append(str(file_path))
            continue

        if fix_file_encoding(file_path):
            results['success'].append(str(file_path))
        else:
            results['failed'].append(str(file_path))

    # 打印总结
    print("\n" + "=" * 60)
    print("修复完成!")
    print("=" * 60)
    print(f"✅ 成功修复: {len(results['success'])} 个文件")
    for f in results['success']:
        print(f"   - {f}")

    if results['failed']:
        print(f"\n❌ 修复失败: {len(results['failed'])} 个文件")
        for f in results['failed']:
            print(f"   - {f}")

    if results['skipped']:
        print(f"\n⚠️  跳过: {len(results['skipped'])} 个文件")
        for f in results['skipped']:
            print(f"   - {f}")

    print("\n💡 提示: 备份文件保存为 .bak 后缀，确认修复成功后可以删除")

    return 0 if not results['failed'] else 1

if __name__ == '__main__':
    sys.exit(main())
