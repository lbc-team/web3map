# Fiat-Shamir 变换

## 概念简介

Fiat-Shamir 变换是密码学中一个非常重要的变换思想，由 Amos Fiat 和 Adi Shamir 在 1986 年提出的方法，用于将交互式的零知识证明协议变成非交互式的协议。这样就通过减少通信步骤而提高了通信的效率。

## 交互式与非交互式的区别

**交互式[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)**：Prover 和 Verifier 需要交互式的多次通信，才能生成一个 proof 用于验证。
- 只能取信于一个验证者
- 只能在交互的那个时刻有效

**非交互式[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)（NIZK）**：Prover 直接发送一个 proof，Verifier 可以直接验证正确性。
- 可以取信于多个验证者，以至所有人
- 将始终有效

## 核心思想

**随机预言机模型**：Fiat-Shamir 的核心思想是用一个安全的哈希函数模拟验证者(Verifier) 的"随机挑战"。该算法允许将交互步骤中随机挑战替换为非交互随机数预言机（Random oracle）。

**哈希函数替代**：利用 hash 函数结果的随机性，我们可以将承诺数据的 hash 计算结果作为随机数列用于生成挑战，这也就是 Fiat-Shamir 变换。

## 技术实现

**转换过程：**
1. 在交互式协议中，Verifier 发送随机挑战给 Prover
2. Fiat-Shamir 变换用哈希函数 H(commitment) 替代这个随机挑战
3. Prover 自己计算挑战值，无需与 Verifier 交互
4. 生成的证明包含承诺和响应，任何人都可以验证

## 应用场景

**区块链和数字签名**：这就非常适合在区块链、数字签名等不适合来回通信的环境中使用。

**zk-SNARK**：许多 [zk-SNARK](https://learnblockchain.cn/tags/zkSNARK) 系统使用 Fiat-Shamir 变换将交互式协议转换为非交互式。

**Schnorr 签名**：Schnorr 签名方案就是 Schnorr 身份识别协议的 Fiat-Shamir 变换。

## 安全性考虑

Fiat-Shamir 变换的安全性依赖于所使用的哈希函数的随机[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA)性质。在实践中，使用密码学安全的哈希函数（如 SHA-256、SHA-3）被认为是安全的。

## 推荐阅读

- [零知识证明之Fiat-Shamir范式 - 知乎](https://zhuanlan.zhihu.com/p/32375374470)
- [亚瑟王的「随机」挑战：从交互到非交互式零知识证明 - SECBIT Blog](https://secbit.io/blog/2019/11/01/from-interactive-zkp-to-non-interactive-zkp/)
- [零知识证明系列（1）：从交互式到非交互式 - 知乎](https://zhuanlan.zhihu.com/p/115422206)
- [区块链中的数学 - sigma协议与Fiat-Shamir变换 - 登链社区](https://learnblockchain.cn/article/2493)

## 相关概念

- **交互式证明**
- **非交互式证明**
- **随机[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA)模型**
- **哈希函数**
- **Schnorr签名**
