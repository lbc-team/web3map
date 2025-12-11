# Uniswap

## 概念简介

Uniswap 是建立在以太坊区块链上的去中心化交易协议（[DEX](https://learnblockchain.cn/tags/DEX?map=EVM)），它采用自动做市商（AMM）模型，允许用户在无需中心化中介的情况下交易 ERC-20 代币。作为 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM)（去中心化金融）领域的基石协议之一，Uniswap 解决了传统订单簿交易所在区块链上因性能限制而面临的流动性不足和交易成本高昂的问题。

Uniswap 由 Hayden Adams 于 2018 年创立，深受[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)创始人 [Vitalik](https://learnblockchain.cn/tags/Vitalik?map=EVM) Buterin 关于链上自动做市商文章的启发。它不仅为用户提供了无需许可的代币兑换服务，还允许任何人通过提供流动性来赚取交易手续费。

截至 2024 年，Uniswap 已历经多个版本的迭代（V1、V2、V3 及即将到来的 V4），累计交易量超过数万亿美元，是目前[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)生态乃至整个加密货币市场中交易量最大、流动性最深的去中心化交易所之一。

## 核心机制与原理

### 自动做市商 (AMM)

Uniswap 摒弃了传统金融市场的买卖订单簿模式，转而采用流动性池（Liquidity Pools）和恒定乘积公式来确定价格。

核心公式为：$x * y = k$

其中：
- $x$ 是流动性池中代币 A 的数量
- $y$ 是流动性池中代币 B 的数量
- $k$ 是一个在交易发生时保持不变的常数（忽略手续费影响）

当用户卖出代币 A 换取代币 B 时，池中的 $x$ 增加，$y$ 必须减少以保持 $k$ 不变，从而推高代币 A 对代币 B 的相对价格。这种机制确保持续的流动性，只要池中有资产，交易就可以执行。

### 流动性提供

任何人都可以将等价值的两种代币存入 Uniswap 的流动性池，成为流动性提供者（LP）。作为回报，LP 会获得代表其在池中份额的流动性代币（LP Tokens），并按比例分得该池产生的交易手续费。

## 主要版本与特点

### Uniswap V1 (2018年11月)
- **机制**：最初版本，仅支持 ETH 与 ERC-20 代币之间的交易。
- **局限**：如果想交易两种 ERC-20 代币（如 DAI 换 USDC），必须先将 DAI 换成 ETH，再将 ETH 换成 USDC，导致双重滑点和高手续费。

### Uniswap V2 (2020年5月)
- **ERC-20 对 ERC-20 交易**：允许创建任意两个 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 代币之间的直接流动性池，消除了对 ETH 的依赖，减少了滑点。
- **价格[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA)**：引入了时间加权平均价格（TWAP）机制，为其他 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议提供难以被操纵的链上价格数据。
- **闪电互换 (Flash Swaps)**：允许用户在支付之前借入代币，只要在同一笔交易结束前归还并支付费用，常用于套利。

### Uniswap V3 (2021年5月)
- **集中流动性 (Concentrated Liquidity)**：这是 V3 的核心创新。LP 不再需要在 $0$ 到 $\infty$ 的整个价格区间提供流动性，而是可以选择特定的价格区间（例如 ETH/USDC 在 1500-2500 之间）提供资金。这极大地提高了资本效率，LP 可以用更少的资金赚取更多的手续费，但也增加了无常损失的风险和管理的复杂度。
- **多级费率**：提供 0.05%、0.30%、1.00% 等不同费率层级，以适应不同波动率的资产（如稳定币对、主流币对、长尾资产）。
- **NFT LP 代币**：由于每个 LP 选择的价格区间不同，流动性仓位不再是同质化的 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 代币，而是以 [NFT](https://learnblockchain.cn/tags/NFT) ([ERC-721](https://learnblockchain.cn/tags/ERC721?map=EVM)) 的形式表示。

### Uniswap V4  
- **Hooks**：允许开发者在流动性池生命周期的特定点（如交易前、交易后、添加流动性前等）插入自定义逻辑。这使得限价单、动态费用、TWAMM（时间加权平均做市商）等功能可以在池级别实现。
- **Singleton (单例合约)**：所有流动性池将存在于一个单一的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)中，而不是像以前那样为每个池部署新合约。这将大幅降低创建池和多跳交易的 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本。

### UniswapX
- **聚合与荷兰式拍卖**：一种基于意图（Intent-based）的交易协议，将路由复杂性外包给第三方填充者（Fillers）。Fillers 相互竞争以提供最佳价格，涵盖了 Uniswap 协议的流动性以及其他 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 的流动性。它还实现了无 Gas 交易（由 Filler 支付 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM)）和 MEV 保护。

## 治理代币 (UNI)

2020 年 9 月，Uniswap 推出了治理代币 UNI，并对早期用户进行了空投。UNI 持有者拥有协议的治理权，可以投票决定：
- 协议的资金库（Community Treasury）分配。
- 协议费用开关（Fee Switch）：社区可以投票决定是否开启协议层面的收费（例如从 LP 收入中抽取 10%-25% 归协议所有）。
- uniswap.eth 域名的管理等。

## 相关概念

- **AMM (自动做市商)**：[Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM) 所采用的交易模型。
- **无常损失 (Impermanent Loss)**：LP 在提供流动性时，相对于直接持有资产所面临的潜在价值损失，通常发生在资产价格剧烈波动时。
- **滑点 (Slippage)**：交易预期价格与实际执行价格之间的差异。
- **TWAP (时间加权平均价格)**：[Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM) 提供的链上价格[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA)机制。

## 推荐阅读

- [Uniswap V2 白皮书](https://uniswap.org/whitepaper.pdf)
- [Uniswap V3 白皮书](https://uniswap.org/whitepaper-v3.pdf)
- [Uniswap V4 核心理念介绍](https://blog.uniswap.org/uniswap-v4)
- [Hayden Adams: A short history of Uniswap](https://uniswap.org/blog/uniswap-history)