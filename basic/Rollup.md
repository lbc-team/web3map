## Rollup

### 概念简介

Rollup 是一种区块链 Layer 2 扩容方案，其核心思想是将链下的大量交易"打包"（Roll up）后，将压缩的交易数据发布到链上，从而降低交易验证的难度和成本。通过这种方式，Rollup 能够在保证安全性的同时大幅提升区块链的吞吐量。

操作者在链下收集用户交易，批量处理后在链上执行智能合约，将打包后的交易数据提交给合约。这相当于一次性执行一批链下交易，但在链上只记录一个交易，从而实现了显著的扩容效果。

### 两大类型

**ZK-Rollup（零知识 Rollup）**

ZK-Rollup 采用零知识证明技术来验证交易的有效性。每一批交易打包上传至链上时都会附带一个有效性证明（Validity Proof），通常使用 zk-SNARK 或 zk-STARK 等零知识证明技术。智能合约通过验证这个证明来确认所有交易都是有效的，无需重新执行每笔交易。

提交到链上的数据包含：压缩后的交易数据、执行交易前后的状态 Merkle 树根、零知识证明。由于证明可以即时验证，用户通常可以在约 10 分钟内完成资金提取。

**Optimistic Rollup（乐观 Rollup）**

Optimistic Rollup 采用"乐观"假设和欺诈证明（Fraud Proof）机制。每次打包的交易被提交到链上时，智能合约默认假定它们是正确的，无需立即验证。如果有人发现并成功证明交易存在欺诈，智能合约会回滚不正确的状态。

这种方案的挑战期通常为 7 天，意味着用户需要等待一周才能将资金从 Layer 2 提取到 Layer 1。但在 Layer 2 内部，交易可以即时确认，用户体验流畅。

### 技术优势

- **高吞吐量**：通过批量处理交易，TPS 可达数千甚至数万
- **低成本**：交易费用可降低至主链的 1-5%
- **继承安全性**：数据和最终状态存储在主链上，继承主链的安全保障
- **EVM 兼容**：大多数 Rollup 方案兼容以太坊虚拟机，开发者可轻松迁移应用

### 市场格局

根据 L2Beat 的统计数据，截至 2022 年 6 月，Optimistic Rollup 占以太坊 Layer 2 网络总锁仓量的 74.3%，而零知识证明方案占 25.9%。随着技术发展，ZK-Rollup 的市场份额正在逐步上升。

主流项目包括：Arbitrum、Optimism（Optimistic Rollup），zkSync、StarkNet、Polygon zkEVM（ZK-Rollup）等。

### 发展趋势

Rollup 已成为以太坊扩容的主流路径。以太坊路线图中明确将 Rollup 作为核心扩容策略，通过数据可用性采样（DAS）和 EIP-4844 等升级进一步降低 Rollup 的成本。未来，多个 Rollup 链之间的互操作性和统一流动性也将成为重要发展方向。

### 相关链接

- [Layer2 开发教程 - 登链社区](https://learnblockchain.cn/article/7995)
- [一文读懂零知识证明区块链项目](https://blog.chain.link/zero-knowledge-projects-zh/)
- [Optimistic Rollup 技术详解](https://blog.csdn.net/gtdisscary/article/details/134631871)
