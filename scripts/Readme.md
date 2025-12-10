#  脚本说明

### 脚本文件
- `extract_terms_from_excali.py`: 从 Excalidraw 文件中提取词条
- `generate_terms.py`: 使用 OpenAI API 生成词条解释
- `replace_terms.py`: 自动将文档中的术语替换为对应的超链接
- `update_terms.py` : 用文件内容更新 LBC 中的术语
- `check_term_is_tag.py` : 检查术语是否为有效标签

### 配置文件
- `.env`: 环境变量配置文件
  ```
  OPENAI_API_KEY=你的OpenAI API密钥
  OPENAI_BASE_URL=你的API基础URL
  ```

### 数据文件
- `temp.txt`: 存储从 Excalidraw 提取的原始词条
- `termlink.md`: 词条链接关系文件

### 输出文件
在 `eth/` 目录下生成的文档：
- `智能合约.md`: 智能合约相关概念解释
- `ethereum.md`: 以太坊相关概念解释
- 其他根据词条自动生成的 markdown 文件

## 提示词


为 Web3 技术术语编写中文的百科解释（Wikipedia），这些术语对应的 markdown 文件已经准备好了，请你补充完整的百科解释，每个术语的说明应该专业且客观公证，不需要有主观的优势说明或未来发展的介绍。


find . -name "*.md" -type f -size -100c

## 环境设置

1. 创建并激活虚拟环境：
   ```
   source venv/bin/activate
   ```
2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```
