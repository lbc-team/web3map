## Raydium

Raydium 是 Solana 上第一个也是最大的自动做市商（AMM）去中心化交易所，它同时也是Solana上唯一一个同时提供链上订单簿和AMM流动性池的DEX。Raydium 的独特之处在于它与 Serum 订单簿的深度集成，使其流动性可以被整个 Solana 生态共享。

### 核心功能

**1. AMM 交易**
Raydium 采用恒定乘积做市商模型（x * y = k）：
- 用户可以直接与流动性池交易
- 无需订单匹配，即时成交
- 价格由池中代币比例决定

**2. 流动性挖矿**
用户向流动性池提供代币对，获得：
- 交易手续费分成（0.25%，其中 0.22% 给 LP）
- RAY 代币奖励
- 部分池还有双重激励（项目方代币）

**3. 与 OpenBook 集成**
这是 Raydium 最独特的功能：
- Raydium 的流动性同时存在于 AMM 池和 OpenBook 订单簿
- 其他 DEX（如 Orca）可以访问这部分流动性
- 提高了整个生态的资金效率

**4. AcceleRaytor（LaunchPad）**
代币发行平台，支持：
- IDO（首次 DEX 发行）
- 公平的代币分配机制
- 自动创建流动性池

**5. 农场（Farms）**
质押 LP token 获得额外奖励：
- 单一质押（RAY）
- 双币质押（LP tokens）
- 双重奖励农场

### 技术特性

**订单簿 + AMM 混合模型**
Raydium 创新性地将两种模式结合：
- AMM 提供即时流动性
- 订单簿提供更好的价格发现
- 流动性互通，降低滑点

**高性能**
利用 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 的高 TPS：
- 交易确认时间 < 1 秒
- 极低的手续费（约 $0.00025）
- 支持高频交易

**无常损失缓解**
- 提供集中流动性池（Concentrated Liquidity）
- 允许 LP 设定价格区间
- 提高资金利用率，降低无常损失

### RAY 代币

**代币用途**
- 治理投票
- 质押获得协议收入分成
- AcceleRaytor 参与权
- 手续费折扣

**代币经济**
- 总供应量：555,000,000 RAY
- 通过流动性挖矿逐步释放
- 部分手续费用于回购销毁

### 生态地位

Raydium 是 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) DeFi 的基础设施：
- 最早的主流 DEX 之一
- 为新代币提供首发平台
- 大量项目通过 Raydium 启动流动性
- 与 Jupiter 等聚合器深度集成

**数据表现**
- TVL（总锁仓量）：数亿美元
- 日交易量：数十亿美元（通过聚合器）
- 支持 1000+ 交易对
- 活跃流动性池 500+

### 产品演进

**Raydium V3（CLMM）**
2023 年推出的集中流动性版本：
- 类似 Uniswap V3
- LP 可以自定义价格区间
- 资金效率提升 4000%+
- 支持多级费率（0.01%, 0.05%, 0.25%）

### 相关概念

- **Uniswap**：以太坊上最大的 AMM，Raydium 的对标项目
- **OpenBook（原 Serum）**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 上的链上订单簿协议
- **Jupiter**：聚合 Raydium 流动性的交易路由器
- **Orca**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 上另一个主流 AMM，竞争对手
