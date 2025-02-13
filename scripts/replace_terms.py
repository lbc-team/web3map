import re
import traceback
from pathlib import Path

def extract_terms_and_links(termlink_path):
    """从 termlink.md 文件中提取术语和对应的链接"""
    terms_dict = {}
    
    try:
        with open(termlink_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 使用正则表达式匹配 markdown 链接格式: [术语](链接)
        pattern = r'\[(.*?)\]\((.*?)\)'
        matches = re.findall(pattern, content)
        
        # 将匹配结果存入字典
        for term, link in matches:
            terms_dict[term] = link
            
    except Exception as e:
        print(f"Error in extract_terms_and_links at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise
    
    return terms_dict

def replace_terms_in_file(file_path, terms_dict):
    """在文件中替换术语为对应的超链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 对每个术语进行替换
        for term, link in terms_dict.items():
            # 使用正则表达式确保只替换独立的词，而不是词的一部分
            pattern = fr'\b{re.escape(term)}\b'
            replacement = f'[{term}]({link})'
            content = re.sub(pattern, replacement, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error in replace_terms_in_file at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise

def process_eth_directory(eth_dir, terms_dict):
    """处理 eth 目录下的所有 markdown 文件"""
    try:
        # 获取所有 .md 文件
        md_files = Path(eth_dir).glob('*.md')
        
        for file_path in md_files:
            try:
                print(f"Processing {file_path}")
                replace_terms_in_file(file_path, terms_dict)
            except Exception as e:
                print(f"Error processing file {file_path} at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
                print(traceback.format_exc())
                continue
                
    except Exception as e:
        print(f"Error in process_eth_directory at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        raise

def main():
    try:
        # 设置路径
        script_dir = Path(__file__).parent
        termlink_path = script_dir / 'termlink.md'
        eth_dir = script_dir.parent / 'eth'
        
        # 确保目录存在
        if not eth_dir.exists():
            raise FileNotFoundError(f"Directory {eth_dir} does not exist")
        
        # 提取术语和链接
        terms_dict = extract_terms_and_links(termlink_path)
        print(f"Found {len(terms_dict)} terms in termlink.md")
        
        # 处理 eth 目录下的文件
        process_eth_directory(eth_dir, terms_dict)
        print("Processing completed successfully")
        
    except Exception as e:
        print(f"Error in main at line {traceback.extract_tb(e.__traceback__)[-1].lineno}:")
        print(traceback.format_exc())
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 