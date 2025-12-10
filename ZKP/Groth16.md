# Groth16

## 概念简介

Groth16 是由 Jens Groth 在 2016 年提出的算法，目前是一个典型的 [zkSNARK](https://learnblockchain.cn/tags/zkSNARK) 算法，在 ZCash、Filecoin、Coda 等项目中使用。

Groth16 是目前最快的 [zk-SNARK](https://learnblockchain.cn/tags/zkSNARK)，具有最小的数据大小，但每个电路需要单独的 Trusted Setup。

## 核心特性

**极小的证明大小**：该算法有一个独特的特点：证明大小极小，只需要三个群元素（约 200 字节）。这使得 Groth16 非常适合区块链应用，因为链上存储和验证成本很低。

**快速验证**：验证一个 Groth16 证明只需要常数时间，且非常高效。

**固定电路 Trusted Setup**：每个电路需要单独的 Trusted Setup，这是其主要限制。不同的电路不能共享 setup 参数。

## 技术实现

**基于配对的密码学**：Groth16 使用双线性配对（Pairing）技术，通常在 BN254 或 BLS12-381 等椭圆曲线上实现。

**QAP（Quadratic Arithmetic [Program](https://learnblockchain.cn/tags/Program?map=Solana)）**：将计算电路转换为 QAP，然后通过多项式承诺和配对检查来生成和验证证明。

## 在 ZCash 中的应用

**Sapling 升级**：在 Zcash 项目中，libsnark 算法库被最初用来实现 zk-SNARK [零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)。当升级到 Sapling 版本（2018年）时，Zcash 切换到使用自研的 bellman 算法库，这是一个基于 [Rust](https://learnblockchain.cn/tags/Rust) 的 [zk-SNARK](https://learnblockchain.cn/tags/zkSNARK) 库，支持 Groth16 方案。

**Trusted Setup 仪式**：为了防止安全问题，Zcash 通过精心设计的多方仪式生成公共参数。如果 setup 过程中的"有毒废料"没有被正确销毁，可能导致伪造证明。

## 应用场景

1. **隐私保护**：Zcash 使用 Groth16 实现屏蔽交易，隐藏发送者、接收者和金额
2. **去中心化交易所**：Loopring 3.0 使用 Groth16 算法提供[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)
3. **存储证明**：[Filecoin](https://learnblockchain.cn/tags/Filecoin) 使用 [Groth16](https://learnblockchain.cn/tags/Groth16) 证明存储数据的可用性
4. **Layer 2 扩容**：多个 zkRollup 项目采用 [Groth16](https://learnblockchain.cn/tags/Groth16)

## 优势与局限

**优势：**
- 证明极小（~200 bytes）
- 验证极快（~5-10 ms）
- [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本低
- 技术成熟，生产就绪

**局限：**
- 需要电路特定的 Trusted Setup
- Setup 过程复杂且有潜在风险
- 不支持递归证明（需要特殊处理）
- 电路更新需要重新 setup

## 推荐阅读

- [零知识证明（zk-SNARK）- groth16（一）- CSDN](https://blog.csdn.net/qq_43271194/article/details/135273716)
- [零知识证明 - Groth16 算法介绍 - GeekMeta](https://www.geekmeta.com/article/1087527.html)
- [简明理解零知识证明历史、原理与发展现状 - 登链社区](https://learnblockchain.cn/article/2745)

## 相关概念

- **[zkSNARK](https://learnblockchain.cn/tags/zkSNARK)**
- **Trusted Setup**
- **ZCash**
- **[Filecoin](https://learnblockchain.cn/tags/Filecoin)**
- **双线性配对**
- **QAP**
