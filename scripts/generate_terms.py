import os
import openai
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env")

# 设置 OpenAI API key


LLM_MODEL_GPT_4O_MINI = "gpt-4o-mini-2024-07-18"

# "deepseek-r1" for aliyun
# deepseek-r1-250120 for volcengine
LLM_MODEL_DEEPSEEK_R1 = "deepseek-r1-250120"  


# deepseek-v3-241226 for volcengine
# deepseek-v3 for aliyun
LLM_MODEL_DEEPSEEK_V3 = "deepseek-v3-241226"

def get_term_explanation(term, model=LLM_MODEL_DEEPSEEK_R1):
    """
    使用 OpenAI API 获取词条介绍
    """
    try:
        prompt = f"""作为区块链领域的专家，给开发者请详细介绍一下："{term}"。
        要求：
        1. 介绍要通俗易懂，但一定要有专业深度，重点介绍实现的机制，方案的原理或来龙去脉，不要泛泛而谈
        2. 使用 markdown 格式，最大的标签是##，其次是###
        3. 每个介绍大概的字数为 500 字 - 2000 字，结构要清晰，每个部分都要有标题
        4. 文字的风格要简洁、客观，不要啰嗦，不要废话、不要有明显的个人观点、不需要额外总结
        4. 如果存在相关概念、相似的技术或相似的产品服务，在末尾列出几个，简单解释它们之间的区别
        """

        if model == LLM_MODEL_GPT_4O_MINI:
            API_KEY = os.getenv('OPENAI_API_KEY')
            BASE_URL = os.getenv('OPENAI_BASE_URL')
        elif model == LLM_MODEL_DEEPSEEK_R1 or model == LLM_MODEL_DEEPSEEK_V3:
            API_KEY = os.getenv('VOLC_API_KEY')
            BASE_URL = os.getenv('VOLC_API_BASE_URL')

        openai_client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

        request_params = {
            "model": model,
            "messages": [
                {"role": "system", "content": "你是一位编程及区块链领域的专家，帮助用户理解区块链相关概念。"},
                {"role": "user", "content": prompt}
            ],
            # temperature:1,
            # max_tokens=2000
        }

        if model == LLM_MODEL_DEEPSEEK_R1:
            request_params["stream"] = True
            response = openai_client.chat.completions.create(
                **request_params
            )

            responseContent = ""
            for chunk in response:
                answer_chunk = chunk.choices[0].delta.content
                # print(answer_chunk)
                if answer_chunk and answer_chunk != "":
                    responseContent += answer_chunk
            return responseContent
        else:
            return response.choices[0].message.content
    except Exception as e:
        print(f"获取'{term}'的解释时出错: {str(e)}")
        return None

def save_explanation(term, content, under_dir):
    """
    将解释保存为markdown文件
    """
    try:
        # 创建文件路径
        file_path = Path(under_dir) / f"{term}.md"
        
        # 确保目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"已保存 {term} 的解释到 {file_path}")
    except Exception as e:
        print(f"保存'{term}'的解释时出错: {str(e)}")

def file_exists(term):
    """
    检查是否在项目任意目录下存在对应的markdown文件
    """
    # 获取当前脚本所在目录的上一级目录
    current_dir = Path(__file__).parent.parent
    
    # 遍历所有子目录
    for path in current_dir.rglob(f"{term}.md"):
        if path.is_file():
            print(f"找到该词条的解释文件: {path}")
            return True
    
    return False

def process_terms(model=LLM_MODEL_DEEPSEEK_R1):
    """
    处理所有词条
    """
    try:
        # 读取词条文件
        with open('temp.txt', 'r', encoding='utf-8') as f:
            terms = [line.strip() for line in f if line.strip()]
        
        # 处理每个词条
        for term in terms:
            print(f"正在处理词条: {term}")
            
            # 检查文件是否已存在
            if file_exists(term):
                print(f"跳过词条 {term} (文件已存在)")
                continue
            
            # 获取解释
            explanation = get_term_explanation(term, model)
            
            if explanation:
                # 保存解释
                save_explanation(term, explanation, '_deepseek_r1')
                
                # 添加延迟以避免触发 API 限制
                time.sleep(1)
            else:
                print(f"跳过词条 {term} (获取解释失败)")
                
    except Exception as e:
        print(f"处理词条时出错: {str(e)}")

if __name__ == "__main__":
    if not os.getenv('OPENAI_API_KEY'):
        print("错误: 未设置 OPENAI_API_KEY 环境变量")
    else:
        process_terms(LLM_MODEL_DEEPSEEK_R1) 