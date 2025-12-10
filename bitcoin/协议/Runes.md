# RUNE（符文协议）

## 概念简介

Runes（符文协议）是 Ordinals 创始人 Casey Rodarmor 于 2023 年 9 月 26 日提出的比特币同质化代币协议。Runes 被设计为 BRC-20 的改进版本，提供了一个更简单、更高效的比特币原生代币标准。

符文协议的核心特点是基于比特币的 UTXO 模型，而不是像 BRC-20 那样依赖 Ordinals 的 Inscription。Casey Rodarmor 将其总结为"一个简单的、基于 UTXO 的同质化代币协议，为比特币用户提供良好的用户体验"。

## 设计动机

**BRC-20 的问题**
- 依赖 Ordinals Inscription，每次操作都需要铭刻
- 产生大量垃圾 UTXO，污染比特币 UTXO 集
- 索引和验证复杂，依赖链外索引器
- 用户体验不佳，[Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 费用高

**Runes 的改进**
- 基于 UTXO 模型，与比特币原生兼容
- 使用 OP_RETURN 存储协议数据，不产生垃圾 UTXO
- "减害"设计理念，最小化对比特币网络的影响
- 更简单的协议规范，易于实现和验证

## 核心特性

**UTXO 原生**
- 每个 UTXO 可以包含一种或多种符文代币
- 代币转移遵循比特币的 UTXO 转移规则
- 无需额外的索引层，比特币节点可以直接验证

**协议消息**
使用 OP_RETURN 在比特币交易中嵌入协议消息：
- **Etching（蚀刻）**：创建新的符文代币
- **Minting（铸造）**：增发符文代币（如果允许）
- **Transferring（转移）**：在 UTXO 之间转移符文

**代币属性**
- 名称：符文代币的唯一名称
- 符号：可选的代币符号
- 可分割性：小数位数
- 供应量：总供应量和铸造规则
- Premine：预挖数量

## 技术实现

**OP_RETURN 数据结构**
```
OP_RETURN <protocol_id> <runestone>
```

**Runestone（符文石）**
包含协议操作的编码数据：
- 使用 Protobuf 编码
- 包含代币 ID、数量、操作类型等信息
- 高效的二进制格式

**UTXO 余额模型**
- 每个 UTXO 可以携带多种符文的余额
- 转账时指定如何分配符文到输出 UTXO
- 未明确分配的符文会被销毁（作为一种安全机制）

## 激活时间

Runes 协议在比特币区块高度 840,000 激活，恰好与 2024 年 4 月的[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)减半事件同时发生。

## 与其他协议对比

| 特性 | Runes | BRC-20 | Taproot Assets |
|------|-------|---------|---------------|
| 基础技术 | UTXO + OP_RETURN | Ordinals Inscription | Taproot + CSV |
| UTXO 污染 | 最小 | 严重 | 最小 |
| 复杂度 | 简单 | 中等 | 复杂 |
| 链上足迹 | 小 | 大 | 最小 |
| 验证方式 | 链上 | 链外索引 | 客户端验证 |
| 闪电网络 | 可能支持 | 不支持 | 原生支持 |

## 应用场景

**代币发行**
- 社区代币和 Meme 币
- 项目治理代币
- 奖励和积分系统

**去中心化交易**
- 链上 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 可以直接交易符文
- 原子交换（Atomic Swaps）
- 流动性池

**游戏和应用**
- 游戏内货币和资产
- 应用代币经济
- [NFT](https://learnblockchain.cn/tags/NFT) 项目的辅助代币

## 生态发展

**工具和基础设施**
- 符文索引器和浏览器
- 符文[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)支持
- 交易市场和 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM)

**社区采用**
- 多个符文项目在减半时推出
- 交易所逐步添加符文支持
- 开发者工具和 SDK

**未来展望**
- 可能成为[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)原生代币的标准
- 与闪电网络的潜在集成
- 更多创新应用和用例

## 推荐阅读

- [比特币符文协议 Runes](https://www.panewslab.com/zh/articledetails/l8750iy9.html)
- [Runes 协议解读](https://www.jinse.cn/blockchain/3665937.html)
- [符文新手指南](https://www.xverse.app/sc-blogs/bitcoin-runes-sc)

## 相关概念

- **UTXO 模型**
- **OP_RETURN**
- **Ordinals**
- **BRC-20**
- **Casey Rodarmor**
- **原子交换 (Atomic Swaps)**
