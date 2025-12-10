# Pedersen 承诺

## 概念简介

Pedersen 承诺是 1992 年由 Torben Pryds Pedersen 提出的一种密码学承诺方案，主要搭配[椭圆曲线密码学](https://learnblockchain.cn/tags/椭圆曲线密码学)使用，具有基于离散对数困难问题的强绑定性和同态加法特性。

Pedersen 承诺是一个满足完美隐藏、计算绑定的同态承诺协议，其完美隐藏性不依赖于任何困难性假设，计算绑定依赖于离散对数假设。

## 核心公式

**基本公式**：C = r×G + v×H

其中：
- C 为生成的承诺值
- G、H 为特定椭圆曲线上的生成点
- r 代表盲因子（blinding factor）
- v 代表原始信息（要承诺的值）

## 主要特性

**完美隐藏性**：给定承诺 C，在计算上无法推断出原始值 v。完美隐藏性不依赖于任何困难性假设。

**计算绑定性**：一旦创建承诺，证明者在计算上无法找到另一个值 v' 使得承诺值相同。计算绑定依赖于离散对数假设。

**加法同态性**：两个 Pedersen 承诺的和等于明文的和的 Pedersen 承诺。即 C1 + C2 = (r1+r2)×G + (v1+v2)×H，这是 Pedersen 承诺最重要的特性之一。

## 零知识证明应用

Pedersen 承诺常见的形式有两种：
1. **非零知识的 Pedersen 承诺**：不提供零知识性
2. **零知识的 Pedersen 承诺**：结合[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)技术

**与 Bulletproof 结合**：Pedersen 承诺在[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)（如 Bulletproofs）中有重要应用，可以在不泄露交易金额的情况下证明交易的有效性。

## 隐私保护应用

**隐私币**：在区块链技术中，Pedersen 承诺常被用于实现交易的隐私保护，例如在 Monero、Grin 等隐私币中，Pedersen 承诺被用于隐藏交易金额，保护用户隐私。

**保密交易**：目前加密货币的保密交易实现中，主要有零知识简洁无交互证明（[zk-SNARK](https://learnblockchain.cn/tags/zkSNARK)）、零知识可扩展透明证明（[zk-STARK](https://learnblockchain.cn/tags/zkSTARK)）和子弹证明（Bulletproof）等，它们都利用了 Pedersen 承诺的特性。

**范围证明**：配合 Bulletproof 可以证明承诺的值在某个范围内（如交易金额大于 0），而不泄露具体数值。

## 与其他承诺方案对比

| 特性 | Pedersen 承诺 | 哈希承诺 |
|------|--------------|---------|
| 隐藏性 | 完美隐藏 | 计算隐藏 |
| 绑定性 | 计算绑定 | 完美绑定 |
| 同态性 | 支持（加法）| 不支持 |
| 效率 | 需要椭圆曲线运算 | 仅需哈希运算 |

## 推荐阅读

- [浅谈承诺（Commitment）和零知识证明（ZKP）- 博客园](https://www.cnblogs.com/Severus-Cavendish/p/15608374.html)
- [密码学承诺之Pedersen commitment原理及应用 - 知乎](https://zhuanlan.zhihu.com/p/108659500)
- [区块链中的数学 - Pedersen承诺 - 登链社区](https://learnblockchain.cn/article/2096)

## 相关概念

- **[椭圆曲线密码学](https://learnblockchain.cn/tags/椭圆曲线密码学)**
- **离散对数问题**
- **同态加密**
- **Bulletproof**
- **Monero**
- **范围证明**
