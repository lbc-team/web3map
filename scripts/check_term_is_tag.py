import requests

def load_tags():
    """从 evm.txt 加载所有标签"""
    with open('evm.txt', 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f if line.strip())

def is_tag(term):
    """检查给定术语是否为有效标签
    
    Args:
        term: 要检查的术语
        tags: 可选的标签集合（此参数将被弃用）
        
    Returns:
        bool: 如果术语是有效标签则返回 True，否则返回 False
    """
    
    
    url = f"https://learnblockchain.cn/tags/{term}"
    try:
        response = requests.get(url)
        return response.status_code != 404
    except requests.RequestException:
        # 如果请求失败，返回 False
        return False

if __name__ == '__main__':
    # 测试示例
    tags = load_tags()
    
    for term in tags:
        result = is_tag(term)
        if not result:
            print(f'"{term}"')
