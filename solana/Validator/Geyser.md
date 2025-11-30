## Geyser

Geyser 是 Solana 验证器的插件接口，用于实时导出账户和交易数据。它允许开发者订阅区块链状态变化，实时获取账户更新、交易确认和区块信息，是构建索引服务、数据分析工具和实时应用的基础设施。

### 核心功能

Geyser 插件提供以下数据流：

**1. 账户更新（Account Updates）**
当账户的数据、余额或所有者发生变化时触发：
- 账户地址
- 账户数据（完整或增量）
- lamports 余额
- 所有者程序
- 租金状态
- 时隙（slot）信息

**2. 交易通知（Transaction Notifications）**
每笔交易执行后的完整信息：
- 交易签名
- 交易状态（成功/失败）
- 日志消息
- 计算单元消耗
- 涉及的账户列表

**3. 区块元数据（Block Metadata）**
每个区块的完整信息：
- 区块哈希
- 父区块哈希
- 时隙高度
- 区块时间
- 奖励信息

**4. Slot 状态（Slot Status）**
时隙的确认状态变化：
- Processed（已处理）
- Confirmed（已确认）
- Finalized（已最终确定）

### 使用场景

**1. 数据索引服务**
像 Helius、QuickNode 这样的 RPC 提供商使用 Geyser 构建实时索引：
- 解析程序指令
- 追踪 Token 转账
- 监控 NFT 交易
- 构建账户历史记录

**2. 区块链浏览器**
Solscan、SolanaFM 等浏览器使用 Geyser 实时更新：
- 最新交易列表
- 账户余额变化
- 程序活动统计

**3. DeFi 应用监控**
监控链上 DeFi 协议的实时状态：
- 流动性池价格变化
- 大额交易预警
- 清算机会发现

**4. 钱包同步**
钱包应用使用 Geyser 实时更新用户资产：
- Token 余额变化
- NFT 接收通知
- 交易确认状态

### 架构设计

Geyser 采用插件架构，验证器作为数据源，插件作为消费者：

```
Solana Validator
    ↓
Geyser Plugin Interface
    ↓
Plugin Implementation (gRPC, Kafka, PostgreSQL, etc.)
    ↓
External Applications
```

常见的 Geyser 插件实现：
- **gRPC Plugin**：通过 gRPC 流式传输数据
- **Kafka Plugin**：将数据发送到 Kafka 消息队列
- **PostgreSQL Plugin**：直接写入数据库
- **Redis Plugin**：缓存到 Redis

### 配置要求

运行 Geyser 插件需要：

**硬件要求**
- 更高的 CPU 和内存（因为需要额外处理和缓存数据）
- 快速的网络连接（传输大量数据）
- 充足的磁盘 I/O（某些插件需要写入数据库）

**验证器配置**
在验证器启动参数中指定插件：
```bash
solana-validator   --geyser-plugin-config /path/to/geyser-config.json
```

### 性能考虑

**过滤优化**
仅订阅需要的数据，避免处理全量数据：
- 按程序 ID 过滤账户
- 排除投票交易
- 排除失败交易

**批量处理**
将多个更新批量处理，减少网络开销。

**异步处理**
使用异步消息队列（如 Kafka）解耦数据接收和处理。

### 与 Websocket 的对比

| 特性 | Geyser | Websocket（RPC） |
|------|--------|------------------|
| 数据源 | 验证器直连 | RPC 节点 |
| 延迟 | 极低（毫秒级） | 较低（秒级） |
| 完整性 | 100% 数据 | 可能丢失 |
| 成本 | 需要运行插件 | 仅消费 RPC |
| 灵活性 | 高度可定制 | 固定接口 |

### 相关概念

- **Yellowstone**：Solana 官方维护的 Geyser gRPC 插件实现
- **AccountsDB**：Solana 存储账户数据的数据库，Geyser 从这里读取数据
- **Websocket**：RPC 节点提供的实时订阅接口，功能类似但性能和完整性不如 Geyser
