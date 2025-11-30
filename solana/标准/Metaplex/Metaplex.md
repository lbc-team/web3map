## Metaplex

Metaplex 是 Solana 上的 [NFT](https://learnblockchain.cn/tags/NFT) 标准和工具套件，提供创建、销售和管理 [NFT](https://learnblockchain.cn/tags/NFT) 的完整解决方案。Metaplex 是 Solana [NFT](https://learnblockchain.cn/tags/NFT) 生态的基础设施。

### 核心组件

**1. Token Metadata [Program](https://learnblockchain.cn/tags/Program?map=Solana)**
定义 NFT 元数据标准：
- 名称、符号、URI
- 创作者信息和版税
- 属性和特征
- 链上和链下数据

**2. Candy Machine**
NFT 铸造和发行工具：
- 批量上传资产
- 公平发行机制
- 白名单和预售
- 防止机器人

**3. Auction House**
NFT 拍卖和交易协议：
- 支持拍卖、固定价格
- 链上出价
- 创作者版税自动分配

**4. Metaplex Storefront**
可定制的 NFT 市场前端模板。

### NFT 标准

**元数据账户**
每个 NFT 有独立的元数据账户（[PDA](https://learnblockchain.cn/tags/PDA?map=Solana)）：
```
PDA = ["metadata", metadata_program_id, mint_address]
```

**元数据结构**
```rust
pub struct Metadata {
    pub key: Key,
    pub update_authority: Pubkey,
    pub mint: Pubkey,
    pub data: Data,
    pub primary_sale_happened: bool,
    pub is_mutable: bool,
    pub collection: Option<Collection>,
    pub uses: Option<Uses>,
}

pub struct Data {
    pub name: String,
    pub symbol: String,
    pub uri: String,
    pub seller_fee_basis_points: u16,
    pub creators: Option<Vec<Creator>>,
}
```

### Candy Machine

**NFT 发行流程**
1. 准备资产（图片 + 元数据 JSON）
2. 上传到 Arweave/IPFS
3. 配置 Candy Machine
4. 用户 mint NFT

**配置选项**
- 总供应量
- 价格
- 开始/结束时间
- 白名单
- 预售机制

### 版税机制

**链上版税**
元数据中定义版税比例和接收者：
```json
{
  "seller_fee_basis_points": 500, // 5%
  "creators": [
    {
      "address": "creator_wallet",
      "share": 100 // 100%
    }
  ]
}
```

**自动执行**
支持的市场会在二次销售时自动支付版税。

### Compressed NFT (cNFT)

**突破性创新**
使用状态压缩技术，大幅降低 NFT 成本：
- 传统 NFT：约 0.012 SOL/个
- cNFT：约 0.0001 SOL/个（100倍降低）

**原理**
- 使用 Merkle 树存储数据
- 链上只存储树根
- 完整数据在链下
- 通过 Merkle 证明验证所有权

**适用场景**
- 大规模空投
- 游戏道具
- 会员卡
- 任何需要低成本铸造的场景

### 可编程 NFT (pNFT)

**规则引擎**
为 NFT 添加链上规则：
- 转让限制
- 燃烧条件
- 委托权限
- 自定义逻辑

**用途**
- 游戏物品（绑定、升级）
- 会员权益（不可转让）
- 合规性（KYC 后才能转移）

### Metaplex 协议

**开放标准**
所有协议开源，任何人可用：
- 市场可以自由集成
- 开发者可以扩展
- 社区可以贡献

**互操作性**
遵循 Metaplex 标准的 NFT 可在所有支持的市场交易。

### 主流采用

**NFT 市场**
- Magic Eden
- Tensor
- OpenSea（[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 支持）

**创作者工具**
- Candy Machine
- Sugar CLI
- [Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) Studio

### 开发工具

**Sugar CLI**
命令行工具，简化 Candy Machine 操作：
```bash
# 创建 Candy Machine
sugar create-config

# 上传资产
sugar upload

# 部署
sugar deploy

# Mint
sugar mint
```

**[JavaScript](https://learnblockchain.cn/tags/JavaScript) SDK**
```javascript
import { Metaplex } from "@metaplex-foundation/js";

const metaplex = new Metaplex(connection);
const nft = await metaplex.nfts().findByMint({ mintAddress });
```

### 对生态的影响

[Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) 为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) NFT 生态奠定了基础：
- 统一的标准
- 完善的工具
- 活跃的社区
- 持续的创新（cNFT, pNFT）

### 相关概念

- **cNFT**：压缩 NFT，[Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) 的创新
- **pNFT**：可编程 NFT
- **Candy Machine**：NFT 发行工具
- **版税（Royalties）**：二次销售创作者分成
