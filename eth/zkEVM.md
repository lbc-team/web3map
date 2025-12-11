# zkEVM

zkEVM（Zero-Knowledge Ethereum Virtual Machine）即零知识以太坊虚拟机，是一种旨在以兼容以太坊生态系统的方式执行智能合约，并生成零知识证明（Zero-Knowledge Proofs, ZKPs）来验证计算正确性的虚拟机技术。它是 ZK-Rollup 扩容方案的“圣杯”。

## 要解决的问题

早期的 ZK-Rollup 技术（如 Loopring, zkSync Lite）虽然能通过零知识证明提供极高的安全性和扩容能力，但它们通常不支持通用的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)，或者需要使用特定的语言（如 [Cairo](https://learnblockchain.cn/tags/Cairo?map=Web3)）重新编写代码。

zkEVM 致力于解决以下矛盾：
1.  **扩容需求**：利用 ZK 证明的简洁性（Succinctness），将大量 Layer 2 交易压缩验证，显著降低 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 费并提高 TPS。
2.  **开发者体验**：保持与以太坊主网（Layer 1）的兼容性，使得开发者可以直接部署 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 合约，使用现有的工具（Remix, Hardhat, Metamask），而无需重写代码或学习新语言。

## 实现机制与原理

传统 EVM 在设计时并未考虑生成[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)，其基于堆栈的架构和某些操作码（Opcode）对 ZK 电路非常不友好（生成证明的开销巨大）。zkEVM 的核心挑战在于如何高效地将 EVM 的执行痕迹（Execution Trace）转换为多项式约束系统，进而生成证明。

### 技术路径
根据 [Vitalik](https://learnblockchain.cn/tags/Vitalik?map=EVM) Buterin 的分类，zkEVM 主要分为四种类型：

*   **Type 1（完全等效）**：完全等同于以太坊，不改变任何共识逻辑、哈希算法或状态树结构。它能完美验证以太坊主网区块，但证明生成速度最慢。
*   **Type 2（EVM 等效）**：完全兼容 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 规范，但可能修改内部数据结构（如状态树）以优化 ZK 证明生成。对开发者完全透明，但某些特定应用（依赖历史区块哈希等）可能受影响。
*   **Type 2.5 / Type 3**：为了更快的证明速度，在 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本或特定操作码行为上做出了更多妥协。
*   **Type 4（语言兼容）**：将 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 编译为一种对 ZK 友好的中间语言或自定义字节码。证明生成极快，但可能存在边缘情况下的行为差异。

### 核心组件
1.  **[zkEVM](https://learnblockchain.cn/tags/zkEVM?map=EVM) 电路**：一组复杂的数学约束，用于证明 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 每一步操作（加法、跳转、存储读写）都是正确的。
2.  **证明者（Prover）**：负责运行复杂的计算以生成[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)。
3.  **验证合约**：部署在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)主网上的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)，用于快速验证提交的证明。

## 主要特点

*   **安全性**：不同于 Optimistic [Rollup](https://learnblockchain.cn/tags/Rollup) 依赖博弈论和挑战期（7天），[zkEVM](https://learnblockchain.cn/tags/zkEVM?map=EVM) 依赖数学密码学保证安全性，状态转换一旦在 L1 验证通过即为最终确认。
*   **兼容性**：允许现有的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) [DApp](https://learnblockchain.cn/tags/DApp) 无缝迁移到 Layer 2。
*   **吞吐量**：通过链下计算和链上数据压缩，大幅提升处理能力。

## 推荐阅读

*   [Vitalik Buterin: The different types of ZK-EVMs](https://vitalik.eth.limo/general/2022/08/04/zkevm.html)
*   [Polygon zkEVM Documentation](https://wiki.polygon.technology/docs/zkevm/)
*   [Scroll Architecture Overview](https://docs.scroll.io/en/technology/)

## 相关概念

*   **ZK-[Rollup](https://learnblockchain.cn/tags/Rollup)**
*   **SNARKs / STARKs**
*   **电路 (Circuit)**
*   **有效性证明 (Validity Proof)**
