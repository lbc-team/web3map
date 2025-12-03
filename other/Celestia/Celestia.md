## Celestia

### 概念简介

Celestia 是首个模块化区块链网络，专注于提供数据可用性（Data Availability）层服务。与传统的单体区块链不同，Celestia 将共识和数据可用性与执行层解耦，允许开发者在其之上构建各种类型的区块链和 Rollup，而无需关心底层的数据存储和共识问题。

Celestia 由 Mustafa Al-Bassam 于 2019 年提出概念（当时称为 LazyLedger），2021 年正式更名为 Celestia 并开始开发。2023 年 10 月主网上线，标志着模块化区块链时代的正式到来。Celestia 的核心创新是数据可用性采样（Data Availability Sampling, DAS）技术，使得轻节点也能高效验证数据可用性。

截至 2024 年，Celestia 已经成为模块化区块链生态的基础设施，支持多个 Rollup 和区块链项目在其之上构建，包括 Manta Pacific、Lyra、Aevo 等。TIA 作为 Celestia 的原生代币，用于支付数据发布费用和网络安全。

### 核心特性

**数据可用性层**

Celestia 专注于解决数据可用性问题，确保区块链数据被正确发布并可供验证。Rollup 可以将交易数据发布到 Celestia，而不必依赖以太坊主网的昂贵 calldata 或 blob 空间。Celestia 通过纠删码和数据可用性采样技术，使得即使只有部分节点存储数据，网络仍能保证数据的完整性和可访问性。

**数据可用性采样（DAS）**

DAS 是 Celestia 最重要的技术创新。轻节点通过随机采样少量数据片段，就能以高概率验证完整区块的数据可用性，而无需下载整个区块。这使得 Celestia 可以支持远超传统区块链的数据吞吐量，同时保持轻客户端的验证能力，增强了网络的去中心化程度。

**主权 Rollup**

Celestia 支持"主权 Rollup"概念，这些 Rollup 只使用 Celestia 作为数据可用性层，而将结算和争议解决逻辑放在 Rollup 自身。主权 Rollup 拥有完全的自主权，可以自定义升级机制、治理规则和执行环境，不受任何结算层的限制。

**Tendermint 共识**

Celestia 采用 Tendermint BFT 共识算法的改进版本，提供即时最终性和高性能。验证者通过质押 TIA 代币参与共识，诚实验证者获得区块奖励和交易费用，恶意行为将导致质押资产被罚没。

**命名空间 Merkle 树**

Celestia 引入了命名空间 Merkle 树（Namespaced Merkle Tree, NMT），允许多个 Rollup 或应用将数据发布到同一个 Celestia 区块，但每个应用只需下载和验证自己命名空间的数据。这种设计提高了数据隔离性和查询效率。

### 技术优势

**极致的可扩展性**

Celestia 的数据吞吐量随着轻节点数量的增加而线性增长。理论上，如果有足够多的轻节点进行采样，Celestia 可以支持数 GB 级别的区块大小，为大规模应用提供数据基础设施。

**成本大幅降低**

相比以太坊主网，在 Celestia 上发布数据的成本可降低 100-1000 倍。这使得 Rollup 可以显著降低用户的交易费用，推动 Web3 应用的大规模采用。

**灵活的执行环境**

开发者可以在 Celestia 之上使用任意执行环境（EVM、WASM、Move、SVM 等），甚至创建全新的虚拟机，而不受底层数据可用性层的限制。这种模块化设计为创新提供了巨大空间。

**增强的去中心化**

DAS 技术使得资源受限的设备（如手机）也能参与数据可用性验证，大幅提高了网络的去中心化程度。这与传统区块链只有少数全节点能验证形成鲜明对比。

### 发展历程

**2019 年：LazyLedger 概念提出**

Mustafa Al-Bassam 发布 LazyLedger 白皮书，首次系统性提出模块化区块链和数据可用性采样的概念，奠定了 Celestia 的理论基础。

**2021 年：更名与开发**

项目更名为 Celestia，获得 Polychain Capital、Binance Labs 等机构的种子轮投资。团队开始全力开发主网，构建开发者工具和生态系统。

**2022 年：测试网与融资**

Celestia 测试网陆续上线，开发者开始在其上构建 Rollup 和应用。项目完成 5500 万美元 A 轮和 B 轮融资，估值达 10 亿美元。

**2023 年 10 月：主网上线**

Celestia 主网正式启动，TIA 代币开始流通。首批 Rollup 项目迁移到 Celestia 主网，验证了技术方案的可行性和性能。

**2024 年：生态爆发**

越来越多的 Rollup 采用 Celestia 作为数据可用性层，包括 Manta Pacific、Lyra、Aevo、Dymension 等。Celestia 成为模块化区块链运动的旗舰项目，推动了整个行业向模块化架构演进。

### 应用场景

**Rollup 数据可用性**：为 Optimistic Rollup 和 ZK Rollup 提供低成本的数据发布服务。

**主权应用链**：开发者构建完全自主的应用链，只依赖 Celestia 作为数据层。

**链上游戏和社交**：支持高吞吐量的游戏和社交应用，以可承受的成本在链上运行。

**跨链通信**：作为多个 Rollup 之间的共享数据层，促进跨链互操作。

**实验性区块链**：为新的共识机制、虚拟机或加密技术提供快速实验平台。

### 相关链接

- [Celestia 官网](https://celestia.org/)
- [Celestia 文档](https://docs.celestia.org/)
- [Celestia GitHub](https://github.com/celestiaorg)
- [LazyLedger 白皮书](https://arxiv.org/abs/1905.09274)
- [模块化区块链详解](https://celestia.org/learn/)
- [Celestia 区块浏览器](https://celenium.io/)
