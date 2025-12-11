# Fusaka

## 概念简介

Fusaka（Fulu-Osaka）是以太坊在 2025 年 12 月 6 日激活的第二次重大升级，由执行层升级 Osaka 和共识层升级 Fulu 组成。该升级于 2025 年 12 月 6 日 21:49 UTC 激活并在约 15 分钟后最终确定，标志着以太坊 2025 年的第二次升级，也是首个完全符合以太坊统一路线图愿景的升级。

Fusaka 的核心是 PeerDAS（对等数据可用性采样），这是以太坊扩容路线图中的关键技术，旨在通过优化数据可用性来支持更大规模的 Rollup 扩展，而不增加验证者的硬件要求。

## 核心特性

### PeerDAS (EIP-7594)

**Peer Data Availability Sampling**（对等数据可用性采样）是 Fusaka 升级的核心功能：

**工作原理：**
- PeerDAS 将 blob 数据拆分成更小的单元（cells）
- 使用采样和纠删码技术
- 验证者只需获取随机的数据片段，而非下载完整的 blob
- 每个节点只需下载 1/8 的数据即可验证可用性
- 未来可以进一步降低到 1/16 或 1/32

**技术优势：**
- **降低带宽需求**：减少每个节点的带宽和存储压力
- **支持家庭质押者**：无需数据中心级别的硬件
- **扩容潜力**：为最终实现 8 倍 blob 容量增长铺平道路
- **安全性保证**：通过随机采样解决扣留攻击，网络规模越大成功攻击概率越低

**采样机制：**
- PeerDAS 将"样本"定义为"列"（column），是跨所有 blob 的横截面
- 相比"行"（row，即完整 blob），列采样更高效
- 使用伪随机采样方案，网络规模增长时攻击成功率呈次线性下降

### Blob 参数专用分叉（BPO Forks）

Fusaka 引入了 **Blob Parameter Only (BPO)** 分叉机制：
- 允许随时间推移提高每个区块的 blob 数量
- 无需等待完整的硬分叉即可调整 blob 参数
- 实现更灵活的扩容策略
- 根据网络状况动态调整数据可用性容量

### [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) Limit 提升

**EIP-7935：协调提高 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) Limit**
- 协调执行层客户端团队提高默认 gas limit
- 当前 45M gas limit 将有所提升
- 为更复杂的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)交互提供空间
- 支持更高的交易吞吐量

## 路线图定位

### 统一协议战略

以太坊基金会概述了以"协议"为中心的战略，围绕三个长期目标：
1. **扩展 L1**：提高主网吞吐量
2. **扩展 blob**：增加数据可用性容量
3. **改善用户体验**：降低使用门槛

Fusaka 是首个完全符合这一统一愿景的升级，深入推进了以太坊路线图的 **Surge（扩容）**、**Verge（验证）** 和 **Purge（净化）** 阶段。

### 价值累积新时代

富达数字资产（Fidelity Digital Assets）表示，Fusaka 升级标志着以太坊价值累积的新时代。通过 PeerDAS 和 BPO 分叉机制，以太坊可以持续提升扩容能力，同时保持网络的去中心化特性。

## 技术影响

**降低节点成本**

PeerDAS 大幅降低了运行验证者节点的硬件和带宽要求：
- 存储需求减少约 87.5%（1/8 的数据）
- 带宽需求大幅降低
- 支持普通硬件运行全节点
- 提高网络的去中心化程度

**加速 Layer 2 结算**

- 更多的 blob 容量意味着 L2 可以提交更多交易数据
- L2 交易费用进一步降低
- 结算速度提升
- 支持更多 Rollup 同时运行

**向完整 Danksharding 迈进**

Fusaka 是通往完整 Danksharding 的重要里程碑：
- PeerDAS 是 Danksharding 的关键组件
- 验证了数据可用性采样的可行性
- 为未来更大规模扩容奠定基础
- 目标：最终支持 16MB/秒的数据吞吐量

## 与 Pectra 的关系

**接续 Pectra**：Fusaka 在 Pectra 增加 blob 容量（3→6→9）的基础上，通过 PeerDAS 进一步优化数据可用性机制

**互补功能**：
- Pectra 专注于[账户](https://learnblockchain.cn/tags/账户?map=EVM)抽象和质押改进
- Fusaka 专注于数据可用性和扩容
- 两者共同推进以太坊的可扩展性和易用性

## 后续路线图

### Glamsterdam（2026）

Fusaka 之后，以太坊路线图继续推进到 **"Glamsterdam"**，计划于 2026 年发布：
- 结合"Glamour"和 Devcon 举办城市"Amsterdam"
- 将进一步推进路线图的各个阶段
- 继续优化网络性能和用户体验

### 每年两次升级节奏

Fusaka 的推出确立了以太坊新的升级节奏：
- 每年进行两次重大升级
- 更快速地迭代和改进
- 更及时地响应生态需求
- 保持技术领先地位

## 社区与生态影响

**开发者准备**

[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)开发者在 2025 年 11 月积极准备 Fusaka 升级，确保客户端兼容性和平滑过渡。

**L2 生态受益**

[Rollup](https://learnblockchain.cn/tags/Rollup) 项目（如 Arbitrum、Optimism、zkSync、Starknet 等）将直接受益于 PeerDAS 带来的成本降低和容量提升。

**价值主张增强**

通过持续的技术升级，[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)巩固了其作为可扩展、去中心化结算层的地位，吸引更多用户和开发者。

## 推荐阅读

- [Fulu-Osaka (Fusaka) - Ethereum.org](https://ethereum.org/roadmap/fusaka/)
- [How the Fusaka Upgrade Advances Ethereum's Long-Term Roadmap - Cointelegraph](https://cointelegraph.com/explained/how-the-fusaka-upgrade-fits-into-ethereum-s-long-term-roadmap)
- [Reaching New Scale: Ethereum's Fusaka Upgrade - Coin Metrics](https://coinmetrics.substack.com/p/state-of-the-network-issue-340)
- [Ethereum's Fusaka Upgrade Signals New Era - Fidelity Digital Assets](https://www.coindesk.com/tech/2025/11/20/ethereum-s-fusaka-upgrade-signals-new-era-for-value-accrual-fidelity-digital-assets)
- [Ethereum Fusaka Upgrade: What You Need to Know - QuickNode](https://blog.quicknode.com/ethereum-fusaka-upgrade-what-you-need-to-know/)

## 相关概念

- **PeerDAS**
- **EIP-7594**
- **数据可用性采样**
- **Danksharding**
- **Blob**
- **Pectra**
- **Layer 2**
- **[Rollup](https://learnblockchain.cn/tags/Rollup)**
