# Dencun

## 概念简介

Dencun（Deneb-Cancun）是以太坊在 2024 年 3 月 13 日激活的重大升级，代表了以太坊在可扩展性、安全性和交易效率方面最具影响力的更新之一。Deneb 指共识层升级，Cancun 指执行层升级，两者结合简称为 Dencun。

该升级最重要的创新是引入了 **EIP-4844（Proto-Danksharding）**，通过引入临时数据 blob，大幅降低了 Layer 2 网络的交易费用，为以太坊的 Rollup 中心扩容战略奠定了基础。

## 核心特性：EIP-4844

### Proto-Danksharding

EIP-4844 也被称为"Proto-Danksharding"（原型分片），是通往完整 Danksharding 的第一步：

**Blob 交易**

引入了携带 blob 的交易类型，这是常规交易的扩展，附加了额外的二进制大对象（blob）：
- **数据大小**：每个 blob 存储最多 128 KB 数据
- **临时存储**：blob 数据在信标链上存储约 18 天（4096 个 epoch）后自动删除
- **KZG 承诺**：使用 KZG 多项式承诺保证数据完整性
- **独立定价**：blob 不占用区块 gas 空间，使用独立的费用市场

**多维费用市场**

基于 [EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 实现了多维费用市场：
- Blob 携带交易不与其他交易竞争区块空间
- 拥有独立的 blob gas 定价机制
- 根据 blob 使用情况动态调整费用
- 提供更可预测的 L2 成本结构

### 数据可用性

**仅共识层访问**

Blob 数据的设计独特：
- **不可被 EVM 访问**：执行层（[EVM](https://learnblockchain.cn/tags/EVM?map=EVM)）无法直接读取 blob 内容
- **仅引用可见**：执行层只能访问 blob 数据的引用（commitment）
- **共识层存储**：blob 数据由信标节点（共识层）下载和存储
- **有限期保存**：存储约 18 天，足够长让所有 L2 参与者检索数据

**成本优势**

由于临时存储特性，blob 的定价远低于永久存储的 CALLDATA：
- CALLDATA 永久存储在历史记录中
- Blob 在有限时间后被剪枝
- 使 blob 成为 L2 数据发布的经济选择
- 防止永久性存储膨胀

## 对 Layer 2 的影响

### 费用大幅降低

EIP-4844 旨在将以太坊 Layer 2 网络上的 gas 费用降低 **10-100 倍**：

**实际效果**：
- 升级后几天内，Arbitrum 和 Optimism 等 Layer 2 网络报告费用降低高达 **90%**
- Rollup 可以使用 blob 而非昂贵的 CALLDATA 发布数据
- 用户享受到接近中心化平台的低费用体验

### Rollup 中心战略

Dencun 升级成功奠定了以太坊 Rollup 中心扩容方法的基础：
- 主网专注于安全性和去中心化
- Layer 2 提供高吞吐量和低费用
- Blob 作为 L2 与主网的经济数据桥梁
- Proto-Danksharding 是通往完整 Danksharding 的垫脚石

## 其他重要 EIP

除了 EIP-4844，Dencun 还包含多个改进提案：

**共识层（Deneb）：**
- **EIP-4788**：信标区块根在 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 中可用
- **EIP-7044**：永久验证者退出
- **EIP-7045**：增加最大证明包含槽

**执行层（Cancun）：**
- **EIP-1153**：瞬态存储操作码（TSTORE/TLOAD）
- **EIP-5656**：MCOPY 操作码
- **EIP-6780**：限制 SELFDESTRUCT 操作码
- **EIP-7516**：BLOBBASEFEE 操作码

## 技术实现

### Blob 规格

**容量参数（初始）：**
- **目标 blob 数量**：每个区块 3 个
- **最大 blob 数量**：每个区块 6 个
- **单个 blob 大小**：128 KB
- **区块最大 blob 数据**：768 KB（6 × 128 KB）

**定价机制：**
- 基于 [EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 的动态定价
- Blob gas 价格独立于常规 gas
- 根据网络 blob 使用情况调整
- 提供可预测的成本模型

### 数据生命周期

1. **提交**：L2 Sequencer 将批量交易数据打包到 blob 中
2. **发布**：通过 blob 携带交易提交到以太坊主网
3. **可用性**：数据在共识层存储约 18 天
4. **检索**：L2 节点和验证者在此期间可以获取数据
5. **剪枝**：18 天后 blob 数据被自动删除
6. **存档**：第三方归档服务可选择性保存历史 blob 数据

## 升级时间线

- **2023 年初**：EIP-4844 提案和规范制定
- **2023 年下半年**：测试网部署和测试
- **2024 年 2 月**：最终测试网验证
- **2024 年 3 月 13 日**：主网激活

## 历史意义

**扩容里程碑**

Dencun 标志着[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)"The Surge"（扩容）时代的正式开始：
- 首次在主网引入专用数据可用性层
- 验证了 blob 和临时存储的可行性
- 为后续 PeerDAS 和完整 Danksharding 铺平道路

**生态繁荣**

费用降低激发了 L2 生态的爆发性增长：
- 更多用户迁移到 L2
- [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM)、[NFT](https://learnblockchain.cn/tags/NFT)、游戏等应用在 L2 上蓬勃发展
- [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)主网定位为安全结算层
- [Rollup](https://learnblockchain.cn/tags/Rollup) 成为主流用户入口

## 与后续升级的关系

**为 Pectra 铺路**

Dencun 引入的 blob 机制为 Pectra 升级奠定基础：
- Pectra (EIP-7691) 将 blob 容量从 3/6 提升到 6/9
- 进一步降低 L2 费用
- 持续扩展数据可用性

**通往 Fusaka**

Fusaka 升级的 PeerDAS 建立在 Dencun 的 blob 基础上：
- 优化 blob 数据的分发和采样
- 降低验证者的存储和带宽需求
- 支持更大规模的 blob 扩展

## 推荐阅读

- [What Is the Ethereum Dencun Upgrade? - CoinMarketCap](https://coinmarketcap.com/academy/article/what-is-eip-4844-a-quick-guide-for-beginners)
- [Ethereum Dencun Upgrade Explained - DataWallet](https://www.datawallet.com/crypto/ethereum-cancun-upgrade-explained)
- [Dencun Mainnet Announcement - Ethereum Foundation](https://blog.ethereum.org/en/2024/02/27/dencun-mainnet-announcement)
- [Ethereum Dencun Upgrade 2024 - QuickNode](https://blog.quicknode.com/ethereum-dencun-upgrade-2024-proto-danksharding-and-the-surge-era-begins/)
- [Cancun-Deneb (Dencun) FAQ - Ethereum.org](https://ethereum.org/roadmap/dencun/)
- [Ethereum Evolved: EIP-4844 - Consensys](https://consensys.io/blog/ethereum-evolved-dencun-upgrade-part-5-eip-4844)

## 相关概念

- **EIP-4844**
- **Proto-Danksharding**
- **Blob**
- **数据可用性**
- **Layer 2**
- **[Rollup](https://learnblockchain.cn/tags/Rollup)**
- **Pectra**
- **Fusaka**
