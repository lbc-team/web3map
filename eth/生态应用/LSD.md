# LSD (流动性质押衍生品)

## 概念简介

LSD（Liquid Staking Derivatives），现更常被称为 **LST**（Liquid Staking Tokens，流动性质押代币），是指在 [PoS](https://learnblockchain.cn/tags/PoS)（权益证明）区块链上，用户将原生代币（如 ETH）质押给协议后，获得的代表其质押份额及未来收益的凭证代币。

LSD 的出现解决了 [PoS](https://learnblockchain.cn/tags/PoS) 机制中**资本效率**与**网络安全**之间的核心矛盾。在传统的质押模式下，资产被锁定以维护网络安全，期间无法流通或使用；LSD 协议允许用户在获得质押奖励的同时，保留资产的流动性，使其能够继续参与 DeFi 活动（如借贷、做市）。

## 核心价值

### 1. 释放流动性
用户不再面临质押锁定期带来的机会成本。持有的 stETH 或 rETH 可以像原生 ETH 一样在市场上随时出售，或者作为抵押品借出稳定币，极大地提高了资本效率。

### 2. 降低参与门槛
[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)原生的 Solo Staking 需要 32 ETH 和复杂的硬件运维。LSD 协议通常允许用户以任意小额资金参与，且无需管理节点。

### 3. 提高网络安全性
通过降低门槛和提供流动性，LSD 吸引了更多本不愿锁定资金的用户参与质押，从宏观上增加了网络中质押代币的总量，提升了攻击网络的成本。

## 主要机制类型

### 1. Rebase 模型 (如 [Lido](https://learnblockchain.cn/tags/Lido?map=EVM) stETH)
- **机制**：代币余额随质押奖励每日自动增加。
- **汇率**：通常锚定 1:1（1 stETH ≈ 1 ETH）。
- **优缺点**：直观反映收益，但在某些 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议中集成较复杂，涉及税务处理可能较繁琐。

### 2. 增值模型 / 奖励承载代币 (如 Rocket Pool rETH, Compound cToken)
- **机制**：代币数量不变，但其对底层资产的兑换汇率随时间上升。
- **汇率**：1 LSD > 1 ETH，且差价不断扩大。
- **优缺点**：[DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 兼容性极好（作为标准 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM)），被视为资本利得税。

## 衍生生态：LSDFi

LSD 的普及催生了建立在 LSD 之上的金融生态，称为 **LSDFi**。
- **收益聚合与杠杆**：循环借贷（抵押 stETH 借 ETH 买 stETH）以放大质押收益。
- **稳定币抵押**：使用 LSD 作为抵押品铸造去中心化稳定币（如 Lybra, Raft）。
- **[DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 流动性**：为 LSD/ETH 交易对提供流动性。
- **指数产品**：一篮子 LSD 代币组合（如 dsETH）。

## 风险与挑战

- **脱锚风险**：虽然 LSD 代表了底层 ETH，但二级市场价格受供需影响，极端行情下可能出现负溢价（脱锚）。
- **[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)风险**：LSD 协议涉及复杂的合约交互，存在黑客攻击风险。
- **中心化风险**：如果某个 LSD 协议（如 [Lido](https://learnblockchain.cn/tags/Lido?map=EVM)）控制了过高比例的验证节点，可能威胁[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)的抗审查性。
- **罚没风险 (Slashing)**：如果节点运营商作恶或配置错误，质押的 ETH 会被罚没，导致 LSD 价值受损（尽管协议通常有保险机制）。

## 相关概念

- **DVT (分布式验证技术)**：通过分散私钥控制权来降低 LSD 协议中心化风险的技术。
- **Restaking (再质押)**：如 EigenLayer，允许将 LSD 再次质押以维护其他服务的安全。

## 推荐阅读

- [Lido Documentation](https://docs.lido.fi/)
- [Rocket Pool Guides](https://docs.rocketpool.net/)
- [Ethereum.org on Staking](https://ethereum.org/en/staking/)
