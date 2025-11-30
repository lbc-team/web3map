## Marginfi

Marginfi 是 Solana 上的去中心化借贷协议，专注于提供安全、高效的借贷服务。Marginfi 采用去中心化、透明的设计，是 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) DeFi 生态中快速崛起的借贷平台。

### 核心功能

**1. 借贷**
- 存入资产赚取利息
- 借出资产支付利息
- 支持主流资产（SOL, USDC, mSOL 等）

**2. 杠杆**
- 循环借贷实现杠杆
- 一键杠杆功能
- 最高 3-5x 杠杆

**3. 清算**
- 自动化清算机制
- 清算惩罚奖励清算人
- 保护协议偿付能力

### 利率模型

采用动态利率模型：
- 利率随utilization（使用率）变化
- 高使用率 → 高利率
- 激励供需平衡

### 风险管理

**抵押率（LTV）**
不同资产不同抵押率：
- SOL：75%
- mSOL：80%
- USDC：90%

**清算阈值**
当健康度 < 1 时触发清算。

### MRGN 代币

- 治理投票
- 协议收入分成
- 质押激励

### 与 Aave 对比

| 特性 | Marginfi | Aave |
|------|----------|------|
| 链 | [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) | Ethereum/多链 |
| Gas 费 | 极低 | 高 |
| 速度 | 快 | 慢 |
| TVL | 较小 | 巨大 |

### 相关概念

- **Kamino Lend**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 另一个借贷协议
- **Aave**：以太坊最大借贷协议
- **清算**：强制平仓保护协议
