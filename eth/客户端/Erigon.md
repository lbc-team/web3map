# Erigon

## 概念简介

Erigon（原名 Turbo-Geth）是以太坊执行层客户端的高效实现，使用 [Go](https://learnblockchain.cn/tags/Go) 语言开发，专注于性能优化和存储效率。Erigon 由 Ledgerwatch 团队开发，其设计目标是提供最快的同步速度和最小的磁盘占用，使运行以太坊全节点和归档节点更加经济可行。

Erigon 通过重新设计数据库架构、优化状态存储和改进同步算法，实现了相比传统客户端（如 Geth）数倍的性能提升。它特别适合需要快速同步、运行归档节点或在磁盘空间受限环境中使用。Erigon 已经成为以太坊基础设施提供商、区块浏览器和数据分析平台的首选客户端。

## 核心特性

### 高效的存储架构
Erigon 的核心创新在于其独特的数据库设计：
- **扁平存储模型**：摒弃传统的 Merkle Patricia Trie 存储，采用扁平的键值存储，大幅减少磁盘占用
- **MDBX 数据库**：使用高性能的 MDBX（基于 LMDB）作为存储引擎，提供卓越的读写性能
- **历史数据压缩**：智能压缩历史状态数据，归档节点的磁盘占用可以比 Geth 减少 70% 以上
- **增量快照**：只存储状态变化，避免重复存储相同数据

这些优化使得运行以太坊归档节点从需要数 TB 磁盘降低到 1-2 TB。

### 极速同步
Erigon 的同步速度在以太坊客户端中名列前茅：
- **并行下载**：充分利用多核 CPU 和网络带宽，并行下载和处理区块
- **分阶段同步**：将同步分为多个优化的阶段（Headers、Bodies、Execution 等），每个阶段独立优化
- **增量验证**：边下载边验证，减少等待时间
- **快速恢复**：中断后可以快速恢复同步，无需重新开始

全节点同步时间可以缩短到 1-2 天，归档节点也可以在合理时间内完成同步。

### 模块化分阶段架构
Erigon 采用独特的分阶段（Staged Sync）架构：
1. **Headers 阶段**：下载区块头
2. **Block Hashes 阶段**：下载区块哈希
3. **Bodies 阶段**：下载区块体
4. **Senders 阶段**：恢复交易发送者
5. **Execution 阶段**：执行交易，更新状态
6. **HashState 阶段**：计算状态哈希
7. **Intermediate Hashes 阶段**：计算中间哈希
8. **Account Hashing 阶段**：计算[账户](https://learnblockchain.cn/tags/账户?map=EVM)哈希
9. **Storage Hashing 阶段**：计算存储哈希

每个阶段可以独立优化和并行化，提供最佳性能。

### 完整的归档节点支持
Erigon 对归档节点进行了深度优化：
- **高效历史查询**：快速查询任意区块高度的状态
- **trace 和 debug API**：完整支持以太坊的 trace 和 debug RPC 方法
- **历史数据索引**：为历史数据构建索引，加速查询
- **合理的资源占用**：即使是归档节点，也能在普通硬件上运行

### RPC 和 API
Erigon 提供全面的 API 支持：
- **标准 JSON-RPC**：兼容以太坊标准 API
- **扩展 API**：额外的 trace、debug 方法
- **多协议支持**：HTTP、WebSocket、IPC
- **高并发处理**：优化的 RPC 服务器，支持大量并发请求

## 客户端特点

**存储效率领先**：通过创新的存储架构，Erigon 在磁盘占用方面遥遥领先：
- 全节点：约 400-600 GB（Geth 需 800+ GB）
- 归档节点：约 1-2 TB（Geth 需 10+ TB）

**同步速度最快**：分阶段同步和并行化设计使 Erigon 成为同步速度最快的以太坊客户端之一。

**开源社区驱动**：完全开源，采用 LGPL-3.0 许可证。活跃的开发者社区，快速迭代和改进。

**模块化设计**：清晰的模块化架构，便于理解、维护和扩展。开发者可以轻松贡献代码或定制功能。

**性能监控**：内置详细的性能指标和诊断工具，便于优化和故障排除。

**向后兼容**：完全兼容以太坊协议和现有工具链，可以无缝替换其他客户端。

## 发展历程

**2019年**：项目以 Turbo-Geth 的名字启动，目标是优化 Geth 的性能。

**2020年**：推出创新的 Staged Sync 架构，同步速度大幅提升。开始被以太坊社区关注。

**2021年3月**：Turbo-Geth 更名为 Erigon，标志着项目的成熟和独立身份。获得以太坊基金会和其他组织的资助。

**2021-2022年**：持续优化存储和同步算法，支持[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)主网硬分叉。越来越多的基础设施提供商采用 Erigon。

**2022年9月**：成功支持[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)合并（The Merge），提供稳定的执行层客户端服务。

**2023年**：支持 Shanghai/Capella 和 Cancun/Deneb 升级。进一步优化归档节点性能，成为运行归档节点的首选。

**2024年至今**：继续推动性能边界，探索新的优化技术。扩展生态系统支持，包括 Layer 2 和其他 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 链。

## 应用场景

- **归档节点服务商**：提供历史数据查询服务，区块浏览器、分析平台
- **DApp 基础设施**：为 [DApp](https://learnblockchain.cn/tags/DApp) 提供快速可靠的 RPC 服务
- **数据分析**：链上数据分析、研究、审计
- **MEV 搜索者**：需要快速访问链上数据和历史状态
- **开发者**：本地开发环境，需要快速同步测试网或主网
- **质押服务商**：与共识层客户端配合，运行验证者
- **资源受限环境**：磁盘空间有限的 VPS 或服务器

## 相关链接

- GitHub：https://github.com/ledgerwatch/erigon
- 文档：https://github.com/ledgerwatch/erigon#documentation
- Discord：https://github.com/ledgerwatch/erigon#getting-in-touch
- Telegram：https://t.me/ErigonClient
- Twitter：https://twitter.com/ErigonEth
