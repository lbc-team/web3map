# Gas 机制

Gas（燃料）是以太坊网络中用于衡量执行特定操作（如交易转账、[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)计算、存储数据）所需计算工作量的单位。它是以太坊经济模型和安全机制的核心。

## 要解决的问题

作为去中心化的世界计算机，[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)面临两个关键的资源管理问题：

1.  **停机问题（Halting Problem）**：由于 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 是图灵完备的，恶意或错误的代码可能包含无限循环。如果没有终止机制，网络节点将永远陷入死循环，导致网络瘫痪。
2.  **资源滥用（Spam Prevention）**：链上计算和存储资源是有限且昂贵的。如果操作是免费的，攻击者可以毫无成本地向网络发送海量垃圾交易，导致拒绝服务（DoS）。

Gas 机制通过为每个操作定价，强制发送者付费，从而解决了上述问题。

## 实现机制与原理

### Gas 计量
[EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 中的每个操作码（Opcode）都有固定的 Gas 成本（例如，`ADD` 消耗 3 Gas，`SSTORE` 写入存储可能消耗 20000 Gas）。复杂的交易是所有子操作 Gas 消耗的总和。

### EIP-1559 费用模型
自 2021 年伦敦升级（[EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM)）以来，[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)采用了新的费用市场机制：

*   **Gas Limit（Gas 限制）**：用户愿意为一笔交易消耗的最大 Gas 数量，防止合约错误导致资金耗尽。
*   **Base Fee（基础费用）**：协议自动计算的每单位 Gas 最低价格，根据区块拥堵程度动态调整。**这部分费用会被直接销毁（Burn）**。
*   **Priority Fee（优先费/小费）**：用户额外支付给验证者的费用，以激励验证者优先打包该交易。
*   **Max Fee**：用户愿意支付的最高单价（Base Fee + Priority Fee）。

交易总费用 = 实际消耗的 Gas 数量 × (Base Fee + Priority Fee)。

### 失败处理
如果交易执行过程中 Gas 耗尽（Out of Gas），交易会失败并回滚所有状态更改，但**已经消耗的 Gas 费用不会退还**，因为矿工/验证者已经执行了相应的计算工作。

## 主要特点

*   **去中心化计价**：不依赖中心化机构，而是由市场供需和协议算法动态决定资源价格。
*   **通缩机制**：[EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 引入的 Base Fee 销毁机制，使得在网络活跃时，ETH 的销毁量可能超过发行量，从而实现通缩。
*   **细粒度控制**：不同的操作（计算密集型 vs 存储密集型）根据其对节点资源的占用程度有不同的定价。

## 推荐阅读

*   [Ethereum.org: Gas and Fees](https://ethereum.org/en/developers/docs/gas/)
*   [EIP-1559: Fee market change for ETH 1.0 chain](https://learnblockchain.cn/docs/eips/EIPS/eip-1559)
*   [EVM Opcodes Gas Costs](https://www.evm.codes/)

## 相关概念

*   **Gwei**：Gas 价格的常用单位，1 Gwei = $10^{-9}$ ETH。
*   **Gas Limit (Block)**：单个区块允许包含的最大 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 总量，决定了区块的大小上限。
*   **MEV (最大可提取价值)**：验证者通过重新排序交易来获取额外收益，与 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 竞价密切相关。
