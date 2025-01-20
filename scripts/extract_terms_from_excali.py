import json
import re
import argparse

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
        if element.get("link") is None and "originalText" in element:
            original_text = element["originalText"]
            if original_text:  # 确保不是空字符串
                original_texts.append(original_text)

    # 将结果写入 temp.txt
    with open('scripts/temp.txt', 'w', encoding='utf-8') as f:
        for text in original_texts:
            f.write(text + '\n')

    print(f"已提取 {len(original_texts)} 个文本项到 scripts/temp.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='从 Excalidraw 文件中提取文本')
    parser.add_argument('filename', help='Excalidraw 文件名（不需要包含 .excalidraw 扩展名）')
    args = parser.parse_args()
    
    extract_original_text(args.filename) 