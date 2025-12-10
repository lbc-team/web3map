# zk-proofs（零知识证明）

## 概念简介

零知识证明（Zero-Knowledge Proofs, ZKP）使一方能够向另一方证明声明是真实的，而无需透露任何其他信息。[ZKP](https://learnblockchain.cn/tags/zkp) 既有利于增加隐私——因为它们减少了各方之间共享的信息量——也有利于可扩展性，因为它只需要证明而非整个数据集被验证。

零知识证明起源于 Goldwasser、Micali 和 Rackoff 1985 年的论文《The knowledge complexity of interactive proof systems》，引入了完备性、可靠性和零知识性的概念。

## 核心特性

**三大特性：**
1. **完备性（Completeness）**：如果声明为真，诚实的验证者会被诚实的证明者说服
2. **可靠性（Soundness）**：如果声明为假，没有欺骗性的证明者可以说服诚实的验证者
3. **零知识性（Zero-Knowledge）**：如果声明为真，验证者除了声明为真之外不会学到任何其他信息

## 主要类型

**交互式 vs 非交互式：**
- **交互式零知识证明**：证明者和验证者需要交互式的多次通信才能生成一个 proof 用于验证
- **非交互式[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)（NIZK）**：证明者直接发送一个 proof，验证者可以直接验证正确性

**交互式证明的局限：**
- 只能取信于一个验证者，而 NIZK 可以取信于多个验证者，以至所有人
- 只能在交互的那个时刻有效，而 NIZK 将始终有效

## 应用场景

1. **隐私保护**：在区块链交易中隐藏交易金额和参与方身份
2. **身份验证**：证明身份而不泄露个人信息
3. **可扩展性**：Layer 2 方案通过[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)压缩链上数据
4. **合规性**：在保护隐私的同时满足监管要求

## 推荐阅读

- [理解 zk-SNARKs 和 zk-STARKS 的区别](https://blog.chain.link/zk-snarks-vs-zk-starks-zh/)
- [零知识证明之争：STARK还是SNARK？- CSDN](https://blog.csdn.net/Galaxytraveller/article/details/133845919)
- [理解零知识证明算法之 Zk-stark - 登链社区](https://learnblockchain.cn/article/269)

## 相关概念

- **[zkSNARK](https://learnblockchain.cn/tags/zkSNARK)**
- **[zkSTARK](https://learnblockchain.cn/tags/zkSTARK)**
- **交互式证明**
- **非交互式证明**
- **Fiat-Shamir 变换**
