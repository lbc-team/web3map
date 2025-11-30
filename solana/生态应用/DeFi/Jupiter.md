## Jupiter


官网：https://jup.ag/

Jupiter 是 Solana 生态系统中最大的去中心化交易聚合器（[DEX](https://learnblockchain.cn/tags/DEX?map=EVM) Aggregator），为用户提供最优的代币交换路径和价格。它通过整合多个 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 的流动性池，自动寻找最佳交易路径，帮助用户以最低的滑点和最优的价格完成代币兑换。

### 核心功能

**1. 交易聚合**
Jupiter 聚合了 Solana 上几乎所有主流 DEX，包括：
- Orca
- Raydium  
- Saber
- Meteora
- Phoenix
- Lifinity
- 等 20+ 个 DEX

当用户发起交易时，Jupiter 会：
- 查询所有 DEX 的价格和流动性
- 计算所有可能的交易路径（包括多跳路径）
- 选择滑点最小、价格最优的路径
- 执行原子性的跨 DEX 交易

**2. 限价单（Limit Orders）**
Jupiter 提供链上限价单功能，用户可以：
- 设定目标价格
- 设置有效期
- 部分成交
- 自动执行

限价单通过链上程序实现，资金安全性高，且可以被任何人触发（Keeper 机制）。

**3. DCA（定投）**
支持自动定期买入功能：
- 按设定时间间隔自动执行交易
- 平摊成本，降低波动风险
- 完全链上执行

**4. Perpetuals（永续合约）**
Jupiter 还推出了永续合约交易功能，支持：
- 高达 100x 杠杆
- 多种主流代币对
- 零价格影响（使用预言机喂价）
- 低交易费用

### 技术优势

**智能路由算法**
Jupiter 的核心是其智能路由引擎，能够：
- 实时计算数百万条可能的交易路径
- 考虑滑点、手续费、价格影响等因素
- 支持跨多个池的拆分订单（Split Trades）
- 在几百毫秒内找到最优路径

例如，如果用户要用 SOL 买 USDC，Jupiter 可能会发现通过 SOL → mSOL → USDC 的路径比直接 SOL → USDC 更优。

**MEV 保护**
Jupiter 实现了多种 MEV 保护机制：
- 交易路径随机化
- 与 [Jito](https://learnblockchain.cn/tags/Jito?map=Solana) 集成，防止抢跑
- 提供滑点保护设置

**高性能**
- 利用 Solana 的高 TPS，实现秒级交易确认
- 并行处理多个交易路由计算
- 缓存流动性数据，减少 RPC 调用

### JUP 代币

2024 年初，Jupiter 推出了治理代币 JUP：

**代币用途**
- 治理投票（协议参数、功能提案）
- 质押获得手续费分成
- 参与 Launchpad（新项目发行平台）

**分配机制**
- 通过空投分发给历史用户
- 社区金库用于生态发展
- 团队和投资人代币有锁定期

### Jupiter Launchpad

Jupiter 还推出了代币发行平台 Jupiter Launchpad（JLP），为优质项目提供：
- 公平的代币分发机制（防止女巫攻击）
- 自动做市和流动性引导
- 社区审查和投票机制

### 数据表现

Jupiter 在 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 生态中占据主导地位：
- 交易量占 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) DEX 总量的 60-70%
- 日均交易量数十亿美元
- 支持 1000+ 代币交易对
- 日活用户数万

### 相关概念

- **DEX Aggregator**：去中心化交易聚合器，整合多个 DEX 的流动性
- **1inch（[以太坊](https://learnblockchain.cn/tags/以太坊?map=[EVM](https://learnblockchain.cn/tags/EVM?map=EVM))）**：以太坊上类似的交易聚合器
- **AMM**：自动做市商，Jupiter 聚合的 DEX 大多基于 AMM 模型
- **Raydium/Orca**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 上的原生 DEX，Jupiter 的流动性来源
