## 什么是Rollup？

Rollups是一种 Layer2 的[扩容技术](https://learnblockchain.cn/tags/%E6%89%A9%E5%AE%B9) ，Rollups的扩容原理是将数百个在交易捆绑压缩（Rollup）到一个基础（Layer 1）区块链单个交易中，由所有的 Layer2 交易来分摊 Layer1 单个交易的成本 ，以此来提升交易速度，降低交易手续费。

Rollups主要有两个方案：Op Rollup和 ZK Rollup。



## Op Rollup

Op Rollup全称为Optimistic Rollup，。Optimistic扩容方案是基于“乐观”机制的，系统总是乐观的假设链下交易是有效的，并且不发布推送到链上的交易批次的有效性证明，这是Op Rollup 与 ZK Rollup 的不同。



Op Rollup 依赖于欺诈证明方案来检测交易计算不正确的情况。 在以太坊上提交Rollup批次后，有一个时间窗口（称为挑战期， 通常为 7 天），在此期间任何人都可以通过计算欺诈证明（Fraud proofs）来挑战 Rollup 交易的结果。如果欺诈证明成功，则Rollup协议重新执行交易并相应地更新Rollup链的状态。 成功的欺诈证明的另一个影响是，负责将错误执行的交易纳入区块的排序者会受到惩罚。如果在挑战期过后Rollup批次仍未受到挑战（即所有交易均已正确执行），则将其视为有效并在以太坊上接受。 其他人可以继续扩建未经确认的 Rollup 区块，但需要注意：交易结果如果基于先前发布的错误执行交易，则将被逆转。



典型的 Op Rollup 方案有 **[Arbitrum One](https://learnblockchain.cn/tags/Arbitrum)**和**[Optimism](https://learnblockchain.cn/tags/Optimism)**、[Base](https://learnblockchain.cn/tags/Base) ，后两者基于 [Op Stack](https://learnblockchain.cn/tags/OP%20Stack) 实现。



## ZK Rollup

ZK Rollup ：零知识证明 Rollup， 同样是通过将计算和状态存储转移到链下进行提高了以太坊主网吞吐量。 零知识 Rollup 可以处理一个批次中的数千笔交易，但仅将一部分最少量的摘要数据发布到主网。 这些摘要数据确定了应对以太坊状态进行的变化以及一些证明这些变化正确性的加密证明（有效性证明）。



通过[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)技术可以确认链下状态转换的正确性，而无需在以太坊上重新执行交易。这些证明可以是 [ZK-SNARK](https://learnblockchain.cn/tags/zk-SNARK)（零知识简洁非交互式知识论证）或 [ZK-STARK](https://learnblockchain.cn/tags/zk-STARK)（零知识可扩容透明知识论证）两种形式。 



与乐观 Rollup 不同，零知识Rollup不直接与[以太坊虚拟机 (EVM)](https://ethereum.org/zh/developers/docs/evm/) 兼容。 在线路中证明通用以太坊虚拟机计算比证明简单计算（如前面描述的代币转账），更加困难且更加耗费资源。



典型的 ZK Rollup 方案有：**[Starknet](https://learnblockchain.cn/tags/Starknet)**、**[Polygon zkEVM](https://learnblockchain.cn/tags/Polygon%20zkEVM)**  、**[Scroll](https://learnblockchain.cn/tags/Scroll)**  、**[Taiko](https://taiko.xyz/)** 、**[ZKSync](https://learnblockchain.cn/tags/zkSync)** 、**[Linea](https://learnblockchain.cn/tags/Linea)**

Starknet 通过 ZK-Stark 技术构建一个通用的 [zkVM](https://learnblockchain.cn/tags/zkVM) 虚拟机来实现有效性证明，其他的项目则通过构建以太坊虚拟机兼容 [zkEVM](https://learnblockchain.cn/tags/zkEVM) 。



还有一些解决特定的需求的  ZK Rollup ： [Loopring](https://learnblockchain.cn/tags/Loopring)、[dYdX v3](https://learnblockchain.cn/tags/dydx)



## Op Rollup 与 ZK Rollup 对比

以下是一些不同角度的对比：

**安全性**： 零知识 Rollup 使用智能合约通过 ZK 有效性证明来处理交易完整性的验证，安全性更高，相比之下，乐观Rollup认为交易有效，并依赖于基于惩罚的欺诈系统，同时要求验证者在挑战期内标记潜在的欺诈交易。[l2beat](https://l2beat.com/scaling/summary) 从安全角度对各个 Rollup 有跟详细的对比。

 **交易确定性**： Optimistic Rollups 的挑战期最长为 7 天。因此，理论上这些交易直到此时才主网络确定。另一方面，ZK rollups 上的交易在主网络上达到最终确定的速度比乐观Rollup更快，因为每个 ZK rollup 批次在主网上的最终确定都是即时的。反应在提现时间也有所不同，将资产从 Optimistic Rollup 网络桥接到主网可能需要长达 7 天的时间。同时，ZK Rollup 上的提现在交易批次提交到主网并经过验证后即可完成，通常最多需要三个小时。

**复杂度及成本**：由于有效性证明计算的复杂性，ZK-rollup 交易相对较重，成本更高，OP Rollups 的复杂性和交易成本均较低、与 EVM 的兼容性更好。在 https://l2fees.info/ 可以查看layer2 的费用对比。这一点也让OP Rollup 网络 更早推出，成为用户更便宜且相对更具可扩展性的选择。Optimism 的 OP Stack 的推出，也让项目更容易推出自己的Layer 2。



随着 ZK 技术的的发展，ZK Roolup 被认为将在各个方面胜出。









