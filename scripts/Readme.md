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


去中心化存储/AO.md

ZKP/Aztec.md
ZKP/Aleo.md
ZKP/Monero.md
ZKP/Zcash.md
ZKP/Cysic.md
ZKP/zkVM.md
ZKP/Noir.md
bitcoin/协议/RGB++.md
bitcoin/协议/Ordinals/indexer.md
bitcoin/协议/客户端验证.md
bitcoin/协议/Atomicals/ARC20.md
bitcoin/协议/Atomicals/AVM.md
bitcoin/协议/Atomicals/Atomicals.md
bitcoin/协议/Taproot-Assets.md
bitcoin/二层扩容/BitVM.md
bitcoin/二层扩容/扩容技术/Stacks.md
bitcoin/二层扩容/扩容技术/Merlin.md
bitcoin/二层扩容/CKB.md
bitcoin/二层扩容/BEVM.md
bitcoin/二层扩容/Liquid.md
bitcoin/基础概念/Schnorr.md
bitcoin/opcode.md
eth/eips/ERC1271.md
eth/eips/ERC6551.md
eth/eips/EIP1159.md
eth/eips/ERC4337.md
eth/eips/EIP3074.md
eth/eips/ERc1967.md
eth/EVM字节码.md
eth/合约安全.md
eth/执行层.md
eth/生态应用/跨链桥.md
eth/生态应用/USDC.md
eth/生态应用/Curve.md
eth/生态应用/DEX.md
eth/生态应用/Rocket.md
eth/生态应用/Lending.md
eth/生态应用/Lido.md
eth/生态应用/USDT.md
eth/生态应用/ens.md
eth/生态应用/DAI.md
eth/生态应用/LSD.md
eth/生态应用/Uniswap.md
eth/生态应用/稳定币.md
eth/zkEVM.md
eth/gas.md
eth/kohaku.md
eth/Reth.md
eth/开发/web3j.md
eth/开发/合约升级.md
eth/开发/合约工厂.md
eth/开发/gas优化.md
eth/开发/create2.md
eth/开发/Vyper.md
eth/开发/离线签名.md
eth/开发/delegatecall.md
data/数据服务.md

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
