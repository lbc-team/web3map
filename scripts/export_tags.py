#!/usr/bin/env python3
"""
标签导出和整理脚本
从MySQL数据库导出标签数据，并按主标签分组整理
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path

try:
    import pymysql
    from dotenv import load_dotenv
except ImportError:
    print("请先安装依赖: pip install pymysql python-dotenv")
    exit(1)


class TagExporter:
    """标签导出器"""

    def __init__(self):
        """初始化数据库连接"""
        load_dotenv()

        self.connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f"✓ 成功连接到数据库: {os.getenv('DB_DATABASE')}")

    def execute_query(self, sql_file: str) -> List[Dict[str, Any]]:
        """执行SQL查询"""
        # 读取SQL文件
        sql_path = Path(sql_file)
        if not sql_path.exists():
            raise FileNotFoundError(f"SQL文件不存在: {sql_file}")

        sql = sql_path.read_text(encoding='utf-8')
        print(f"✓ 读取SQL文件: {sql_file}")

        # 执行查询
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(f"✓ 查询到 {len(results)} 条标签数据")
            return results

    def export_raw_data(self, data: List[Dict[str, Any]], output_file: str):
        """导出原始数据到JSON文件"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

        print(f"✓ 原始数据已导出到: {output_file}")

    def organize_by_main_tag(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """按主标签分组整理数据"""
        organized = {
            'metadata': {
                'total_tags': len(data),
                'export_time': datetime.now().isoformat(),
                'group_by': 'main_tag'
            },
            'groups': {}
        }

        # 按主标签分组
        for tag in data:
            main_tag_name = tag.get('main_tag_name') or '无主标签'

            if main_tag_name not in organized['groups']:
                organized['groups'][main_tag_name] = {
                    'main_tag_id': tag.get('main_id'),
                    'tags': [],
                    'total_count': 0,
                    'total_usage': 0,
                    'total_followers': 0
                }

            group = organized['groups'][main_tag_name]
            group['tags'].append({
                'id': tag['id'],
                'name': tag['name'],
                'parent_tag_name': tag.get('parent_tag_name'),
                'parent_id': tag.get('parent_id'),
                'category_id': tag.get('category_id'),
                'usage_count': tag.get('usage_count', 0),
                'followers': tag.get('followers', 0)
            })

            group['total_count'] += 1
            group['total_usage'] += tag.get('usage_count', 0)
            group['total_followers'] += tag.get('followers', 0)

        # 对每个分组内的标签按使用次数排序
        for group_name in organized['groups']:
            organized['groups'][group_name]['tags'].sort(
                key=lambda x: (x['usage_count'], x['followers']),
                reverse=True
            )

        # 计算统计信息
        organized['metadata']['total_main_tags'] = len(organized['groups'])
        organized['metadata']['top_groups'] = sorted(
            [
                {
                    'name': name,
                    'tag_count': group['total_count'],
                    'total_usage': group['total_usage'],
                    'total_followers': group['total_followers']
                }
                for name, group in organized['groups'].items()
            ],
            key=lambda x: x['total_usage'],
            reverse=True
        )[:10]

        print(f"✓ 数据已按主标签分组，共 {len(organized['groups'])} 个主标签分组")
        return organized

    def export_organized_data(self, data: Dict[str, Any], output_file: str):
        """导出整理后的数据"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

        print(f"✓ 整理后的数据已导出到: {output_file}")

    def print_summary(self, organized_data: Dict[str, Any]):
        """打印数据摘要"""
        print("\n" + "="*60)
        print("数据摘要")
        print("="*60)

        metadata = organized_data['metadata']
        print(f"总标签数: {metadata['total_tags']}")
        print(f"主标签分组数: {metadata['total_main_tags']}")
        print(f"导出时间: {metadata['export_time']}")

        print("\n前10个最活跃的主标签分组:")
        print("-" * 60)
        for i, group in enumerate(metadata['top_groups'], 1):
            print(f"{i:2d}. {group['name']:20s} "
                  f"标签数: {group['tag_count']:3d} | "
                  f"使用次数: {group['total_usage']:5d} | "
                  f"关注者: {group['total_followers']:5d}")
        print("="*60)

    def close(self):
        """关闭数据库连接"""
        if self.connection:
            self.connection.close()
            print("✓ 数据库连接已关闭")


def main():
    """主函数"""
    # 脚本所在目录
    script_dir = Path(__file__).parent

    # 文件路径
    sql_file = script_dir / 'tag.sql'
    output_dir = script_dir / 'output'
    raw_output = output_dir / f'tags_raw_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    organized_output = output_dir / f'tags_organized_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    latest_organized = output_dir / 'tags_organized_latest.json'

    try:
        # 创建导出器
        exporter = TagExporter()

        # 执行查询
        print("\n开始导出标签数据...")
        raw_data = exporter.execute_query(str(sql_file))

        # 导出原始数据
        exporter.export_raw_data(raw_data, str(raw_output))

        # 整理数据
        print("\n开始整理标签数据...")
        organized_data = exporter.organize_by_main_tag(raw_data)

        # 导出整理后的数据
        exporter.export_organized_data(organized_data, str(organized_output))
        exporter.export_organized_data(organized_data, str(latest_organized))

        # 打印摘要
        exporter.print_summary(organized_data)

        print(f"\n✓ 导出完成!")
        print(f"  - 原始数据: {raw_output}")
        print(f"  - 整理数据: {organized_output}")
        print(f"  - 最新数据: {latest_organized}")

        # 关闭连接
        exporter.close()

    except Exception as e:
        print(f"\n✗ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()
