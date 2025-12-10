# VRF（可验证随机函数）

## 概念简介

可验证随机函数（Verifiable Random Function, VRF）是一种公钥伪随机函数，它提供了证明其输出被正确计算的凭证。VRF 接受一系列输入，计算它们，并产生一个伪随机输出和可以被任何人验证的真实性证明。

VRF 的概念由 Silvio Micali、Michael Rabin 和 Salil Vadhan 在 1999 年发表的论文中引入。值得注意的是，Silvio Micali 后来推出了 Algorand 区块链，该区块链在其共识机制中使用了 VRF。

## 核心特性

**三个主要特征：**
1. **可验证性**：任何人都可以使用公钥和证明验证输出的正确性
2. **随机性**：输出在计算上与随机值无法区分
3. **确定性**：相同的输入总是产生相同的输出

## 在区块链共识中的应用

**解决共识节点权衡问题**：VRF 用于解决共识节点数量和共识性能之间的权衡问题。尽管共识节点数量越多意味着更高的去中心化程度，但与此同时会导致共识性能的降低。

**随机节点选择**：可验证随机函数用于区块链中完成出块节点的随机选择。使用 VRF 的方式，矿工只需要公布自己的 R 表明自己的出块权，当出完块的时候再公布 P，那么攻击者就无法在出块之前知道谁具有出块权，因此也就无法实施针对性的攻击。

**VRF 与二项分布结合**：在选举共识节点时通过使用二项分布根据每个共识候选节点的权重计算出每个候选节点的概率，VRF 和二项分布结合来执行。

## 业界应用案例

**Algorand 算法**：VRF 算法作为一种基于密码学的新型共识模型被提出，最大的优势是快速共识、抗攻击能力、极低算力需求（较高的经济性）。业界已问世的解决方案有图灵奖得主 Micali 提出的 Algorand 算法和 DFINITY 中基于 BLS 的算法。

**[Chainlink](https://learnblockchain.cn/tags/Chainlink) VRF**：提供可验证的随机性服务，用于[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)中需要不可预测且防篡改的随机数场景。

## 技术优势

- **防止攻击**：攻击者无法提前知道哪个节点拥有出块权，无法进行针对性攻击
- **高效共识**：快速达成共识，无需大量计算
- **公平性**：基于密码学保证的随机性确保选择过程公平

## 推荐阅读

- [密码学小知识(8)：可验证随机函数 - CSDN](https://blog.csdn.net/A33280000f/article/details/124316216)
- [VRF在区块链中的应用 - 博客园](https://www.cnblogs.com/informatics/p/9721295.html)
- [可验证随机函数（VRF）应用于区块链共识 - 知乎](https://zhuanlan.zhihu.com/p/356585833)
- [Verifiable Random Function (VRF) - Chainlink](https://chain.link/education-hub/verifiable-random-function-vrf)

## 相关概念

- **Algorand**
- **区块链共识**
- **随机数生成**
- **抗攻击性**
- **[Chainlink](https://learnblockchain.cn/tags/Chainlink)**
