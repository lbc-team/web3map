## EigenDA

### 概念简介

EigenDA 是由 EigenLayer 推出的去中心化数据可用性（Data Availability）层，是首个基于 EigenLayer 重新质押机制构建的主动验证服务（AVS）。EigenDA 为以太坊 Rollup 提供了高吞吐量、低成本的数据可用性解决方案，相比直接使用以太坊主网的 blob 空间，可以将数据存储成本降低 100 倍以上。

数据可用性是 Rollup 扩容方案的关键瓶颈。Rollup 需要将交易数据发布到链上，以便任何人都可以重建 Rollup 的状态。传统上，这些数据存储在以太坊主网上，成本高昂且容量有限。EigenDA 通过利用 EigenLayer 的共享安全模型，创建了一个专用的数据可用性层，既保持了去中心化的安全性，又大幅降低了成本，提高了吞吐量。

截至 2024 年，EigenDA 已吸引多个主流 Rollup 项目采用，包括 Mantle、Celo、Polymer 等，成为以太坊生态中重要的模块化基础设施组成部分。

### 核心特性

**基于重新质押的安全性**

EigenDA 的安全性来自 EigenLayer 的重新质押机制。以太坊验证者可以选择将已质押的 ETH 重新质押到 EigenDA，为数据可用性提供加密经济安全保障。这种共享安全模型使得 EigenDA 无需从零建立自己的验证者网络，直接继承了以太坊数十亿美元的质押安全性。

**高吞吐量设计**

EigenDA 采用纠删码（Erasure Coding）技术，将数据分片并分散存储在多个验证者节点上。即使部分节点离线或数据丢失，系统仍能恢复完整数据。这种设计允许 EigenDA 实现极高的数据吞吐量，理论上可达每秒数百 MB，远超以太坊主网的容量。

**数据可用性采样（DAS）**

EigenDA 支持数据可用性采样技术，轻客户端只需下载随机的小部分数据片段，就可以高概率验证完整数据的可用性。这大幅降低了验证成本，使得更多节点能够参与验证，增强了网络的去中心化程度。

**动态定价机制**

EigenDA 根据网络使用情况动态调整数据存储价格。在网络空闲时，价格较低；在高峰期，价格上涨以反映供需关系。这种市场化定价机制既保证了网络资源的高效利用，又为 Rollup 提供了可预测的成本结构。

### 核心优势

**成本优势显著**

相比以太坊主网的 calldata 或 blob 空间，EigenDA 的数据存储成本可降低 100-1000 倍。对于 Rollup 而言，数据可用性成本通常占总成本的 90% 以上，使用 EigenDA 可以将用户的交易费用降低一个数量级，极大提升 Rollup 的竞争力。

**可扩展性强**

EigenDA 的吞吐量随验证者数量线性增长，没有传统区块链的带宽瓶颈。随着更多 EigenLayer 验证者加入 EigenDA，网络容量可以持续扩展，满足未来数千个 Rollup 的数据需求。

**安全性保障**

EigenDA 继承了以太坊的加密经济安全性，验证者需要质押 ETH 作为抵押品。如果验证者未能履行数据存储和提供义务，其质押资产将被罚没。这种强大的经济激励确保了数据的持久性和可用性。

**快速最终性**

EigenDA 可以在数秒内提供数据可用性证明，远快于以太坊主网的 12 秒区块时间。这种快速确认使得 Rollup 能够提供更流畅的用户体验，接近中心化应用的响应速度。

### 发展历程

**2023 年初期开发**

EigenLayer 团队开始设计和开发 EigenDA，作为展示重新质押概念的首个应用案例。团队与多个 Rollup 项目沟通需求，确定技术架构和功能规格。

**2023 年中测试网上线**

EigenDA 测试网正式启动，早期采用者开始集成测试。Mantle Network 成为首个公开宣布采用 EigenDA 的主流 Rollup，验证了技术方案的可行性。

**2024 年主网启动**

EigenDA 主网正式上线，开始为生产环境的 Rollup 提供服务。多个 Rollup 陆续迁移数据可用性层到 EigenDA，用户开始享受到更低的交易费用。

**2024 年生态扩展**

越来越多的 Rollup 宣布集成 EigenDA，包括 Celo、Polymer、Fuel 等。EigenDA 的数据吞吐量持续增长，成为以太坊模块化生态中不可或缺的基础设施层。

### 应用场景

**Rollup 数据存储**：为 Optimistic Rollup 和 ZK Rollup 提供低成本的数据发布服务，降低用户交易费用。

**高频应用**：支持游戏、社交等高频交易应用的数据需求，使得这些应用能够以可承受的成本在链上运行。

**跨链桥**：为跨链桥提供高效的消息传递和数据验证服务。

**数据密集型 DApp**：支持链上数据市场、去中心化存储等需要大量数据存储的应用。

### 相关链接

- [EigenDA 官网](https://www.eigenda.xyz/)
- [EigenDA 文档](https://docs.eigenlayer.xyz/eigenda/overview)
- [EigenLayer GitHub](https://github.com/Layr-Labs/eigenda)
- [数据可用性详解](https://ethereum.org/en/developers/docs/data-availability/)
- [Mantle Network 采用 EigenDA](https://www.mantle.xyz/blog/developers/mantle-adopts-eigenda)
