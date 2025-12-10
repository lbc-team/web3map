# Atomicals 协议

Atomicals 协议是一种简单而灵活的框架，用于在比特币区块链上铸造、转移和更新去中心化的数字对象（Digital Objects），也被称为“Atomicals”。它通过将数据直接绑定到比特币的最小单位——聪（satoshi）上，来实现资产的所有权和管理。该协议旨在提供一种更原生的方式来发行和管理数字收藏品、身份和可替代代币等。

## 要解决的问题

在比特币网络上发行和管理数字资产一直是一个挑战。传统的解决方案往往依赖于链下数据、侧链或复杂的比特币脚本，这些方案可能存在以下问题：

1.  **中心化风险**：许多资产协议依赖中心化的发行方或索引器来追踪所有权和验证有效性。
2.  **非原生性**：资产与比特币核心 UTXO 模型的绑定不够紧密，可能导致安全性和原子性不足。
3.  **功能受限**：[比特币脚本](https://learnblockchain.cn/tags/比特币脚本?map=BTC)的局限性使得在链上实现复杂资产逻辑变得困难。

Atomicals 协议旨在提供一个去中心化、安全且与比特币底层机制紧密结合的数字对象管理方案。

## 实现机制与原理

Atomicals 协议的核心机制在于**“原子化（Atomization）”**，即将任意数据和状态绑定到单个或一组比特币聪上。

### 数字对象的铸造 (Minting Digital Objects)
1.  **Commit 阶段**：用户通过一笔特殊的比特币交易，在 `OP_RETURN` 输出中嵌入一个 JSON 文本。这个 JSON 文本包含了一个 `init` 操作指令，其中定义了要铸造的数字对象的元数据、内容类型和内容数据（可以是文本、图片、代码等）。这笔交易的第一个输入 UTXO 被称为“初始原子”（initial atom）。
2.  **Reveal 阶段**：用户发送第二笔交易，该交易花费了“初始原子”所在的 UTXO，从而“激活”这个数字对象。这笔 Reveal 交易必须在 Commit 交易后的特定区块高度内发送，并满足一定的比特币工作量证明（PoW）要求，以确保公平铸造。

### 所有权与转移
1.  **绑定聪**：一个 Atomical 数字对象（无论是 NFT、身份还是 ARC20 代币）在创建后，其所有权就**永久绑定**到了它所附加的比特币聪上。
2.  **UTXO 模型**：数字对象的转移就是**转移承载该对象的比特币 UTXO**。当一个 UTXO 被花费到新的 UTXO 时，其上的 Atomical 数字对象也随之转移。协议规定，一个 UTXO 只能承载一个 Atomical 数字对象或一种 ARC20 代币（数量等于聪的金额）。
3.  **数字身份 (Digt)**：Atomicals 协议还支持去中心化的数字身份（Digt），它也是一种特殊的数字对象，可以被赋予人类可读的名称，并与比特币地址关联。

### 协议层级
Atomicals 协议是一个层叠结构，它定义了三种主要的数字对象类型：
*   **Realm (域名)**：类似 ENS 的去中心化域名系统，例如 `.atom` 这样的顶级域名。
*   **Container (容器)**：用于存储和管理相关数字对象的集合，例如一个项目或社区的专属容器。
*   **ARC20 (可替代代币)**：将代币余额直接绑定到聪上，实现原生的比特币代币。

## 主要特点

*   **原子性**：数字对象直接与比特币 UTXO 绑定，其所有权和安全性与比特币网络完全一致，无需额外的信任层或侧链。
*   **原生性**：协议数据通过 `OP_RETURN` 等标准[比特币脚本](https://learnblockchain.cn/tags/比特币脚本?map=BTC)机制嵌入，符合比特币的设计哲学。
*   **去中心化铸造**：大部分 Atomicals 资产采用[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)工作量证明（[PoW](https://learnblockchain.cn/tags/PoW)）的方式进行铸造，确保了公平和开放的发行过程。
*   **简单灵活**：协议设计简洁，易于实现和理解，同时足够灵活以支持各种数字对象和代币。
*   **不可变性**：一旦数字对象被铸造并锚定在[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)区块链上，其核心数据就不可篡改。

## 推荐阅读

*   [Atomicals Protocol Official Website](https://atomicals.xyz/)
*   [Atomicals Protocol Documentation](https://docs.atomicals.xyz/)
*   [Atomicals Whitepaper](https://atomicals.xyz/whitepaper.pdf)

## 相关概念

*   **聪 (Satoshi)**
*   **UTXO 模型**
*   **OP_RETURN**
*   **[PoW](https://learnblockchain.cn/tags/PoW) (工作量证明)**
*   **ARC20**
*   **Ordinal 协议**
