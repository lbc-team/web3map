# Monero (门罗币)

Monero (XMR) 是一个创建于 2014 年的开源加密货币，专注于隐私、去中心化和可互换性。与比特币不同，Monero 的区块链是默认模糊化的，交易的发送方、接收方和金额均被加密隐藏，使其成为目前公认的最具隐私性的加密货币之一。

## 要解决的问题

虽然比特币常被误认为是匿名的，但实际上它是伪匿名（Pseudonymous）的。比特币区块链上的交易历史完全公开，通过链上分析，地址可以与现实世界的身份（通过交易所 KYC 等）关联起来。

Monero 旨在解决以下核心问题：
1.  **交易可追踪性**：防止第三方（政府、分析公司、犯罪分子）追踪资金流向。
2.  **资产可互换性（Fungibility）**：在比特币中，如果某些币曾涉及非法活动（“脏币”），它们可能会被交易所拒收，导致不同比特币的价值实质上不相等。Monero 由于无法追踪历史，所有代币都是完全平等的，确保了货币的可互换性。

## 实现机制与原理

Monero 并未采用单一的隐私技术，而是结合了多种密码学协议来分别保护交易的不同部分。

### 环签名 (Ring Signatures) - 保护发送方
环签名允许发送者将其公钥与其他用户的公钥（“诱饵”）混合在一起进行签名。对于外部观察者来说，交易看起来可能由组内任何一个成员发起，无法确定具体的签署者。这有效地隐藏了**发送方**的真实身份。目前 Monero 使用的是 CLSAG（Compact Linkable Spontaneous Anonymous Group）签名方案，优化了大小和验证速度。

### 隐身地址 (Stealth Addresses) - 保护接收方
对于每一笔交易，发送者的钱包会自动为接收者生成一个一次性的随机地址（隐身地址）。区块链上记录的是这个一次性地址，而非接收者的真实主地址。只有拥有接收方私钥（View Key 和 Spend Key）的人才能扫描区块链，识别出哪些交易是发给自己的。这隐藏了**接收方**的身份。

### 环形机密交易 (RingCT) - 保护金额
Ring Confidential Transactions (RingCT) 于 2017 年引入，用于隐藏交易金额。它利用 Pederson 承诺（Pederson Commitments）和范围证明（Range Proofs，现升级为 Bulletproofs），在数学上证明“输入金额等于输出金额”，而不泄露具体的数值。

### 随机X (RandomX) 共识算法
为了抗衡 ASIC 矿机导致的算力中心化，Monero 定期升级其 PoW 算法，最终采用了 RandomX。这是一种针对通用 CPU 优化的算法，使得消费级 CPU 在挖矿效率上优于 GPU 和 ASIC，极大地增强了网络的去中心化程度。

## 主要特点

*   **默认隐私**：隐私功能是强制性的，不是可选项。这确保了整个匿名集（Anonymity Set）足够大，最大化隐私保护效果。
*   **动态区块大小**：Monero 没有固定的区块大小限制，而是根据网络交易量动态调整，这有助于在高负载下保持低费率。
*   **抗审查性**：由于无法区分交易类型和参与者，网络无法针对特定用户或资金进行审查或黑名单拦截。
*   **尾部发行 (Tail Emission)**：为了保障网络长期的安全性，Monero 在主发行阶段结束后，会保持每分钟 0.6 XMR 的固定微量发行，以此激励矿工持续维护网络。

## 推荐阅读

*   [Monero Whitepaper (CryptoNote v 2.0)](https://cryptonote.org/whitepaper.pdf)
*   [Zero to Monero: A Technical Guide](https://www.getmonero.org/library/Zero-to-Monero-2-0-0.pdf)
*   [Mastering Monero](https://masteringmonero.com/)

## 相关概念

*   **CryptoNote 协议**
*   **Bulletproofs (子弹证明)**
*   **View Key (查看密钥)**
*   **ASIC 抗性**
