# Lido

## 概念简介

Lido 是以太坊上规模最大、最具影响力的流动性质押（Liquid Staking）协议。它旨在解决以太坊 2.0 信标链（Beacon Chain）质押的流动性不足问题。在以太坊上海升级之前，质押的 ETH 无法提取；即使在开放提取后，直接运行验证节点仍需锁定 32 ETH 并具备技术运维能力。

Lido 允许用户质押任意数量的 ETH，并获得 1:1 对应的 stETH 代币。stETH 可以在 DeFi 市场中自由流通、交易、作为抵押品，从而释放了质押资产的流动性，同时让用户享受质押带来的层级收益。

## 核心机制与原理

### 1. stETH (Lido Staked ETH)
- **Rebase 机制**：stETH 是一种 Rebase 代币。随着以太坊验证者获得质押奖励，stETH 的总供应量会每天自动调整（增加），用户的[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)余额也会相应增加。这意味着 1 stETH 的价格理论上应始终锚定 1 ETH。
- **wstETH (Wrapped stETH)**：为了兼容某些不支持 Rebase 机制的 DeFi 协议（如 [Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM), MakerDAO），Lido 提供了封装版本的 wstETH。wstETH 的余额不变，但其对 stETH 的兑换率会随时间增长（价值累积型）。

### 2. 节点运营商 (Node Operators)
Lido 并不直接运行所有验证节点，而是作为一个 DAO 将用户的 ETH 分配给一组经过筛选的专业节点运营商。
- **DAO 治理**：Lido DAO 通过投票决定哪些运营商可以加入白名单。这些运营商通常是知名的质押服务商（如 P2P.org, Stakefish）。
- **费用分配**：质押奖励的 10% 被 Lido 协议收取，其中一半归节点运营商，一半归 Lido DAO 国库（用于保险、开发等），剩余 90% 发放给 stETH 持有者。

### 3. 提款与缓冲
在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)上海升级后，Lido 支持 ETH 赎回。协议维护一个提款缓冲区，通过用户新存入的 ETH 和部分奖励来满足提款需求，若缓冲区不足则启动验证者退出流程。

## 主要特点

- **极佳的流动性**：stETH 是 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 中流动性最好的质押资产，在 [Curve](https://learnblockchain.cn/tags/Curve?map=EVM) 等 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 上拥有深厚的 stETH/ETH 池，几乎可以无损退出。
- **[DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 乐高基石**：stETH 被广泛接受为 Aave 的抵押品、MakerDAO 的铸币资产等，极大地提高了 ETH 的资本效率。
- **简单易用**：用户一键质押，无需维护硬件。

## 争议与挑战

- **中心化风险**：Lido 占据了[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)质押市场极高的份额（曾超过 30%），引发了社区对于网络中心化和审查风险的担忧。[Lido](https://learnblockchain.cn/tags/Lido?map=EVM) 正在通过引入 DVT（分布式验证技术）和模块化节点运营商集合（Staking Router）来试图缓解这一问题。
- **治理攻击**：如果 LDO 代币的持有过于集中，治理层可能对协议施加不利影响。

## 相关概念

- **LSD / LST**：流动性质押代币。
- **LDO**：[Lido](https://learnblockchain.cn/tags/Lido?map=EVM) 的治理代币。
- **DVT**：分布式验证技术，旨在将验证者私钥碎片化，降低单点故障和中心化风险。

## 推荐阅读

- [Lido Primer](https://docs.lido.fi/)
- [The Lido DAO Constitution](https://lido.fi/governance)
