# DEX (去中心化交易所)

## 概念简介

DEX（Decentralized Exchange，去中心化交易所）是一种基于区块链智能合约构建的加密货币交易平台。与 CEX（中心化交易所，如 Binance, Coinbase）不同，DEX 不依赖第三方中介来托管用户资金或撮合交易。用户直接通过非托管钱包（如 MetaMask）与链上合约交互，实现点对点的资产兑换。

DEX 是 DeFi（去中心化金融）生态的核心支柱，体现了无需许可（Permissionless）、抗审查（Censorship-resistant）和非托管（Non-custodial）的区块链精神。

## 核心交易模型

DEX 主要采用以下几种交易模型：

### 1. 自动做市商 (AMM)
目前最主流的 DEX 模式。
- **机制**：使用算法定价，通过流动性池（Liquidity Pool）来提供即时交易。用户与智能合约交易，而不是与其他用户交易。
- **公式**：最经典的是 $x \cdot y = k$（恒定乘积公式）。
- **角色**：
    *   **交易者 (Trader)**：支付手续费进行代币兑换。
    *   **流动性提供者 (LP)**：将资产存入池中，赚取交易手续费。
- **代表项目**：Uniswap, Curve, Balancer, PancakeSwap。

### 2. 订单簿 (Order Book)
模仿传统金融市场的模式，维护买单和卖单列表。
- **链上订单簿**：所有订单和撮合都在链上完成，透明度高但受限于区块链 TPS 和 Gas 费（如早期的 EtherDelta，现在的 Solana 上的很多 DEX）。
- **混合/链下订单簿**：订单撮合在链下服务器进行，只有最终结算上链，以提高速度和降低成本（如 dYdX, 0x Protocol）。
- **代表项目**：dYdX (衍生品), Serum (Solana), Loopring。

### 3. 聚合器 (DEX Aggregators)
不拥有自己的流动性，而是从多个 DEX 中搜索最佳价格和路径，帮助用户以最低的滑点完成交易。
- **代表项目**：1inch, ParaSwap, CoW Swap。

## 核心特点

- **非托管 (Non-custodial)**：用户始终掌控自己的私钥和资金，不存在交易所跑路或挪用资金的风险。
- **无需许可 (Permissionless)**：任何人都可以访问，没有 KYC（身份验证）限制；任何人都可以为任何代币创建交易对（在 AMM 模式下）。
- **链上透明**：所有交易记录和流动性数据公开可查。
- **可组合性**：DEX 协议可以被其他 DeFi 应用（如借贷、收益聚合器）集成。

## 面临的挑战

- **无常损失 (Impermanent Loss)**：AMM 模式下的 LP 在代币价格剧烈波动时，相对于单纯持有代币可能遭受的损失。
- **滑点 (Slippage)**：大额交易可能导致成交价格显著偏离市场价格。
- **MEV (最大可提取价值)**：矿工或套利机器人可以通过抢跑（Front-running）或三明治攻击（Sandwich Attack）从普通用户的交易中获利。
- **交易速度与成本**：受限于底层区块链的性能，Layer 1 上的 DEX 可能面临拥堵和高昂的 Gas 费。

## 相关概念

- **流动性挖矿 (Liquidity Mining)**：DEX 协议通过分发治理代币来激励用户提供流动性。
- **TVL (总锁仓价值)**：衡量 DEX 流动性深度的重要指标。

## 推荐阅读

- [Vitalik Buterin: The Path to Better DEXs](https://vitalik.ca/)
- [DeFi 之道: 深入理解 AMM](https://mp.weixin.qq.com/)