## Token-2022

Token-2022（也称为 Token Extensions 或 SPL Token-2022）是 SPL Token 的升级版本，增加了许多新特性和扩展功能，为 Solana 代币提供更强大和灵活的功能。

### 核心改进

**向后兼容**
Token-2022 与原 SPL Token 完全兼容：
- 现有程序可以无缝支持
- 相同的基础接口
- 可选的扩展功能

**模块化设计**
功能以扩展（Extensions）形式添加：
- 按需启用功能
- 降低复杂度
- 灵活组合

### 主要扩展功能

**1. 转账手续费（Transfer Fees）**
代币转账时自动收取手续费：
- 设置手续费比例
- 手续费归代币创建者
- 适合收益分成场景

```rust
// 示例：设置 1% 转账手续费
transfer_fee: 100, // basis points (1%)
```

**2. 转账钩子（Transfer Hooks）**
在转账前/后执行自定义逻辑：
- 调用外部程序
- 实现复杂的转账规则
- 合规性检查

用途：
- KYC/AML 验证
- 黑名单/白名单
- 自动税务处理

**3. 保密转账（Confidential Transfers）**
隐藏转账金额：
- 使用零知识证明
- 保护财务隐私
- 仍可验证有效性

**4. 永久委托（Permanent Delegate）**
指定一个永久的委托者：
- 可以在任何情况下转移代币
- 用于监管合规
- 紧急恢复机制

**5. 利息 bearing 代币（Interest Bearing Tokens）**
代币余额随时间自动增长：
- 链上计算利息
- 无需手动分发
- 适合存款凭证、债券等

**6. 元数据扩展（Metadata Extension）**
直接在 Mint 账户存储元数据：
- 名称、符号、URI
- 无需额外账户
- 降低成本

**7. 默认账户状态（Default Account State）**
新建 Token 账户的默认状态：
- 可设为冻结状态
- 需要 KYC 后解冻
- 合规性工具

**8. 不可转让代币（Non-Transferable Tokens）**
创建后无法转移的代币：
- 灵魂绑定代币（Soulbound）
- 会员凭证
- 成就徽章

**9. 备忘录必需（Memo Required）**
转账时必须附加备忘录：
- 合规要求
- 附加转账信息
- 审计追踪

**10. [CPI](https://learnblockchain.cn/tags/CPI?map=Solana) 保护（[CPI](https://learnblockchain.cn/tags/CPI?map=Solana) Guard）**
防止跨程序调用盗取代币：
- 增强安全性
- 防止某些攻击向量

### 使用示例

**创建带转账手续费的代币**
```bash
spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb   --enable-transfer-fee   --transfer-fee-basis-points 100   --max-transfer-fee 10000000
```

**启用元数据扩展**
```bash
spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb   --enable-metadata
```

### 程序 ID

Token-2022 使用不同的程序 ID：
```
TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb
```

原 SPL Token：
```
TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
```

### 采用情况

**优势**
- 丰富的功能
- 官方支持
- 持续更新

**挑战**
- 生态采用需要时间
- 钱包和 DApp 需要更新
- 部分功能仍在测试

### 与 [SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) 对比

| 特性 | [SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) | Token-2022 |
|------|-----------|------------|
| 基础功能 | ✓ | ✓ |
| 转账手续费 | ✗ | ✓ |
| 转账钩子 | ✗ | ✓ |
| 保密转账 | ✗ | ✓ |
| 元数据 | 外部 | 内置 |
| 利息 | ✗ | ✓ |

### 未来发展

**更多扩展**
[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 团队持续添加新扩展功能。

**生态集成**
主流钱包、DEX、DeFi 协议逐步集成。

**标准化**
成为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 代币的新标准。

### 相关概念

- **[SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana)**：原始的 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 代币标准
- **扩展（Extensions）**：模块化的功能增强
- **零知识证明**：保密转账的技术基础
- **合规性**：部分扩展专为合规设计
