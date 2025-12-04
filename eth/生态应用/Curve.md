# Curve Finance

## 概念简介

Curve Finance 是一个基于以太坊的去中心化交易所（DEX），专注于稳定币（如 USDC、DAI、USDT）以及价值锚定资产（如 WBTC/renBTC、ETH/stETH）之间的高效互换。Curve 采用了专门设计的自动做市商（AMM）算法，旨在为同类资产交易提供极低的滑点（Slippage）和低手续费，同时为流动性提供者（LP）提供较低的无常损失风险。

Curve 于 2020 年推出，迅速成为 DeFi 领域的关键基础设施，特别是在稳定币流动性和收益聚合方面占据主导地位。

## 核心机制与原理

### StableSwap 算法

传统的 Uniswap V2 采用恒定乘积公式 $x \cdot y = k$，这在价格波动大的资产间表现良好，但对于应该具有相同价值的资产（如 1 USDC 理论上应等于 1 USDT），该公式会导致不必要的滑点和资金利用率低下。

Curve 创造性地结合了**恒定和公式**（$x+y=k$，零滑点但无法应对流动性枯竭）和**恒定乘积公式**（$x \cdot y = k$，无限流动性但高滑点）。

其核心公式引入了一个放大系数 $A$（Amplification Coefficient）：
- 当资产组合平衡时，曲线表现得像恒定和曲线（平坦），滑点极低。
- 当资产组合极不平衡时，曲线逐渐向恒定乘积曲线过渡，以确保流动性不会枯竭。

这种设计使得 Curve 在价格维持在 1:1 附近时，能够比 Uniswap 提供深得多的流动性和更优的成交价格。

### 治理与 veToken 模型

Curve 引入了 **veCRV**（Vote-Escrowed CRV）模型，这对整个 DeFi 的治理经济学产生了深远影响：

1.  **锁定机制**：用户必须将 CRV 代币锁定在协议中才能获得 veCRV。锁定时间越长（最长 4 年），获得的 veCRV 越多。veCRV 不可转账。
2.  **权益**：
    *   **治理权**：投票决定 Curve 池子的参数。
    *   **收益分成**：获得协议交易手续费的一半（以 3CRV 等形式分发）。
    *   **收益加速 (Boost)**：为自己在 Curve 池中的流动性提供高达 2.5 倍的 CRV 挖矿奖励加速。
3.  **Gauge 权重投票**：veCRV 持有者可以投票决定下一周期的 CRV 增发奖励分配给哪些流动性池。这引发了著名的“Curve War”，各协议（如 Convex, Yearn）争相积累 CRV 以争夺对收益分配的控制权。

## Curve V2 (Tricrypto)

Curve V2 引入了针对非锚定资产（如 ETH/USDT）的自动做市算法。它使用内部预言机（EMA）动态调整价格曲线的形状（重新定锚），将流动性集中在当前市场价格附近。这使得 Curve 能够与 Uniswap V3 竞争通用资产的交易市场。

## 主要特点

- **低滑点**：专为稳定币设计，大额交易磨损极小。
- **低手续费**：通常为 0.04%，低于一般 DEX 的 0.3%。
- **低无常损失**：由于交易资产价格高度相关，LP 面临的无常损失风险显著降低。
- **流动性基础**：是许多 DeFi 协议（如 Yield Aggregators）的底层收益来源。

## 相关概念

- **Curve War**：指各大 DeFi 协议为了争夺 Curve 的治理权（veCRV）和流动性激励而进行的竞争。
- **Convex Finance**：构建在 Curve 之上的协议，旨在优化 CRV 质押收益和简化 veCRV 流程。
- **3pool**：Curve 上最著名的流动性池，由 DAI、USDC、USDT 组成，常被视为 DeFi 流动性的晴雨表。

## 推荐阅读

- [Curve StableSwap Whitepaper](https://curve.fi/files/stableswap-paper.pdf)
- [Curve CryptoSwap (V2) Whitepaper](https://curve.fi/files/crypto-pools-paper.pdf)