# zkSTARK

## 概念简介

zkSTARK 全称 Zero-Knowledge Scalable Transparent Argument of Knowledge（零知识可扩展透明知识论证），是一种[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)技术，由 StarkWare 团队的 Eli Ben-Sasson 等人于 2018 年提出。与 zkSNARK 相比，zkSTARK 的核心优势在于透明性（无需可信设置）、可扩展性和抗量子计算攻击能力，但代价是证明体积较大。

zkSTARK 的名称揭示了其关键特性：零知识保护隐私信息，可扩展性支持处理大规模计算，透明性消除了可信设置的需求，知识论证确保证明者确实拥有相关知识。透明性是 zkSTARK 最显著的优势之一，使其在安全性假设上比需要可信设置的 zkSNARK 方案更加纯粹和可审计。

## 核心特性

**透明性（Transparent）**

zkSTARK 不需要可信设置（Trusted Setup），所有公共参数都可以公开生成，无需依赖秘密随机数。这消除了"有毒废料"的风险，使得系统更加透明和可审计。透明性是 zkSTARK 最显著的优势，避免了 zkSNARK 中多方计算仪式的复杂性和潜在风险。

**可扩展性（Scalable）**

zkSTARK 的证明生成和验证时间呈准线性增长（quasi-linear），意味着即使面对大规模计算，性能下降也较为温和。和 Replay Computation 的验证耗时相比，zkSTARK 的证明和验证耗时分别与之呈拟线性关系和对数关系。证明生成时间约为 O(log² n)，而认证的时间复杂度是对数的，其中 n 为计算规模。这种可扩展性使 zkSTARK 适合处理复杂的计算任务。

**抗量子安全**

zkSTARK 基于哈希函数和信息论安全性，不依赖[椭圆曲线密码学](https://learnblockchain.cn/tags/椭圆曲线密码学)或配对运算。STARK 中的密码学元素仅为 collision-resistant hash function。因此，如果选择理想的 hash 函数，STARK 为抗量子攻击的。这使得 zkSTARK 能够抵抗量子计算机攻击。随着量子计算技术的发展，这种抗量子特性变得越来越重要。

**证明体积**

zkSTARK 的证明体积比 zkSNARK 大，通常在几十到几百 KB。虽然比 zkSNARK（几百字节）大得多，但考虑到无需可信设置和抗量子安全的优势，这种体积增加在许多应用场景中是可以接受的，特别是在带宽不是主要瓶颈的情况下。

## 技术原理

zkSTARK 采用 FRI（Fast Reed-Solomon Interactive Oracle Proof of Proximity）协议作为核心。该技术利用多项式承诺和 Merkle 树结构，通过重复的低度测试过程验证多项式的低度性。整个过程基于 FRI 协议的递归折叠机制，每一步都将多项式的度数减半，直到达到足够小的度数可以直接验证。

计算过程首先被编码为代数中间表示（AIR, Algebraic Intermediate Representation）。证明者将执行轨迹（trace）转换为多项式，并使用 Merkle 树承诺这些多项式。验证者通过随机采样检查多项式的约束满足情况。整个协议通过 Fiat-Shamir 启发式转换实现非交互化，在区块链环境中只需提交证明和 Merkle 根。

## 与 zkSNARK 对比

| 特性 | [zkSNARK](https://learnblockchain.cn/tags/zkSNARK) | zkSTARK |
|------|---------|---------|
| Trusted Setup | 需要 | 不需要（透明）|
| 证明大小 | 极小（~200 bytes）| 较大（~100 KB）|
| 验证时间 | 常数时间 | 对数时间 |
| 抗量子性 | 否 | 是 |
| [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本 | 更低 | 更高 |
| 密码学基础 | 椭圆曲线配对 | 哈希函数 |

## 应用场景

**Layer2 扩容方案**

StarkNet 和 StarkEx 是基于 zkSTARK 的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) [Layer2](https://learnblockchain.cn/tags/Layer2?map=EVM) 解决方案。dYdX、Immutable X、Sorare 等项目使用 StarkEx 实现高吞吐量和低成本的去中心化交易。StarkNet 进一步提供了通用[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)平台，支持使用 Cairo 语言开发复杂的去中心化应用。

**可验证计算**

zkSTARK 可用于证明复杂计算的正确性，而不泄露计算细节。这在隐私计算、外包计算和机构级应用中尤为重要。企业可以验证计算结果而无需信任执行方，保护了商业机密。

**隐私保护与合规**

利用 zkSTARK 可以实现隐私交易、身份认证和合规证明。用户可以证明满足某些条件（如财富证明、年龄验证）而不透露具体信息。监管机构可以验证合规性而不侵犯隐私。

**数据完整性验证**

虽然 zkSTARK 常用于计算验证，但其透明性使其也适合数据完整性和存储证明场景。去中心化存储系统可以使用 zkSTARK 证明数据可用性和完整性。

## 发展历程

2018 年，Eli Ben-Sasson 等人发表了 zkSTARK 论文，提出了透明的[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)方案。同年，StarkWare 公司成立，专注于 [zkSTARK](https://learnblockchain.cn/tags/zkSTARK) 的商业化应用。

2019 年，StarkWare 推出了 [Cairo](https://learnblockchain.cn/tags/Cairo?map=Web3) 编程语言，用于编写可生成 STARK 证明的程序。同年，StarkEx 开始为 dYdX 等 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 项目提供扩容服务。

2021 年，StarkNet Alpha 测试网启动，提供了通用的 [Layer2](https://learnblockchain.cn/tags/Layer2?map=EVM) 网络，支持复杂的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)。dYdX 基于 StarkEx 的永续合约交易所成为去中心化衍生品交易的领军项目。

2022-2023 年，StarkNet 主网逐步开放和成熟，推出了代币 STRK。越来越多的项目选择基于 [zkSTARK](https://learnblockchain.cn/tags/zkSTARK) 技术构建，涵盖 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM)、[NFT](https://learnblockchain.cn/tags/NFT)、游戏等多个领域。

## 推荐阅读

- [理解 zk-SNARKs 和 zk-STARKS 的区别](https://blog.chain.link/zk-snarks-vs-zk-starks-zh/)
- [零知识证明之争：STARK还是SNARK？- CSDN](https://blog.csdn.net/Galaxytraveller/article/details/133845919)
- [理解零知识证明算法之 Zk-stark - 登链社区](https://learnblockchain.cn/article/269)
- [长文详解零知识证明协议——从zk-STARK谈起 - 知乎](https://zhuanlan.zhihu.com/p/362936724)
- [zkSTARK 论文](https://eprint.iacr.org/2018/046)

## 相关链接

- [StarkWare 官网](https://starkware.co/)
- [Cairo 编程语言](https://www.cairo-lang.org/)
- [StarkNet 文档](https://docs.starknet.io/)

## 相关概念

- **[zkSNARK](https://learnblockchain.cn/tags/zkSNARK)**
- **StarkWare**
- **StarkNet**
- **StarkEx**
- **FRI**
- **[Cairo](https://learnblockchain.cn/tags/Cairo?map=Web3)**
- **抗量子密码学**
- **哈希函数**
- **Bulletproofs**
