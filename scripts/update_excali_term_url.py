import json

files = [
    "basic/基础概念/多签钱包.md",
    "basic/基础概念/托管钱包.md",
    "basic/基础概念/插件钱包.md",
    "basic/基础概念/硬件钱包.md",
    "basic/基础概念/预言机.md",
    "basic/衍生品.md",
    "data/数据服务.md",
    "eth/开发/合约交互库.md",
    "eth/开发/安全工具.md"
]

# 提取术语（不带.md的文件名）
terms = {}  # 使用字典存储术语和对应的文件路径
for file in files:
    term = file.split('/')[-1].replace('.md', '')
    terms[term] = file

# 读取 EVM.excalidraw 文件
with open('../excalidraw/EVM.excalidraw', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 遍历所有元素
for element in data.get('elements', []):
    # 检查是否包含 originalText 和 link 字段
    if ('originalText' in element and 
        'link' in element and 
        element['link'] is None and 
        element['originalText'] in terms):
        # 找到匹配的术语，更新 link
        term = element['originalText']
        element['link'] = f"{term},,https://github.com/lbc-team/web3map/blob/main/{terms[term]}"

# 写回文件，保持格式
with open('../excalidraw/EVM.excalidraw', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)