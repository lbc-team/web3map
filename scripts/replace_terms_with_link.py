import re
from pathlib import Path

def extract_terms_and_links(termlink_path):
    """从 termlink.md 文件中提取术语和对应的链接"""
    terms_dict = {}
    
    with open(termlink_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 使用正则表达式匹配 markdown 链接格式: [术语](链接)
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, content)
    
    # 将匹配结果存入字典
    for term, link in matches:
        terms_dict[term] = link
    
    return terms_dict

def replace_terms_in_file(file_path, terms_dict):
    """在文件中替换术语为对应的超链接"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified_lines = []
    for line in lines:

        if line.startswith('##') or 'https://' in line:
            modified_lines.append(line)
            continue
        else:
            # 对每个术语进行替换
            for term, link in terms_dict.items():
                # 使用正则表达式确保只替换独立的词，而不是词的一部分
                pattern = fr'\b{re.escape(term)}\b'
                replacement = f'[{term}]({link})'
                line = re.sub(pattern, replacement, line)
        
        modified_lines.append(line)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)
    

def process_eth_directory(eth_dir, terms_dict):
    """处理 eth 目录下的所有 markdown 文件"""
    # 获取所有 .md 文件
    md_files = Path(eth_dir).glob('*.md')
    
    for file_path in md_files:
        print(f"Processing {file_path}")
        replace_terms_in_file(file_path, terms_dict)

def main():
    # 设置路径
    script_dir = Path(__file__).parent
    termlink_path = script_dir / 'termlink.md'
    handle_dir = script_dir / 'release'
    
    # 确保目录存在
    if not handle_dir.exists():
        print(f"Error: Directory {handle_dir} does not exist")
        return
    
    # 提取术语和链接
    try:
        terms_dict = extract_terms_and_links(termlink_path)
        print(f"Found {len(terms_dict)} terms in termlink.md")
        
        # 处理 eth 目录下的文件
        process_eth_directory(handle_dir, terms_dict)
        print("Processing completed successfully")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    
    # 路径参数
    main() 