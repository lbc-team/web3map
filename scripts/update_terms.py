import re
from pathlib import Path
from lbc_api import get_tag_info, update_tag
 

def process_directory(eth_dir):
    """处理目录下的所有 markdown 文件（包括子目录）"""
    # 递归获取所有 .md 文件（包括子目录）
    md_files = Path(eth_dir).rglob('*.md')
    
    for file_path in md_files:
        print(f"处理: {file_path}")
        update_tag_from_file(file_path)

def update_tag_from_file(file_path):
    """更新 TAG"""
    file_path_name = file_path.name
    tag_name = file_path_name.split('/')[-1].replace('.md', '')

    read_file = open(file_path, 'r', encoding='utf-8')
    content = read_file.read()
    read_file.close()

    # print(tag_name, content)

    update_tag(tag_name, content, None)

def main():
    # 设置路径
    script_dir = Path(__file__).parent
    handle_dir =  script_dir.parent / 'solana'
    
    # 确保目录存在
    if not handle_dir.exists():
        print(f"Error: Directory {handle_dir} does not exist")
        return
    
    # 提取术语和链接
    try:
        # 处理 eth 目录下的文件
        process_directory(handle_dir)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    
    # 路径参数
    main() 