#!/usr/bin/env python3
"""
无主标签分析脚本
分析使用次数>=2的无主标签，找出同义标签和建议的层级关系
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any, Set
from collections import defaultdict
from difflib import SequenceMatcher


class OrphanTagAnalyzer:
    """无主标签分析器"""

    def __init__(self, data_file: str):
        """初始化"""
        self.data_file = Path(data_file)
        self.organized_data = None
        self.orphan_tags = []

        # Web3常见概念分类（用于智能归类）
        self.categories = {
            'Layer1/区块链': [
                'bitcoin', 'btc', 'ethereum', 'eth', 'solana', 'sol', 'avalanche',
                'avax', 'polygon', 'matic', 'bsc', 'binance', 'cardano', 'ada',
                'polkadot', 'dot', 'cosmos', 'atom', 'near', 'arbitrum', 'optimism',
                'base', 'zksync', 'starknet', 'sui', 'aptos', 'ton'
            ],
            'Layer2': [
                'layer2', 'l2', 'rollup', 'zk', 'zkrollup', 'optimistic', 'arbitrum',
                'optimism', 'base', 'zksync', 'starknet', 'scroll', 'linea', 'polygon'
            ],
            'DeFi': [
                'defi', 'dex', 'swap', 'lending', 'borrow', 'yield', 'farm', 'stake',
                'liquidity', 'amm', 'uniswap', 'aave', 'compound', 'curve', 'maker',
                'dao', 'governance', 'flash', 'loan'
            ],
            'NFT': [
                'nft', 'erc721', 'erc1155', 'opensea', 'mint', 'collection',
                'marketplace', 'art', 'pfp', 'avatar', 'metaverse', 'gaming'
            ],
            'Token': [
                'token', 'erc20', 'erc-20', 'coin', 'stable', 'usdt', 'usdc',
                'dai', 'busd', 'payment', 'currency'
            ],
            'Bridge': [
                'bridge', 'cross-chain', 'crosschain', 'multichain', 'interoperability'
            ],
            'Wallet': [
                'wallet', 'metamask', 'ledger', 'trezor', 'hardware', 'custody',
                'multisig', 'safe', 'gnosis'
            ],
            'Infrastructure': [
                'oracle', 'chainlink', 'indexer', 'graph', 'node', 'validator',
                'rpc', 'api', 'sdk', 'tool', 'developer', 'infra'
            ],
            'Security': [
                'security', 'audit', 'hack', 'exploit', 'vulnerability', 'safe',
                'insurance', 'risk'
            ],
            'Privacy': [
                'privacy', 'anonymous', 'mixer', 'tornado', 'zero-knowledge',
                'zk', 'private', 'confidential'
            ],
            'Protocol': [
                'protocol', 'standard', 'eip', 'erc', 'bep', 'specification'
            ]
        }

    def load_data(self):
        """加载数据"""
        print(f"正在加载数据: {self.data_file}")
        with open(self.data_file, 'r', encoding='utf-8') as f:
            self.organized_data = json.load(f)
        print(f"✓ 数据加载完成")

    def extract_orphan_tags(self, min_usage: int = 2):
        """提取无主标签（使用次数>=min_usage）"""
        if '无主标签' not in self.organized_data.get('groups', {}):
            print("未找到无主标签分组")
            return

        group = self.organized_data['groups']['无主标签']
        self.orphan_tags = [
            tag for tag in group['tags']
            if tag['usage_count'] >= min_usage
        ]

        # 按使用次数排序
        self.orphan_tags.sort(key=lambda x: x['usage_count'], reverse=True)

        print(f"✓ 找到 {len(self.orphan_tags)} 个使用次数>={min_usage}的无主标签")

    def similarity_score(self, str1: str, str2: str) -> float:
        """计算两个字符串的相似度"""
        # 转小写比较
        s1 = str1.lower().strip()
        s2 = str2.lower().strip()

        # 完全相同
        if s1 == s2:
            return 1.0

        # 移除常见分隔符后比较
        s1_clean = re.sub(r'[-_\s.]', '', s1)
        s2_clean = re.sub(r'[-_\s.]', '', s2)
        if s1_clean == s2_clean:
            return 0.95

        # 使用SequenceMatcher计算相似度
        return SequenceMatcher(None, s1_clean, s2_clean).ratio()

    def find_similar_groups(self, threshold: float = 0.85) -> List[List[Dict]]:
        """查找相似的标签（可能是同义词或拼写变体）"""
        similar_groups = []
        processed = set()

        for i, tag1 in enumerate(self.orphan_tags):
            if tag1['id'] in processed:
                continue

            group = [tag1]
            processed.add(tag1['id'])

            for tag2 in self.orphan_tags[i+1:]:
                if tag2['id'] in processed:
                    continue

                score = self.similarity_score(tag1['name'], tag2['name'])
                if score >= threshold:
                    group.append(tag2)
                    processed.add(tag2['id'])

            if len(group) > 1:
                similar_groups.append(group)

        return similar_groups

    def categorize_tags(self) -> Dict[str, List[Dict]]:
        """将标签按类别归类"""
        categorized = defaultdict(list)
        uncategorized = []

        for tag in self.orphan_tags:
            tag_name_lower = tag['name'].lower()
            found_category = False

            # 检查是否匹配任何类别
            for category, keywords in self.categories.items():
                for keyword in keywords:
                    if keyword in tag_name_lower or tag_name_lower in keyword:
                        categorized[category].append(tag)
                        found_category = True
                        break
                if found_category:
                    break

            if not found_category:
                uncategorized.append(tag)

        return dict(categorized), uncategorized

    def suggest_main_tags(self, similar_groups: List[List[Dict]]) -> List[Dict]:
        """为相似标签组建议主标签"""
        suggestions = []

        for group in similar_groups:
            # 选择使用次数最多的作为主标签候选
            main_candidate = max(group, key=lambda x: x['usage_count'])

            suggestions.append({
                'suggested_main_tag': main_candidate['name'],
                'main_tag_id': main_candidate['id'],
                'variants': [
                    {
                        'id': tag['id'],
                        'name': tag['name'],
                        'usage_count': tag['usage_count'],
                        'should_merge': True
                    }
                    for tag in group if tag['id'] != main_candidate['id']
                ],
                'total_usage': sum(tag['usage_count'] for tag in group),
                'reason': '相似名称，建议合并为同一标签'
            })

        return suggestions

    def generate_report(self, similar_groups: List[List[Dict]],
                       categorized: Dict[str, List[Dict]],
                       uncategorized: List[Dict],
                       suggestions: List[Dict]) -> Dict:
        """生成分析报告"""
        report = {
            'summary': {
                'total_orphan_tags': len(self.orphan_tags),
                'similar_groups_found': len(similar_groups),
                'tags_in_similar_groups': sum(len(g) for g in similar_groups),
                'categorized_tags': sum(len(tags) for tags in categorized.values()),
                'uncategorized_tags': len(uncategorized),
                'total_usage': sum(tag['usage_count'] for tag in self.orphan_tags)
            },
            'similar_tag_groups': suggestions,
            'categorized_tags': {
                category: [
                    {
                        'id': tag['id'],
                        'name': tag['name'],
                        'usage_count': tag['usage_count'],
                        'parent_tag_name': tag.get('parent_tag_name')
                    }
                    for tag in tags
                ]
                for category, tags in categorized.items()
            },
            'uncategorized_tags': [
                {
                    'id': tag['id'],
                    'name': tag['name'],
                    'usage_count': tag['usage_count'],
                    'parent_tag_name': tag.get('parent_tag_name')
                }
                for tag in uncategorized
            ],
            'top_orphan_tags': [
                {
                    'id': tag['id'],
                    'name': tag['name'],
                    'usage_count': tag['usage_count'],
                    'parent_tag_name': tag.get('parent_tag_name')
                }
                for tag in self.orphan_tags[:50]  # Top 50
            ]
        }

        return report

    def print_summary(self, report: Dict):
        """打印摘要"""
        print("\n" + "="*80)
        print("无主标签分析报告")
        print("="*80)

        summary = report['summary']
        print(f"\n总计: {summary['total_orphan_tags']} 个无主标签（使用次数>=2）")
        print(f"总使用次数: {summary['total_usage']}")
        print(f"发现相似标签组: {summary['similar_groups_found']} 组")
        print(f"  - 涉及标签数: {summary['tags_in_similar_groups']}")
        print(f"已分类标签: {summary['categorized_tags']}")
        print(f"未分类标签: {summary['uncategorized_tags']}")

        # 打印相似标签组
        if report['similar_tag_groups']:
            print("\n" + "-"*80)
            print("相似标签组（建议合并）:")
            print("-"*80)
            for i, group in enumerate(report['similar_tag_groups'][:10], 1):
                print(f"\n{i}. 主标签建议: {group['suggested_main_tag']} "
                      f"(总使用次数: {group['total_usage']})")
                print(f"   变体:")
                for variant in group['variants']:
                    print(f"     - {variant['name']} (使用次数: {variant['usage_count']})")

        # 打印分类统计
        if report['categorized_tags']:
            print("\n" + "-"*80)
            print("按类别分组:")
            print("-"*80)
            for category, tags in sorted(report['categorized_tags'].items(),
                                        key=lambda x: len(x[1]), reverse=True):
                total = sum(t['usage_count'] for t in tags)
                print(f"\n{category}: {len(tags)} 个标签，总使用次数: {total}")
                # 显示前5个
                for tag in sorted(tags, key=lambda x: x['usage_count'], reverse=True)[:5]:
                    print(f"  - {tag['name']} (使用次数: {tag['usage_count']})")
                if len(tags) > 5:
                    print(f"  ... 还有 {len(tags) - 5} 个")

        # 打印Top标签
        print("\n" + "-"*80)
        print("使用次数最多的无主标签 (Top 20):")
        print("-"*80)
        for i, tag in enumerate(report['top_orphan_tags'][:20], 1):
            parent_info = f" (父标签: {tag['parent_tag_name']})" if tag.get('parent_tag_name') else ""
            print(f"{i:2d}. {tag['name']:30s} 使用次数: {tag['usage_count']:5d}{parent_info}")

        print("\n" + "="*80)

    def export_report(self, report: Dict, output_file: str):
        """导出报告"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"\n✓ 分析报告已导出: {output_file}")


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    input_file = script_dir / 'output' / 'tags_organized_latest.json'
    output_file = script_dir / 'output' / 'orphan_tags_analysis.json'

    if not input_file.exists():
        print(f"错误: 找不到数据文件 {input_file}")
        print("请先运行 export_tags.py 导出标签数据")
        exit(1)

    try:
        # 创建分析器
        analyzer = OrphanTagAnalyzer(str(input_file))

        # 加载数据
        analyzer.load_data()

        # 提取无主标签（使用次数>=2）
        print("\n提取无主标签...")
        analyzer.extract_orphan_tags(min_usage=2)

        if not analyzer.orphan_tags:
            print("没有找到符合条件的无主标签")
            return

        # 查找相似标签
        print("\n查找相似标签...")
        similar_groups = analyzer.find_similar_groups(threshold=0.85)
        print(f"✓ 找到 {len(similar_groups)} 组相似标签")

        # 分类标签
        print("\n对标签进行分类...")
        categorized, uncategorized = analyzer.categorize_tags()
        print(f"✓ 已分类: {sum(len(tags) for tags in categorized.values())} 个")
        print(f"✓ 未分类: {len(uncategorized)} 个")

        # 生成主标签建议
        print("\n生成合并建议...")
        suggestions = analyzer.suggest_main_tags(similar_groups)

        # 生成报告
        print("\n生成分析报告...")
        report = analyzer.generate_report(similar_groups, categorized,
                                         uncategorized, suggestions)

        # 导出报告
        analyzer.export_report(report, str(output_file))

        # 打印摘要
        analyzer.print_summary(report)

        print(f"\n✓ 分析完成!")
        print(f"详细报告: {output_file}")

    except Exception as e:
        print(f"\n✗ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()
