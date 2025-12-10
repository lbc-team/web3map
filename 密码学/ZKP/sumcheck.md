# sumcheck 协议

## 概念简介

Sumcheck 协议是一种交互式证明系统，由 Lund、Fortnow、Karloff 和 Nisan 在 1992 年的论文《Algebraic Methods for Interactive Proof Systems》中提出。

Sumcheck 协议允许证明者向验证者证明关于多项式的性质，例如多项式在某个域上的和，广泛应用于基于 PCP 的零知识证明系统中。

## 核心思想

**多项式求和验证**：给定一个 d 变量的多项式 f(x₁, x₂, ..., xₐ) 和一个有限域 F，证明者想要向验证者证明：

∑(x₁,x₂,...,xₐ ∈ F) f(x₁, x₂, ..., xₐ) = H

其中 H 是声称的和。

**交互式验证**：协议使用证明者和验证者之间的交互验证逐步验证计算的每一部分，在保持零知识特性的同时，验证者可以确信结果是正确的，而无需获取关于多项式的完整信息。

## 协议流程

**基本步骤：**
1. **第一轮**：证明者发送关于第一个变量的单变量多项式 g₁(X₁)
2. **验证**：验证者检查 ∑g₁(x) = H
3. **随机挑战**：验证者选择随机点 r₁
4. **迭代**：对剩余变量重复此过程
5. **最终验证**：在所有随机点上评估原始多项式

**复杂度**：
- **通信复杂度**：O(d·deg) 个域元素，其中 d 是变量数，deg 是每个变量的度数
- **证明者复杂度**：多项式时间
- **验证者复杂度**：多项式时间

## 在零知识证明中的应用

**SNARK 构造**：在 SNARK 构造范式中，首先定义一个功能承诺方案，然后构造一个兼容的 IOP（Interactive Oracle Proof），通过 Fiat-Shamir 变换等非交互技术可以转换为 SNARK。

**Spartan**：Spartan 为使用 R1CS 描述的电路提供 IOP，利用多变量多项式的性质和 sumcheck 协议，使用适当的多项式承诺方案产生透明的 SNARK，证明时间为线性。

**GKR 协议**：GKR（Goldwasser-Kalai-Rothblum）协议在 2007 年提出，是构建现代 SNARKs 的重要基础，广泛使用 sumcheck 协议。

## 历史发展

**早期发展**：零知识证明起源于 Goldwasser、Micali 和 Rackoff 1985 年的论文。一些构建现代 SNARKs 的关键思想和协议在 1990 年代被提出（sumcheck 协议），甚至在[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)出现之前（GKR 在 2007 年）。

**现代应用**：Sumcheck 协议已经成为构建高效[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)系统的标准工具之一，特别是在需要验证复杂计算的场景中。

## 优化和变体

**多项式承诺**：结合不同的多项式承诺方案（如 KZG、FRI）可以构建不同特性的证明系统。

**递归组合**：Sumcheck 可以与递归证明技术结合，实现更复杂的证明组合。

**并行化**：某些 sumcheck 的实现可以并行化，提高证明生成效率。

## 实际意义

Sumcheck 协议作为一个基础构建块，在现代[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)技术栈中扮演着关键角色，是理解和构建高效 SNARK 系统的重要工具。

## 推荐阅读

- [SNARKs：从理论到实践 - CSDN](https://blog.csdn.net/mutourend/article/details/136146403)
- [【证明、论证与零知识】第十章 交互式谕示证明(IOP) - 知乎](https://zhuanlan.zhihu.com/p/633828733)
- [2024年零知识证明(ZK)研究进展 - CSDN](https://blog.csdn.net/wcc19840827/article/details/146658208)

## 相关概念

- **交互式证明**
- **多项式承诺**
- **GKR协议**
- **Spartan**
- **IOP**
