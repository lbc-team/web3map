# Bulletproofs

## 概念简介

Bulletproofs 是一种简洁的非交互式零知识证明技术，由 Benedikt Bünz、Jonathan Bootle 等密码学家于 2017 年提出。该协议的核心优势是无需可信设置（Trusted Setup）即可生成简洁证明，同时证明体积呈对数级增长。Bulletproofs 特别擅长处理范围证明（Range Proof），可以证明某个数值在特定范围内而不泄露具体数值。

与 zk-SNARK 相比，Bulletproofs 最大的优势是无需可信设置，消除了"有毒废料"的风险；与 zk-STARK 相比，Bulletproofs 的证明体积更小。尽管 Bulletproofs 的验证时间略长于 zk-SNARK，但其在无需可信设置的前提下提供了较好的性能平衡，使其成为隐私加密货币和机密资产场景的理想选择。该协议在 Monero、Grin、Beam 等隐私加密货币中得到广泛应用。

## 核心特性

**无需可信设置**

Bulletproofs 最显著的优势是不需要可信设置阶段，所有公共参数都可以透明生成。这消除了秘密随机数泄露的风险，使得系统更加安全和可审计。相比需要复杂多方计算仪式的 zk-SNARK 方案，Bulletproofs 的部署更加简单直接，降低了实施难度和安全假设。

**对数级证明体积**

Bulletproofs 的证明大小呈对数级增长 O(log n)，其中 n 为被证明的陈述数量。对于范围证明，证明体积约为 2log₂(n) + 9 个椭圆曲线元素，在实践中约为 600-700 字节。虽然比 zk-STARK 的证明小得多，但比 zk-SNARK 略大，不过考虑到无需可信设置的优势，这种体积增加是可接受的权衡。

**证明聚合**

Bulletproofs 支持多个证明的聚合：可以将 m 个独立的 n 位范围证明聚合成单一证明，聚合后的证明大小仅为 O(log(mn))。这种聚合特性在需要批量验证的场景中非常有用，如区块链中验证多笔交易的范围约束，可以显著减少存储和带宽需求。

**验证效率权衡**

Bulletproofs 的验证时间复杂度为 O(n)，相对线性增长。虽然不如 zk-SNARK 的常数时间验证快，但在实际应用中仍然高效。对于范围证明等常见场景，验证时间在可接受范围内。这种性能特性使得 Bulletproofs 适合区块链等需要多次验证的场景，尽管单次验证略慢，但无需可信设置的优势弥补了这一不足。

## 技术原理

Bulletproofs 基于 Pedersen 承诺和内积论证（Inner Product Argument）技术。核心思路是将范围证明问题转化为多项式内积关系的证明，然后通过递归折叠技术将证明大小降低到对数级。

对于范围证明，Bulletproofs 首先将数值分解为二进制位表示，然后使用 Pedersen 承诺隐藏这些位，并通过零知识证明每个位确实是 0 或 1。通过巧妙的数学技巧，协议将多个位的约束合并，避免了线性级的证明膨胀。

聚合证明技术利用了多个独立陈述的共同结构，通过随机线性组合将它们合并，从而大幅降低证明大小。

## 应用场景

**隐私加密货币**

Bulletproofs 首先在 Monero、Grin、Beam 等隐私加密货币中得到应用。在保密交易中，Bulletproofs 用于证明交易金额为正数且在合理范围内，防止通货膨胀攻击，同时不泄露具体金额。Monero 采用 Bulletproofs 后，交易体积减少了约 80%，大大降低了存储和带宽成本。

**机密资产**

在区块链上进行资产代币化时，Bulletproofs 可以实现金额隐藏的同时保证交易有效性。企业和机构可以在公链上进行保密交易，保护商业机密。用户可以证明拥有足够余额而不透露具体资产规模。

**审计与合规**

Bulletproofs 可以用于机密审计场景，在保护隐私的同时证明合规性。例如，企业可以向监管机构证明财务数据满足某些条件（如总资产超过门槛、负债率低于上限）而不公开完整财务信息。这种选择性披露机制平衡了隐私保护和监管需求。

**智能合约隐私**

Bulletproofs 可以集成到智能合约中，实现保密计算和隐私状态更新。例如，在拍卖或投票系统中，可以证明出价或选票有效而不泄露具体内容。在 DeFi 协议中，可以实现保密的抵押和借贷，保护用户的财务隐私。

## 发展历程

2017 年，Benedikt Bünz 等人在学术论文中首次提出 Bulletproofs 协议，展示了无需可信设置的简洁范围证明方案，引起了密码学和区块链社区的广泛关注。

2018 年，Monero 正式将 Bulletproofs 集成到主网，替代了之前的 Borromean 环签名范围证明。这次升级使 Monero 交易体积减少了约 80%，区块链增长速度大幅降低，改善了可扩展性。Monero 的成功应用证明了 Bulletproofs 在生产环境中的可行性。

2019-2020 年，Grin、Beam 等基于 Mimblewimble 协议的隐私加密货币采用了 Bulletproofs。研究社区继续改进 Bulletproofs+等变体，进一步优化性能和减小证明体积。一些 Layer2 方案也开始探索 Bulletproofs 的应用。

2021 年至今，随着零知识证明技术的广泛应用和隐私保护需求的增长，Bulletproofs 仍然是无需可信设置的主流方案之一，在多个项目中持续发挥作用。

## 相关链接

- [Bulletproofs 论文](https://eprint.iacr.org/2017/1066)
- [Monero Bulletproofs 公告](https://www.getmonero.org/2018/10/11/monero-0.13.0-released.html)
- [Bulletproofs 代码库](https://github.com/dalek-cryptography/bulletproofs)
- [范围证明详解](https://cathieyun.medium.com/building-on-bulletproofs-2faa58af0ba8)

## 相关协议

- **zk-SNARK**：需要可信设置的零知识证明方案
- **zk-STARK**：另一种无需可信设置的证明协议
- **Pedersen 承诺**：Bulletproofs 使用的密码学原语
- **Monero**：最早采用 Bulletproofs 的隐私加密货币
- **Mimblewimble**：采用 Bulletproofs 的隐私区块链协议
- **Grin/Beam**：基于 Mimblewimble 的隐私加密货币项目
