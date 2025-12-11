# Blob

## 概念简介

Blob（Binary Large Object，二进制大对象）是以太坊在 Dencun 升级（2024 年 3 月）中通过 EIP-4844 引入的一种新型数据存储机制。Blob 是附加在交易上的临时数据段，专门为 Layer 2 Rollup 提供廉价的数据可用性空间，是以太坊扩容战略的关键组成部分。

与永久存储在链上的 CALLDATA 不同，blob 数据仅在共识层临时保存约 18 天，这使得其定价远低于传统的链上存储，为 L2 网络大幅降低了运营成本。

## 技术特性

### 数据规格

**容量参数：**
- **单个 blob 大小**：128 KB（精确 131,072 字节）
- **初始目标**：每个区块 3 个 blob（Dencun）
- **初始最大值**：每个区块 6 个 blob（Dencun）
- **Pectra 后**：目标 6 个，最大 9 个
- **总计容量**：最多 1.125 MB/区块（9 × 128 KB）

**存储特性：**
- 存储在信标链的共识层
- 生命周期约 18 天（4096 个 epoch）
- 超过期限后自动剪枝删除
- 第三方归档服务可选择性保留历史数据

**支付规则：**
- 即使未使用满 128 KB，发送者仍需支付完整 128 KB 的 blob 空间费用
- 使用独立的 blob gas 定价机制

### EVM 不可访问性

Blob 数据的独特设计：
- **执行层不可见**：[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)虚拟机（[EVM](https://learnblockchain.cn/tags/EVM?map=EVM)）无法直接读取 blob 内容
- **仅引用可用**：执行层只能访问 blob 数据的承诺（commitment）和引用
- **共识层专属**：blob 数据由信标节点下载和存储
- **验证机制**：通过 KZG 承诺保证数据完整性和可用性

这种设计确保了 blob 不会与常规交易竞争宝贵的 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 执行空间，同时提供了足够的数据可用性保证。

## 使用 Blob 的交易

### Blob 携带交易（Blob-Carrying Transaction）

EIP-4844 引入了新的交易类型：
```
普通交易 + Blob 数据 = Blob 携带交易
```

**交易结构：**
- 包含所有标准交易字段（from、to、value、gas 等）
- 附加一个或多个 blob
- 包含 blob 的 KZG 承诺
- 使用独立的 blob gas 限制和定价

**提交流程：**
1. L2 Sequencer 将批量交易数据编码为 blob
2. 创建 blob 携带交易并签名
3. 提交到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)主网
4. 验证者验证 blob 可用性
5. 交易被包含在区块中
6. Blob 数据在共识层可访问

## 定价机制

### 多维费用市场

基于 [EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 的动态定价模型，但独立于常规 gas：

**Blob [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 价格计算：**
- **基础费用**：根据网络 blob 使用情况动态调整
- **目标使用率**：每个区块 3 个 blob（Dencun），6 个（Pectra）
- **超过目标**：基础费用上升
- **低于目标**：基础费用下降

**不竞争区块空间：**
- Blob 交易不与普通交易竞争 gas 限制
- 拥有独立的 blob gas 限制
- 降低了 L2 成本的不可预测性
- 提供更稳定的数据发布费用

### 成本优势

相比传统 CALLDATA：
- **CALLDATA**：永久存储，16 gas/字节（非零），4 gas/字节（零）
- **Blob**：临时存储，价格随市场波动但通常远低于 CALLDATA
- **费用降低**：L2 使用 blob 后费用降低 10-100 倍
- **实际案例**：Arbitrum、Optimism 在 Dencun 后费用降低 90%

## 对 Layer 2 的价值

### [Rollup](https://learnblockchain.cn/tags/Rollup) 数据发布

**Optimistic Rollups：**
- 将交易批次数据编码为 blob
- 提交到主网作为数据可用性证明
- 挑战期内任何人可以下载验证
- 大幅降低 Sequencer 的运营成本

**ZK Rollups：**
- 将交易数据打包到 blob
- 同时提交[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)
- Blob 提供数据可用性，证明验证计算正确性
- 实现高吞吐量低成本

### 成本节省

**数据发布成本对比：**
- **使用 CALLDATA**：高昂的永久存储费用
- **使用 Blob**：仅为临时存储付费
- **节省幅度**：90% 以上的成本降低
- **用户受益**：L2 交易费用大幅下降

## 数据可用性保证

### 18 天窗口

**设计理念：**
- 18 天足够长，让所有 L2 参与者检索数据
- 18 天足够短，避免存储膨胀
- L2 节点、验证者、桥接器都有充足时间获取数据
- 支持欺诈证明和有效性证明的生成

**检索机制：**
- L2 全节点自动下载相关 blob
- 轻客户端可通过数据可用性采样验证
- 归档节点可选择保留历史数据
- 公共归档服务提供长期访问

### 安全性

**KZG 承诺：**
- 使用 KZG 多项式承诺方案
- 允许高效验证数据完整性
- 支持数据可用性采样（DAS）
- 防止数据扣留攻击

**冗余保证：**
- 多个验证者存储相同 blob
- 网络分布式存储增加可靠性
- PeerDAS 进一步优化存储分布
- 纠删码提供额外冗余

## 扩容路线图

### 当前状态（Pectra 后）

- 目标：每区块 6 个 blob
- 最大值：每区块 9 个 blob
- 总吞吐量：约 1.125 MB/区块（12 秒）= ~94 KB/秒

### PeerDAS (Fusaka)

- 引入数据可用性采样
- 验证者只需存储 1/8 的 blob 数据
- 为更大规模扩容奠定基础
- 支持未来 blob 数量进一步增加

### 完整 Danksharding（未来）

- 目标：16 MB/秒数据吞吐量
- 每个区块数百个 blob
- 完全分片的数据可用性层
- 支持海量 L2 交易

## 监控和工具

**Blob 浏览器：**
- [Blobscan](https://blobscan.com/)：专门的 blob 浏览器
- [Etherscan Blobs](https://etherscan.io/blobs)：Etherscan 的 blob 查看功能
- [Beaconcha.in](https://beaconcha.in/)：信标链浏览器，显示 blob 数据

**开发工具：**
- Web3.js / Ethers.js：支持 blob 交易创建
- Blob 编码库：将数据编码为 blob 格式
- [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 估算工具：计算 blob 交易费用

## 推荐阅读

- [EIP-4844: Shard Blob Transactions](https://learnblockchain.cn/docs/eips/EIPS/eip-4844)
- [EIP-4844, Blobs, and Blob Gas - Blocknative](https://www.blocknative.com/blog/eip-4844-blobs-and-blob-gas-what-you-need-to-know)
- [Breaking Down Ethereum Blobs - Coin Metrics](https://coinmetrics.substack.com/p/state-of-the-network-issue-262)
- [Guide to EIP-4844 and Blob Transactions - Cyfrin](https://www.cyfrin.io/blog/what-is-eip-4844-proto-danksharding-and-blob-transactions)
- [Data Blobs: New Efficiency and Challenges - Covalent](https://www.covalenthq.com/blog/data-blobs-eip-4844-proto-danksharding/)

## 相关概念

- **EIP-4844**
- **Proto-Danksharding**
- **数据可用性**
- **Layer 2**
- **[Rollup](https://learnblockchain.cn/tags/Rollup)**
- **KZG 承诺**
- **PeerDAS**
- **Dencun**
