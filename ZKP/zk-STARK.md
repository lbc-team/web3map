# zk-STARK

## 概念简介

zk-STARK（Zero-Knowledge Scalable Transparent Argument of Knowledge，零知识可扩展透明知识论证）是一种零知识证明技术，由 StarkWare 团队的 Eli Ben-Sasson 等人于 2018 年提出。与 zk-SNARK 相比，zk-STARK 的核心优势在于透明性（无需可信设置）、可扩展性和抗量子计算攻击能力，但代价是证明体积较大。

zk-STARK 的名称揭示了其关键特性：零知识保护隐私信息，可扩展性支持处理大规模计算，透明性消除了可信设置的需求，知识论证确保证明者确实拥有相关知识。透明性是 zk-STARK 最显著的优势之一，使其在安全性假设上比需要可信设置的 zk-SNARK 方案更加纯粹和可审计。

## 核心特性

**透明性**

zk-STARK 不需要可信设置（Trusted Setup），所有公共参数都可以公开生成，无需依赖秘密随机数。这消除了"有毒废料"的风险，使得系统更加透明和可审计。透明性是 zk-STARK 最显著的优势，避免了 zk-SNARK 中多方计算仪式的复杂性和潜在风险。

**抗量子安全**

zk-STARK 基于哈希函数和信息论安全性，不依赖椭圆曲线密码学或配对运算。这使得 zk-STARK 能够抵抗量子计算机攻击。随着量子计算技术的发展，这种抗量子特性变得越来越重要。

**可扩展性**

zk-STARK 的证明生成和验证时间呈准线性增长（quasi-linear），意味着即使面对大规模计算，性能下降也较为温和。证明生成时间约为 O(log² n)，其中 n 为计算规模。这种可扩展性使 zk-STARK 适合处理复杂的计算任务。

**证明体积**

zk-STARK 的证明体积比 zk-SNARK 大，通常在几十到几百 KB。虽然比 zk-SNARK（几百字节）大得多，但考虑到无需可信设置和抗量子安全的优势，这种体积增加在许多应用场景中是可以接受的，特别是在带宽不是主要瓶颈的情况下。

## 技术原理

zk-STARK 采用 FRI（Fast Reed-Solomon Interactive Oracle Proof of Proximity）协议作为核心。该技术利用多项式承诺和 Merkle 树结构，通过重复的低度测试过程验证多项式的低度性。整个过程基于 FRI 协议的递归折叠机制，每一步都将多项式的度数减半，直到达到足够小的度数可以直接验证。

计算过程首先被编码为代数中间表示（AIR, Algebraic Intermediate Representation）。证明者将执行轨迹（trace）转换为多项式，并使用 Merkle 树承诺这些多项式。验证者通过随机采样检查多项式的约束满足情况。整个协议通过 Fiat-Shamir 启发式转换实现非交互化，在区块链环境中只需提交证明和 Merkle 根。

## 应用场景

**Layer2 扩容方案**

StarkNet 和 StarkEx 是基于 zk-STARK 的以太坊 Layer2 解决方案。dYdX、Immutable X、Sorare 等项目使用 StarkEx 实现高吞吐量和低成本的去中心化交易。StarkNet 进一步提供了通用智能合约平台，支持使用 Cairo 语言开发复杂的去中心化应用。

**可验证计算**

zk-STARK 可用于证明复杂计算的正确性，而不泄露计算细节。这在隐私计算、外包计算和机构级应用中尤为重要。企业可以验证计算结果而无需信任执行方，保护了商业机密。

**隐私保护与合规**

利用 zk-STARK 可以实现隐私交易、身份认证和合规证明。用户可以证明满足某些条件（如财富证明、年龄验证）而不透露具体信息。监管机构可以验证合规性而不侵犯隐私。

**数据完整性验证**

虽然 zk-STARK 常用于计算验证，但其透明性使其也适合数据完整性和存储证明场景。去中心化存储系统可以使用 zk-STARK 证明数据可用性和完整性。

## 发展历程

2018 年，Eli Ben-Sasson 等人发表了 zk-STARK 论文，提出了透明的零知识证明方案。同年，StarkWare 公司成立，专注于 zk-STARK 的商业化应用。

2019 年，StarkWare 推出了 Cairo 编程语言，用于编写可生成 STARK 证明的程序。同年，StarkEx 开始为 dYdX 等 DeFi 项目提供扩容服务。

2021 年，StarkNet Alpha 测试网启动，提供了通用的 Layer2 网络，支持复杂的智能合约。dYdX 基于 StarkEx 的永续合约交易所成为去中心化衍生品交易的领军项目。

2022-2023 年，StarkNet 主网逐步开放和成熟，推出了代币 STRK。越来越多的项目选择基于 zk-STARK 技术构建，涵盖 DeFi、NFT、游戏等多个领域。

## 相关链接

- [StarkWare 官网](https://starkware.co/)
- [zk-STARK 论文](https://eprint.iacr.org/2018/046)
- [Cairo 编程语言](https://www.cairo-lang.org/)
- [StarkNet 文档](https://docs.starknet.io/)

## 相关协议

- **zk-SNARK**：需要可信设置的零知识证明方案
- **FRI**：zk-STARK 的核心技术协议
- **Cairo**：用于编写 STARK 证明的编程语言
- **StarkNet**：基于 zk-STARK 的以太坊 Layer2
- **StarkEx**：专用的 zk-STARK 扩容引擎
- **Bulletproofs**：另一种无需可信设置的证明方案
