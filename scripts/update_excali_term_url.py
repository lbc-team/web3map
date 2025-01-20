import json
import argparse

files = [
        "basic/区块链应用场景/GameFI.md",
        "basic/基础概念/App 钱包.md",
        "basic/基础概念/Coinbase.md",
        "basic/基础概念/KeyStone.md",
        "basic/基础概念/Ledger.md",
        "basic/基础概念/Trezor.md",
        "basic/基础概念/imKey.md",
        "basic/节点服务/Alchemy.md",
        "basic/节点服务/Infura.md",
        "basic/节点服务/QuickNode.md",
        "eth/Teku.md",
        "应用生态/DEFI/衍生品.md",
        "应用生态/Marketplace/Blur.md",
        "应用生态/Marketplace/Element.md",
        "应用生态/Marketplace/MagicEden.md",
        "应用生态/Marketplace/Marketplace.md",
        "应用生态/Marketplace/OpenSea.md",
        "应用生态/Oracle/Chainlink.md",
        "应用生态/Oracle/Pyth.md",
        "应用生态/交易所/Binance.md",
        "应用生态/交易所/Okx.md",
        "应用生态/交易所/中心化交易所.md",
        "应用生态/社交/CyberConnect.md",
        "应用生态/社交/Farcaster.md",
        "应用生态/社交/Lens.md",
        "应用生态/跨链/Across.md",
        "应用生态/跨链/Chainlink CCIP.md",
        "应用生态/跨链/LayerZero.md",
        "应用生态/跨链/Wormhole.md"
]

# 提取术语（不带.md的文件名）
terms = {}  # 使用字典存储术语和对应的文件路径
for file in files:
    term = file.split('/')[-1].replace('.md', '')
    terms[term] = file

def parse_args():
    parser = argparse.ArgumentParser(description='更新 Excalidraw 文件中的术语链接')
    parser.add_argument('filename', help='要处理的 Excalidraw 文件路径')
    return parser.parse_args()

def update_excalidraw_file(filename):
    # 读取 Excalidraw 文件
    with open(filename, 'r', encoding='utf-8') as f:
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
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    args = parse_args()
    update_excalidraw_file(args.filename)

if __name__ == '__main__':
    main()