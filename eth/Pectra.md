# Pectra

## 概念简介

Pectra（Prague-Electra）是以太坊在 2025 年 5 月 7 日激活的重大升级，是继 Dencun 之后的又一次双层硬分叉。Prague 指执行层升级，Electra 指共识层升级，两者结合简称为 Pectra。

该升级于 2025 年 5 月 7 日 10:05:11 UTC 在以太坊主网激活（epoch 364032），引入了 11 个关键的以太坊改进提案（EIP），专注于可扩展性、安全性、质押操作和开发者工具的改进。Pectra 是迄今为止包含最多 EIP 的以太坊升级。

## 核心 EIP 提案

### 账户抽象与用户体验

**EIP-7702：临时账户委托**

这是迈向广泛账户抽象的重要一步，使用户能够为其外部拥有账户（EOA）增强[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)功能。通过 EIP-7702 实现的智能账户将支持：
- **Gas 赞助**：允许第三方代付交易费用
- **批量交易**：一次性执行多个操作
- **基于密钥的认证**：使用 Passkey 等现代认证方式
- **交易模拟**：在执行前预览交易结果

这大幅降低了用户使用以太坊的门槛，提升了用户体验。

### 质押改进

**EIP-7251：增加最大有效余额**

将单个验证者的最大有效余额从 32 ETH 提高到 2048 ETH：
- 验证者可以在单个验证者中质押 32 到 2048 ETH
- 运行多个验证者的质押者可以将它们聚合为一个
- 简化操作并减少网络开销
- 降低验证者集合的规模，提高网络效率

**EIP-7002：执行层触发的退出**

引入新合约，允许使用执行层提款凭证触发验证者退出：
- 质押者可以通过调用特殊合约的函数退出验证者
- 无需访问共识层客户端
- 简化质押服务提供商的操作流程
- 提高质押的灵活性

**EIP-6110：链上存款处理**

从执行层到共识层传递存款的新方式：
- 允许即时处理存款
- 降低实现复杂性
- 提高存款确认的可靠性
- 减少验证者激活等待时间

### Layer 2 可扩展性

**EIP-7691：提高 Blob 容量**

将平均 blob 数量从 3 增加到 6，最大数量从 6 增加到 9：
- **双倍吞吐量**：使以太坊 blob 吞吐量翻倍
- **降低 L2 成本**：为 Rollup 提供更多数据可用性空间
- **未来扩展**：为进一步扩展（如 PeerDAS）奠定基础
- **动态调整**：基于 [EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 的 blob 费用市场

**EIP-7623：提高 Calldata 定价**

增加 Calldata 的 Gas 价格：
- Calldata 从 4/16 Gas/字节增加到 10/40 Gas/字节
- 仅对数据密集型交易生效
- 将最大区块大小从 7.15MB 降至 0.75MB
- 激励使用 blob 而非 calldata
- 推动 L2 迁移到更便宜的 blob 存储

### 开发者工具

**EIP-2537：BLS12-381 曲线预编译**

为 BLS12-381 曲线操作添加预编译合约：
- 改进密码学能力
- 支持更高效的签名聚合
- 增强隐私保护功能
- 降低 ZK 证明的 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本

**EIP-2935：历史区块哈希存储**

将历史区块哈希的链上存储时间从 51 分钟（256 个区块）延长到 27 小时（8191 个区块）：
- 提高依赖历史数据的应用的可靠性
- 简化状态无效性证明
- 支持更长时间范围的 BLOCKHASH 操作
- 为未来的无状态以太坊铺平道路

**其他 EIP：**
- **EIP-7685**：请求引擎 API
- **EIP-7840**：为 CL 添加 Blob 计划
- **EIP-7742**：无约束 Blob [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 价格

## 影响与意义

**用户体验提升**

[EIP-7702](https://learnblockchain.cn/tags/EIP7702?map=EVM) 使智能账户功能更易于访问，降低了以太坊的使用门槛。用户可以享受到类似 Web2 的便利体验，同时保持去中心化和自主托管的优势。

**质押生态优化**

质押相关的改进降低了运行验证者的复杂性，提高了灵活性。这有助于吸引更多质押参与者，增强网络的安全性和去中心化程度。

**Layer 2 扩容加速**

Blob 容量的增加为 [Rollup](https://learnblockchain.cn/tags/Rollup) 提供了更多廉价的数据可用性空间，同时 Calldata 定价的调整激励 L2 迁移到更经济的 blob 存储方案。这直接降低了 L2 的交易费用。

**开发者工具增强**

新的预编译合约和历史数据存储改进为开发者提供了更强大的工具，支持构建更复杂和创新的应用。

## 升级时间线

- **2024 年下半年**：EIP 提案讨论和测试网部署
- **2025 年 2 月**：Hoodi 测试网激活
- **2025 年 3 月**：Mekong 测试网激活
- **2025 年 4 月**：Sepolia 和 Holesky 测试网激活
- **2025 年 5 月 7 日**：主网激活

## 与其他升级的关系

**继承 Dencun**：在 Dencun 引入 blob 的基础上进一步扩展容量

**为 Fusaka 铺路**：为下一次升级（Fusaka）的 PeerDAS 等功能奠定基础

**推进路线图**：符合[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)"The Surge"（扩容）和"The Scourge"（MEV 治理）路线图的目标

## 社区反响

Pectra 升级获得了广泛的社区支持，被认为是[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)历史上最重要的升级之一。特别是[账户](https://learnblockchain.cn/tags/账户?map=EVM)抽象和质押改进，被视为解决长期以来用户体验和质押门槛问题的关键里程碑。

## 推荐阅读

- [Prague-Electra (Pectra) - Ethereum.org](https://ethereum.org/roadmap/pectra/)
- [Ethereum's Prague/Electra Upgrade - Crypto.com University](https://crypto.com/en/university/ethereum-pectra-prague-electra-upgrade)
- [Ethereum Pectra Upgrade - Consensys](https://consensys.io/ethereum-pectra-upgrade)
- [Ethereum Pectra Upgrade: Dev Guide to 11 EIPs - Alchemy](https://www.alchemy.com/blog/ethereum-pectra-upgrade-dev-guide-to-11-eips)
- [Ethereum Pectra Upgrade - QuickNode](https://www.quicknode.com/guides/ethereum-development/ethereum-upgrades/pectra-upgrade)
- [Pectra Mainnet Announcement - Ethereum Foundation](https://blog.ethereum.org/en/2025/04/23/pectra-mainnet)

## 相关概念

- **[账户](https://learnblockchain.cn/tags/账户?map=EVM)抽象**
- **[EIP-7702](https://learnblockchain.cn/tags/EIP7702?map=EVM)**
- **质押**
- **Blob**
- **Dencun**
- **Fusaka**
- **Layer 2**
- **[Rollup](https://learnblockchain.cn/tags/Rollup)**
