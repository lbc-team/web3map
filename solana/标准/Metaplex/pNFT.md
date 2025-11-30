## pNFT ([Program](https://learnblockchain.cn/tags/Program?map=Solana)mable NFT)

pNFT（[Program](https://learnblockchain.cn/tags/Program?map=Solana)mable NFT，可编程 NFT）是 [Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) 推出的增强型 NFT 标准，为 NFT 添加链上规则引擎，实现更复杂的所有权和转移逻辑。

### 核心概念

**规则引擎**
pNFT 可以定义链上规则控制：
- 谁可以转移
- 何时可以转移
- 转移的条件
- 委托权限
- 燃烧条件

**用途**
- 游戏物品（灵魂绑定、升级）
- 会员权益（不可转让）
- 票务（防止黄牛）
- 合规性 [NFT](https://learnblockchain.cn/tags/NFT)（KYC 验证）

### 规则类型

**1. 转移规则**
控制 NFT 的转移：
- 白名单/黑名单地址
- 时间锁定
- 需要特定签名
- 需要燃烧其他 NFT

**2. 委托规则**
控制委托权限：
- 允许/禁止特定程序
- 委托类型限制
- 时间限制

**3. 燃烧规则**
控制 NFT 燃烧：
- 谁可以燃烧
- 燃烧条件
- 燃烧后的动作

**4. 销售规则**
控制市场交易：
- 允许的市场
- 版税强制执行
- 价格限制

### 规则集（Rule Sets）

**定义规则集**
```rust
pub struct RuleSet {
    pub owner: Pubkey,
    pub operations: HashMap<Operation, Vec<Rule>>,
}

pub enum Operation {
    Transfer,
    Delegate,
    Sale,
    Burn,
}
```

**规则示例**
```json
{
  "Transfer": [
    {
      "type": "AdditionalSigner",
      "publicKey": "authority_key"
    },
    {
      "type": "Namespace",
      "field": "Collection",
      "value": "verified_collection"
    }
  ]
}
```

### 使用场景

**灵魂绑定 NFT**
不可转让的 NFT：
```
规则：Transfer -> 永久禁止
```

用途：
- 成就徽章
- 教育证书
- 身份凭证

**游戏物品**
可升级、可绑定的道具：
```
规则：
- Transfer -> 需要"解绑"程序调用
- Delegate -> 只允许游戏合约
```

**会员卡**
时间限制的会员权益：
```
规则：
- Transfer -> 需要平台授权
- Sale -> 禁止在非官方市场
```

**票务**
防止黄牛的票：
```
规则：
- Transfer -> 限制次数
- Sale -> 价格上限
```

### 创建 pNFT

**使用 Token Metadata**
```typescript
import { createNft } from "@metaplex-foundation/mpl-token-metadata";

await createNft(umi, {
  mint,
  name: "My pNFT",
  uri: "https://...",
  sellerFeeBasisPoints: 500,
  tokenStandard: TokenStandard.ProgrammableNonFungible,
  ruleSet: ruleSetAddress, // 规则集地址
}).sendAndConfirm(umi);
```

### 执行规则

**验证过程**
1. 用户发起转移
2. Token Metadata 程序调用规则集
3. 规则集验证条件
4. 通过 -> 执行转移
5. 失败 -> 拒绝交易

**示例：需要额外签名者**
```rust
// 转移时必须提供额外签名
transfer_pnft(
    &nft_mint,
    &from,
    &to,
    &authority,      // 额外签名者
    &rule_set,
)?;
```

### Token 标准比较

| 特性 | NFT | pNFT | cNFT |
|------|-----|------|------|
| 成本 | 中 | 中 | 极低 |
| 可编程性 | 无 | 强 | 无 |
| 压缩 | 否 | 否 | 是 |
| 规则引擎 | ✗ | ✓ | ✗ |
| 适用场景 | 艺术品 | 游戏/会员 | 大规模发行 |

### 生态支持

**[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)**
主流钱包逐步支持 pNFT 的特殊转移逻辑。

**市场**
需要市场理解和尊重 pNFT 规则。

**游戏**
Unity、Unreal 插件支持 pNFT。

### 优势

**灵活性**
可以实现复杂的业务逻辑。

**强制执行**
规则在协议层面执行，无法绕过。

**可组合性**
可以与其他 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 程序交互。

### 挑战

**复杂性**
规则设计和实现比普通 NFT 复杂。

**用户体验**
某些规则可能让用户困惑（为什么不能转移？）。

**市场支持**
需要市场理解 pNFT 规则。

### 未来方向

**更丰富的规则**
社区开发更多规则类型。

**工具改进**
更简单的规则创建和管理工具。

**标准化**
常见规则模式的标准化。

### 相关概念

- **规则集（Rule Set）**：定义 pNFT 行为的规则集合
- **Token Metadata**：[Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) 的 NFT 元数据标准
- **灵魂绑定（Soulbound）**：不可转让的代币
- **Token 标准**：pNFT 是 TokenStandard 枚举的一种
