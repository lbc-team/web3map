#!/usr/bin/env python3
"""
检查 Excalidraw 文件中的链接格式
找出 link 不为空但没有两个连续逗号 (,,) 的链接
"""

import json
import sys
import re

def check_links(filename):
    """检查指定 excalidraw 文件中的链接格式"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 检查文件中的所有元素
        elements = data.get('elements', [])

        error_count = 0
        for idx, element in enumerate(elements):
            link = element.get('link')

            # 检查 link 是否存在且不为空
            if link and link != "null":
                # 检查是否包含两个连续的逗号
                if ',,' not in link:
                    error_count += 1
                    # 打印错误的链接
                    text = element.get('text', element.get('id', 'N/A'))
                    print(f"❌ 错误链接 #{error_count}:")
                    print(f"   文本: {text}")
                    print(f"   链接: {link}")
                    print(f"   元素索引: {idx}")
                    print()

        # 打印总结
        print(f"{'='*60}")
        if error_count > 0:
            print(f"共发现 {error_count} 个格式错误的链接")
            print(f"正确格式应为: \"link\": \"名称,,URL\"")
        else:
            print("✅ 所有链接格式正确！")

    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 不存在")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析 JSON 文件: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python check_links.py <excalidraw文件路径>")
        print("示例: python check_links.py excalidraw/EVM.excalidraw")
        sys.exit(1)

    filename = sys.argv[1]
    check_links(filename)
