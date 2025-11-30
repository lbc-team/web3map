## Solana 程序执行

在 Solana 中，执行（Execution）指的是交易和指令在[SVM](https://learnblockchain.cn/tags/SVM?map=Solana)虚拟机中的运行过程。Solana 的执行引擎 Sealevel 是其高性能的核心，支持并行执行、确定性和高效的资源管理。

### Sealevel 并行运行时

Sealevel 是 Solana 的并行智能合约运行时，与以太坊的串行执行模型完全不同。

**并行执行**
Solana 可以同时执行多个不冲突的交易：
- 分析交易涉及的账户
- 识别无冲突的交易
- 在多个 CPU 核心上并行执行

例如：
- 交易 A 修改账户 X
- 交易 B 修改账户 Y
- A 和 B 可以并行执行

**冲突检测**
如果两个交易都要写入同一账户：
- 它们必须串行执行
- 按交易费用和时间戳排序
- 前一个执行完才能执行下一个

这种机制使 Solana 能充分利用现代多核 CPU，实现高吞吐量。

### 执行流程

**1. 交易接收**
验证者接收交易后：
- 验证签名
- 检查账户余额
- 验证 blockhash 有效性

**2. 调度**
调度器分析交易：
- 提取涉及的账户
- 构建账户依赖图
- 将无冲突交易分组

**3. 并行执行**
在多个线程中执行：
- 加载账户数据
- 调用 eBPF 程序
- 更新账户状态
- 记录日志和 CU 消耗

**4. 状态提交**
执行成功后：
- 将更新写回 AccountsDB
- 更新 Merkle 树
- 生成交易收据

### eBPF 虚拟机

Solana 使用 eBPF 作为智能合约的执行环境。

**执行特性**
- **JIT 编译**：eBPF 字节码即时编译成本地机器码
- **沙箱隔离**：程序无法访问系统资源
- **确定性**：相同输入产生相同输出
- **可验证**：静态分析确保安全性

**执行限制**
- 计算单元（CU）限制
- 调用深度限制（4 层 [CPI](https://learnblockchain.cn/tags/CPI?map=Solana)）
- 堆栈大小限制（32KB）
- 账户数据大小限制（10MB）

### 账户访问模型

**只读 vs 可写**
- **只读账户**：多个交易可并行读取
- **可写账户**：独占锁定，串行写入

**预先声明**
交易必须预先声明所有涉及的账户：
- 无法在执行中访问未声明的账户
- 使调度器能提前检测冲突
- 支持乐观并发控制

### 确定性保证

[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 执行是完全确定性的：

**相同输入**
- 相同交易
- 相同账户状态
- 相同程序代码

**相同输出**
- 相同的状态变化
- 相同的日志输出
- 相同的 CU 消耗

这确保所有验证者能达成一致。

### 性能优化

**1. 预取（Prefetching）**
提前加载账户数据到缓存，减少等待时间。

**2. 流水线（Pipelining）**
将交易处理分为多个阶段：
- 接收 → 验证 → 执行 → 提交
- 各阶段并行处理不同批次

**3. 批量处理**
- 批量加载账户
- 批量写入状态
- 减少 I/O 开销

**4. SIMD 优化**
利用 CPU 的 SIMD 指令加速：
- 签名验证
- 哈希计算
- 数据序列化

### 执行失败处理

**失败原因**
- CU 耗尽
- 程序错误（panic, assert 失败）
- 账户验证失败
- [CPI](https://learnblockchain.cn/tags/CPI?map=Solana) 深度超限

**失败后果**
- 整个交易回滚
- 账户状态不变
- 仍然扣除交易费用（防止 DoS）
- 返回错误日志

### 与 EVM 对比

| 特性 | [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) Sealevel | Ethereum EVM |
|------|-----------------|--------------|
| 并行性 | 支持并行 | 串行执行 |
| 状态访问 | 预先声明账户 | 动态访问 |
| 执行环境 | eBPF (寄存器) | EVM (栈) |
| 吞吐量 | 高（65K TPS） | 低（15 TPS） |
| Gas 模型 | CU 预算 | 动态 Gas |

### 相关概念

- **Sealevel**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 的并行运行时引擎
- **eBPF**：[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 智能合约的字节码格式
- **CU（计算单元）**：衡量执行消耗的资源单位
- **AccountsDB**：存储账户状态的数据库
