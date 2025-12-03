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
这个代码库是要为 Web3 技术术语编写百科，在 @scripts/release/ 文件夹下，编写了一些词条的草稿， 请遍历 @scripts/release/ 文件夹下所有词条，然后完善对应的 md 文件，每个词条的解释最好在 500 -2000 个汉字, 使用 UTF8 编码。



## 环境设置

1. 创建并激活虚拟环境：
   ```
   python3 -m venv myenv
   source venv/bin/activate
   ```
2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```
