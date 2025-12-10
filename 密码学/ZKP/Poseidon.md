# Poseidon

## 概念简介

Poseidon 是一种专门为[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)系统设计的哈希函数。相比传统的 SHA-256、SHA-3 以及 Pedersen 哈希函数，它为 ZK 证明系统中使用的有限域量身定制，旨在最小化电路的大小，从而最小化证明者和验证者的复杂性。

Poseidon 基于 HADES 策略，减少了每个消息位的约束数，提升了 SNARKs、STARKs 和 Bulletproofs 等证明系统的性能。

## 为什么 Poseidon 适合 [ZKP](https://learnblockchain.cn/tags/zkp)？

**降低计算复杂度**：Poseidon 能够显著地降低证明生成和验证的计算复杂度，极大地提升[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)系统整体的运行效率。

**SNARK 友好设计**：适合 SNARK 的哈希算法被称为 SFH (SNARK-friendly hash)，SFH 是专门为 SNARK 而设计的哈希算法，比传统哈希算法拥有更低的乘法复杂度。常见的 SFH 有 MiMC/Poseidon 等。

**效率提升**：SHA256 哈希函数是一个典型的 snark 不友好哈希。而 Poseidon 哈希函数专门设计用于 zkp，这些在 zkp 中更容易实现，并且效率可以提高 100 倍或更多。

## 技术特点

**代数电路优化**：Poseidon 是一系列哈希函数，其设计目的是作为代数电路非常高效。

**有限域运算**：Poseidon 在有限域上进行运算，这与 [zk-SNARK](https://learnblockchain.cn/tags/zkSNARK) 证明系统的算术电路天然契合。

## 应用案例

基于上述优点，Poseidon 目前已被广泛应用在了各种区块链项目当中，包括：

1. **[Filecoin](https://learnblockchain.cn/tags/Filecoin)**：去中心化存储系统
2. **Mina Protocol**：简洁区块链
3. **Dusk Network**：隐私保护[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)平台
4. **StarkNet**：基于 [zk-STARK](https://learnblockchain.cn/tags/zkSTARK) 的 Layer 2

## 推荐阅读

- [POSEIDON: A New Hash Function for Zero-Knowledge Proof Systems - CSDN](https://blog.csdn.net/mutourend/article/details/121796969)
- [Poseidon哈希为什么适合做ZKP - CSDN](https://blog.csdn.net/wcc19840827/article/details/145331467)
- [zkSNARK实践（三）—— 哈希函数的证明 - 登链社区](https://learnblockchain.cn/article/3260)

## 相关概念

- **[zk-SNARK](https://learnblockchain.cn/tags/zkSNARK)**
- **SNARK-friendly hash**
- **MiMC**
- **有限域**
- **代数电路**
