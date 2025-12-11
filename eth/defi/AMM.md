# AMM (自动化做市商)

## 概念简介

AMM（Automated Market Maker，自动化做市商）是一种运行在智能合约上的去中心化交易协议，通过数学公式而非传统订单簿来确定资产价格。AMM 是 DeFi 生态系统的核心基础设施，使得任何人都可以无需许可地创建和参与市场做市。

与传统中心化交易所依赖订单簿撮合买卖订单不同,AMM 使用**流动性池**（Liquidity Pool）和**定价算法**来自动执行交易。用户将资产存入流动性池,智能合约根据预设的数学公式计算交易价格,实现了无需信任、抗审查、永续可用的去中心化交易。

AMM 的诞生彻底改变了加密货币交易的范式,使得长尾资产也能获得流动性,降低了做市商的准入门槛,并为 DeFi 的爆发式增长奠定了基础。自 2018 年 Uniswap V1 推出以来,AMM 已成为 DeFi 中交易量最大、应用最广泛的机制之一。

## 核心特性

### 恒定乘积公式 (x * y = k)

**最经典的 AMM 模型**是恒定乘积做市商（Constant Product Market Maker, CPMM）,由 Uniswap 首次普及,公式为:

```
x * y = k
```

- **x**: 流动性池中代币 A 的数量
- **y**: 流动性池中代币 B 的数量
- **k**: 恒定不变量（constant invariant）

**工作原理:**

1. **初始状态**: 假设池中有 100 ETH (x=100) 和 10,000 DAI (y=10,000),则 k = 1,000,000
2. **用户交易**: 用户用 10 ETH 买入 DAI
3. **池状态更新**: 池中现在有 110 ETH (x=110),根据 k 不变,y = 1,000,000 / 110 ≈ 9,091 DAI
4. **用户收到**: 10,000 - 9,091 = 909 DAI (实际还要扣除手续费)
5. **价格变化**: 交易前 1 ETH = 100 DAI,交易后 1 ETH ≈ 82.6 DAI

**关键特性:**

- **无限流动性**: 理论上任何大小的交易都能执行（但会有滑点）
- **价格发现**: 价格由供需自动调整
- **滑点机制**: 交易规模越大（相对于池子规模）,滑点越大,这是供需机制的自然体现

### 流动性池与 LP 代币

**流动性池（Liquidity Pool）:**

- 由流动性提供者（LP）存入的资产对组成
- 通常要求按**当前价格比例**存入两种资产（如 50% ETH + 50% DAI）
- 所有 LP 共享池中资产和交易手续费

**LP 代币（Liquidity Provider Token）:**

- LP 存入资产后获得的权益证明
- 代表 LP 在池中的份额比例
- 可以随时赎回,按比例取回池中资产
- 可在其他 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议中使用（如质押挖矿、借贷抵押）

**示例:**
```
池子初始状态: 100 ETH + 10,000 DAI
Alice 存入: 10 ETH + 1,000 DAI
Alice 获得份额: 10% (10/110)
Alice 可赎回: 池子的 10% (无论池中资产如何变化)
```

### 交易手续费机制

**手续费标准:**

- **Uniswap V2**: 0.3% 交易手续费,全部分配给 LP
- **Uniswap V3**: 0.05% / 0.3% / 1% 三档,根据池子设置
- **Curve**: 0.04% 稳定币池,0.4% 普通池
- **Balancer**: 0.01% - 10% 可自定义

**收益分配:**

- 手续费按 LP 份额比例自动分配
- 复利增长（手续费留在池中,增加 LP 份额价值）
- 赎回时一并收回本金和累积手续费

**收益计算示例:**
```
假设 Alice 拥有 1% 份额的 ETH/DAI 池
每日交易量: $10,000,000
手续费率: 0.3%
Alice 每日收入: $10,000,000 × 0.3% × 1% = $300
年化收益率: $300 × 365 / 投入资金 = APR
```

### 价格滑点与价格影响

**滑点（Slippage）:**

- 预期价格与实际成交价格的差异
- 由交易规模相对于池子大小决定
- 交易越大,滑点越高（非线性增长）

**价格影响计算:**

根据恒定乘积公式:
```
价格影响 = 1 - (k / (x + Δx)) / (y / x)

其中:
- Δx: 输入的代币数量
- x, y: 池中现有代币数量
```

**滑点示例:**
```
池子状态: 100 ETH, 10,000 DAI (k = 1,000,000)
当前价格: 1 ETH = 100 DAI

场景 1: 买入 1 ETH
实际价格: ≈ 101 DAI/ETH
滑点: 1%

场景 2: 买入 10 ETH
实际价格: ≈ 110 DAI/ETH
滑点: 10%

场景 3: 买入 50 ETH
实际价格: ≈ 200 DAI/ETH
滑点: 100%
```

**用户保护:**

- 设置**最大滑点容忍度**（如 0.5%）
- 交易超过容忍度则回滚
- 防止抢跑攻击和价格操纵

## AMM 模型演进

### Uniswap V1 (2018)

**特点:**
- 最简单的恒定乘积 AMM 实现
- 所有交易对必须与 ETH 配对
- 0.3% 固定手续费
- ETH/DAI 需通过 ETH 中转（DAI → ETH → USDC）

**局限:**
- 跳跃交易增加成本和滑点
- 仅支持 ERC-20 代币
- 资本效率低

### Uniswap V2 (2020)

**改进:**
- **ERC-20 / [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 直接交易对**: 无需 ETH 中转
- **价格预言机**: 时间加权平均价格（TWAP）
- **闪电兑换**: 先借后还的原子交易
- **更安全的架构**: Core + Periphery 分离

**影响:**
- 降低交易成本
- 提供可靠的链上价格源
- 启发大量 Fork（Sushiswap、PancakeSwap 等）

### Uniswap V3 (2021)

**革命性创新:**

**1. 集中流动性（Concentrated Liquidity）:**
- LP 可指定价格区间提供流动性
- 资本效率提升 4000 倍（理论值）
- 仅在价格区间内赚取手续费

**示例:**
```
传统 AMM: 在 0 到 ∞ 价格区间提供流动性
V3: 仅在 $1,800 - $2,200 ETH 价格区间提供流动性
结果: 相同资金,手续费收益大幅增加
```

**2. 多级手续费:**
- 0.05%: 稳定币对
- 0.3%: 主流代币对
- 1%: 长尾/高波动代币对

**3. 非同质化 LP ([NFT](https://learnblockchain.cn/tags/NFT)):**
- 每个流动性头寸是独一无二的 [NFT](https://learnblockchain.cn/tags/NFT)
- 记录价格区间、数量等参数
- 不再是简单的 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) LP 代币

**4. 高级预言机:**
- 单次调用获取多个历史价格点
- Gas 效率显著提升

**权衡:**
- 更高的资本效率
- 但增加了 LP 管理复杂度（需主动管理价格区间）

### Uniswap V4 (2024)

**核心创新 - Hooks:**

- **可定制的流动性池**: 开发者可编写 Hook 合约,在池的关键生命周期注入自定义逻辑
- **支持的 Hook 事件**:
  - `beforeInitialize` / `afterInitialize`
  - `beforeAddLiquidity` / `afterAddLiquidity`
  - `beforeRemoveLiquidity` / `afterRemoveLiquidity`
  - `beforeSwap` / `afterSwap`

**应用场景:**
- 动态手续费（根据波动率调整）
- 链上限价单
- TWAMM（时间加权 AMM,大额订单分散执行）
- 与借贷协议集成
- 自动再平衡策略

**Singleton 架构:**
- 所有池在单一合约中
- 大幅降低 Gas 成本（多跳交易尤其明显）
- 简化升级和维护

**原生 ETH 支持:**
- 直接使用 ETH 而非 WETH
- 减少包装/解包装成本

### [Curve](https://learnblockchain.cn/tags/Curve?map=EVM) Finance (2020)

**专注于稳定币交易:**

**StableSwap 不变量:**
```
A * n^n * Σx_i + D = A * D * n^n + D^(n+1) / (n^n * Πx_i)

其中:
- A: 放大系数（Amplification coefficient）
- n: 资产数量
- x_i: 第 i 个资产的数量
- D: 总流动性（invariant）
```

**特点:**
- 在稳定价格附近接近恒定和公式（x + y = k）,滑点极低
- 偏离锚定价格时切换到恒定乘积,保护池子
- 放大系数 A 可调节曲线陡峭度

**优势:**
- 稳定币交易滑点低于 Uniswap 数十倍
- 适合大额稳定币兑换
- 支持多资产池（如 3pool: DAI/USDC/USDT）

**应用:**
- 稳定币兑换
- 锚定资产交易（stETH/ETH、wBTC/renBTC）
- 低滑点大额交易

### Balancer (2020)

**多资产加权池:**

**不变量:**
```
V = Π (B_i / W_i)^W_i

其中:
- B_i: 资产 i 的余额
- W_i: 资产 i 的权重（总和 = 1）
- V: 恒定值
```

**灵活性:**
- 支持 2-8 种资产的池子
- 自定义权重（如 80% WETH + 20% DAI）
- 可变手续费（0.01% - 10%）

**应用场景:**
- 指数基金（如 80/20 池模拟杠杆持仓）
- 减少无常损失（非 50/50 配比）
- 流动性引导池（Liquidity Bootstrapping Pool, LBP）

**LBP（流动性引导池）:**
- 初始高权重（如 95/5）,逐渐调整到目标权重（如 50/50）
- 价格从高到低变化,抑制抢跑
- 项目方公平分发代币的机制

### 其他创新 AMM

**SushiSwap (2020):**
- Uniswap V2 的 Fork
- 引入 $SUSHI 治理代币
- 0.25% 给 LP, 0.05% 回购 SUSHI

**PancakeSwap (2020):**
- BSC 上的 AMM
- 低 Gas 费
- 类似 Uniswap V2

**Bancor V3 (2022):**
- 单边流动性（只需提供一种代币）
- 无常损失保护（持有时间足够长）
- 自动复利

**Maverick Protocol (2023):**
- 动态分布式 AMM
- 流动性自动跟随价格移动
- LP 无需手动管理

**Trader Joe (Avalanche, 2023):**
- Liquidity Book (离散化流动性)
- 类似限价单的流动性分布
- 零滑点交易（在 bin 内）

## 无常损失

### 什么是无常损失

**无常损失（Impermanent Loss, IL）**是 LP 相比单纯持有资产而产生的价值差异,是 AMM 做市的主要风险。

**产生原因:**
- AMM 要求 LP 按比例持有两种资产
- 价格变化时,套利者调整池子比例使其反映市场价格
- LP 被动地"低买高卖"相反资产,错失单边上涨收益

### 计算公式

对于恒定乘积 AMM,无常损失可精确计算:

```
IL = 2 * sqrt(价格比) / (1 + 价格比) - 1

其中:
价格比 = 当前价格 / 初始价格
```

**具体案例:**

**初始状态:**
- 存入 1 ETH + 100 DAI（1 ETH = 100 DAI）
- 总价值 = $200

**场景 1: ETH 价格翻倍（1 ETH = 200 DAI）**

单纯持有:
- 1 ETH + 100 DAI = $300

做 LP:
- 池子重新平衡: 0.707 ETH + 141.4 DAI
- 总价值 = $282.8
- 无常损失 = ($282.8 - $300) / $300 = **-5.7%**

**场景 2: ETH 价格跌一半（1 ETH = 50 DAI）**

单纯持有:
- 1 ETH + 100 DAI = $150

做 LP:
- 池子重新平衡: 1.414 ETH + 70.7 DAI
- 总价值 = $141.4
- 无常损失 = ($141.4 - $150) / $150 = **-5.7%**

**无常损失表:**
| 价格变化 | 无常损失 |
|---------|---------|
| 1.25x   | -0.6%   |
| 1.5x    | -2.0%   |
| 1.75x   | -3.8%   |
| 2x      | -5.7%   |
| 3x      | -13.4%  |
| 4x      | -20.0%  |
| 5x      | -25.5%  |

### 缓解策略

**1. 选择低波动性资产对:**
- 稳定币对（DAI/USDC）
- 锚定资产对（stETH/ETH）
- 相关资产对（WBTC/renBTC）

**2. 手续费覆盖:**
- 高交易量池的手续费可能超过无常损失
- 尤其是稳定币池（高量低波动）

**3. 短期做市:**
- 价格偏离较小时及时退出
- "无常"损失在赎回时才"permanent"

**4. 单边流动性（Bancor）:**
- 只提供一种代币
- 协议承担无常损失风险

**5. 集中流动性（Uniswap V3）:**
- 缩小价格区间,提高手续费收益
- 但价格移出区间后停止赚取手续费

**6. 无常损失保险:**
- Bancor 提供 100 天保护期
- Nexus Mutual 等保险协议

## 应用场景

### 去中心化交易

**核心功能:**
- 点对合约交易,无需对手方
- 7×24 可用
- 无需 KYC
- 抗审查

**优势:**
- 长尾资产也能获得流动性
- 上币无需许可
- 全球统一市场

**主要平台:**
- Ethereum: Uniswap, [Curve](https://learnblockchain.cn/tags/Curve?map=EVM), Balancer
- BSC: PancakeSwap
- Polygon: QuickSwap
- Arbitrum: Camelot
- [Solana](https://learnblockchain.cn/tags/Solana?map=Solana): Raydium, Orca

### 价格预言机

**TWAP（时间加权平均价格）:**

Uniswap V2/V3 提供抗操纵的链上价格:

```
TWAP = Σ (价格_i × 时间_i) / 总时间
```

**特点:**
- 操纵成本高昂（需持续大额交易）
- 延迟价格更新（平滑短期波动）
- 无需信任的价格源

**应用:**
- 借贷协议（Compound、Aave）
- 合成资产（Synthetix）
- 期权协议（Opyn）
- 稳定币（Frax）

### 流动性挖矿

**SushiSwap 首创:**

- LP 质押获得 $SUSHI 奖励
- 双重收益（手续费 + 代币奖励）
- "吸血鬼攻击"[Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM)

**激励机制:**
```
APR = (手续费收益 + 代币奖励) / LP 投入
通常: 20% - 200%+ APR
```

**代币分发:**
- 引导早期流动性
- 公平分发治理代币
- 冷启动问题的解决方案

**风险:**
- 代币价格下跌
- 高 APR 不可持续
- 无常损失

### 跨链桥流动性

**AMM 作为桥接机制:**

- THORChain: 跨链 AMM（BTC/ETH/BNB 等）
- Synapse: 稳定币跨链桥 + AMM
- Stargate: LayerZero 的跨链流动性

**原理:**
```
链 A: 用户存入 USDC
AMM 池: 链 A USDC ↔ 链 B USDC
链 B: 用户收到 USDC
```

### 杠杆与衍生品

**Perpetual Protocol:**
- vAMM（虚拟 AMM）
- 合成永续合约
- 无需真实资产池

**GMX:**
- GLP 池（多资产流动性）
- LP 作为交易对手方
- 承担交易者盈亏

## 优势与挑战

### 优势

**去中心化与无需许可:**
- 任何人可创建交易对
- 无需中心化审核
- 抗审查和关闭

**永续流动性:**
- 池子永远存在（只要有流动性）
- 无需订单簿深度
- 任意规模交易都能执行（但有滑点）

**可组合性:**
- [智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)间无缝集成
- [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 乐高积木
- 创新协议可直接调用

**透明与可验证:**
- 所有交易链上可查
- 价格公式公开
- 无暗池和特权交易

**被动做市:**
- LP 无需主动管理订单
- 躺赚手续费
- 适合普通用户

### 挑战

**无常损失:**
- 价格波动导致损失
- 可能超过手续费收益
- LP 主要风险来源

**资本效率低:**
- 传统 AMM 大部分流动性闲置
- V3 集中流动性部分解决
- 但增加管理复杂度

**MEV 攻击:**
- 抢跑（Front-running）
- 三明治攻击（Sandwich Attack）
- 套利者获取大部分价值

**大额交易滑点:**
- 恒定乘积的固有问题
- 需要更深的流动性池
- 或使用聚合器拆单

**Gas 成本:**
- Ethereum 主网 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 费高
- 小额交易不经济
- 需依赖 L2 或其他链

**价格操纵风险:**
- 小池子易被操纵
- 影响预言机安全
- 需要 TWAP 等防护

**[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)风险:**
- 代码漏洞
- 闪电贷攻击
- 需要审计和保险

## 未来发展

### 技术创新方向

**1. 更高效的定价曲线:**
- 自适应曲线（根据市场调整）
- 混合曲线（结合 CPMM 和 Stableswap）
- 机器学习优化

**2. 主动流动性管理:**
- 自动再平衡（如 Maverick）
- AI 驱动的区间调整
- 一键策略（如 Gamma、Arrakis）

**3. 更好的[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA):**
- 跨链价格聚合
- 更低延迟
- 更强抗操纵

**4. Layer 2 迁移:**
- Arbitrum、Optimism 上的 [Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM)
- zkSync、StarkNet 的原生 AMM
- 极大降低 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本

**5. 跨链 AMM:**
- THORChain 原生跨链
- [Cosmos](https://learnblockchain.cn/tags/Cosmos) IBC 互操作
- 统一流动性

### 监管与合规

**挑战:**
- 反洗钱（AML）要求
- 证券法规（代币分类）
- 税务合规（复杂的收益计算）

**趋势:**
- 合规版本 AMM（KYC 限制）
- 监管沙盒实验
- 行业自律标准

### 机构采用

**传统金融整合:**
- 做市商使用 AMM 获取流动性
- 资产管理公司提供流动性
- 银行探索 AMM 用于内部市场

**专业工具:**
- 机构级 LP 管理平台
- 复杂的对冲策略
- 风险管理工具

## 推荐阅读

- [What is an Automated Market Maker? - Uniswap Blog](https://blog.uniswap.org/what-is-an-automated-market-maker)
- [How Uniswap works - Uniswap Docs](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Formulas for Automated Market Makers - Faisal Khan](https://faisalkhan.com/knowledge-center/payments-wiki/f/formulas-for-automated-market-makers-amms/)
- [Automated Market Makers: Math, Risks & Solidity Code - Speed Run Ethereum](https://speedrunethereum.com/guides/automated-market-makers-math)
- [Constant Product Automated Market Maker - Medium](https://medium.com/@tomarpari90/constant-product-automated-market-maker-everything-you-need-to-know-5bfeb0251ef2)
- [Constant Function Market Maker - Uniswap V3 Book](https://uniswapv3book.com/milestone_0/constant-function-market-maker.html)
- [What is CPAMM? - Delphi Digital](https://members.delphidigital.io/learn/constant-product-automated-market-maker-cpamm)
- [Automated Market Makers Explained - Chainlink](https://chain.link/education-hub/what-is-an-automated-market-maker-amm)

## 相关概念

- **[DEX](https://learnblockchain.cn/tags/DEX?map=EVM)**（去中心化交易所）
- **流动性提供者**（LP）
- **无常损失**（Impermanent Loss）
- **流动性挖矿**（Yield Farming）
- **滑点**（Slippage）
- **[DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 聚合器**
- **闪电兑换**（Flash Swap）
- **价格[预言机](https://learnblockchain.cn/tags/%E9%A2%84%E8%A8%80%E6%9C%BA)**
- **MEV**
- **Layer 2**
