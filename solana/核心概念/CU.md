## CU (计算单元)

CU（Compute Units，计算单元）是 Solana 用来衡量交易执行过程中消耗计算资源的单位。每个操作都会消耗一定数量的 CU，类似于以太坊中的 Gas 概念，但计费方式和限制机制有所不同。

### 基本概念

在 Solana 中，每笔交易执行时都会消耗计算资源，包括：
- CPU 指令执行
- 内存访问
- 账户数据读写
- 跨程序调用（CPI）
- 系统调用（syscall）

CU 就是将这些资源消耗量化的度量单位。不同操作消耗的 CU 数量不同：
- 基础指令：约 1-3 CU
- 内存分配：每字节约 0.5 CU
- 账户验证：每个账户约 100 CU
- CPI 调用：约 1,000 CU 起步
- SHA256 哈希：约 20 CU 每 32 字节

### 限制与配置

**默认限制**
- 每个交易默认预算：200,000 CU
- 单个交易最大限制：1,400,000 CU
- 每个区块的 CU 总量：约 48,000,000 CU

**动态调整**
开发者可以通过 `ComputeBudgetInstruction` 来请求更多的 CU：

```rust
use solana_sdk::compute_budget::ComputeBudgetInstruction;

// 请求 400,000 CU
let set_compute_unit_limit = ComputeBudgetInstruction::set_compute_unit_limit(400_000);

// 设置优先费用（micro-lamports per CU）
let set_compute_unit_price = ComputeBudgetInstruction::set_compute_unit_price(1_000);
```

### CU 与交易费用

Solana 的交易费用由两部分组成：

1. **基础费用**：固定 5,000 lamports（每个签名）
2. **优先费用**：CU 数量 × CU 价格

优先费用计算公式：
```
优先费用 = 实际消耗的 CU × CU 单价（micro-lamports）/ 1,000,000
```

例如，如果交易消耗了 100,000 CU，CU 单价设置为 10,000 micro-lamports：
```
优先费用 = 100,000 × 10,000 / 1,000,000 = 1,000 lamports
总费用 = 5,000 + 1,000 = 6,000 lamports
```

### 优先级排序

当网络拥堵时，验证者会优先打包优先费用更高的交易。CU 价格成为交易竞争的关键因素：

- **低优先级**：CU 价格 = 0（只支付基础费用）
- **中优先级**：CU 价格 = 1,000 - 10,000 micro-lamports
- **高优先级**：CU 价格 > 100,000 micro-lamports

在 DeFi 套利、NFT mint 等场景中，用户往往会设置较高的 CU 价格以确保交易快速执行。

### CU 优化策略

开发者可以通过以下方式降低程序的 CU 消耗：

**1. 减少账户数量**
每个账户的验证和加载都会消耗 CU，尽量合并账户或使用 PDA。

**2. 优化数据结构**
- 使用紧凑的数据类型（u32 而不是 u64）
- 减少序列化/反序列化开销
- 使用 zero-copy 技术避免内存拷贝

**3. 批量操作**
将多个小操作合并成一个交易，减少重复的账户加载和验证。

**4. 避免重复计算**
缓存计算结果，避免在同一交易中重复执行相同的计算。

**5. 使用轻量级库**
选择经过优化的库（如 Anchor 框架），减少不必要的 CU 消耗。

### CU 监控

开发者可以通过以下工具监控 CU 消耗：

- **模拟交易**：在发送前模拟交易，查看预估的 CU 消耗
- **日志分析**：通过 `sol_log_compute_units!()` 宏记录关键点的 CU 消耗
- **性能分析**：使用 Solana Explorer 查看实际交易的 CU 使用情况

### 相关概念

- **Gas（以太坊）**：与 CU 类似的资源计量单位，但以太坊的 Gas 价格波动更大
- **优先费用（Priority Fee）**：基于 CU 消耗计算的额外费用，用于激励验证者优先处理交易
- **交易大小限制**：Solana 每个交易最大 1232 字节，除了 CU 限制外还要考虑字节限制
- **并行执行**：Solana 可以并行执行不冲突的交易，CU 限制是针对单个交易的
