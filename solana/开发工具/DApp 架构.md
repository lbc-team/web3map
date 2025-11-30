## DApp 架构

DApp（去中心化应用）架构指 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 上去中心化应用的技术架构设计。

### 典型架构

**前端**
- React/Next.js
- Wallet Adapter
- [web3.js](https://learnblockchain.cn/tags/?map=Solana)

**[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)（链上）**
- Rust/[Anchor](https://learnblockchain.cn/tags/Anchor?map=Solana) 程序
- 状态存储
- 业务逻辑

**后端（链下）**
- 数据索引（Geyser）
- API 服务
- 缓存层

**基础设施**
- RPC 节点（[Helius](https://learnblockchain.cn/tags/Helius?map=Solana)）
- IPFS/Arweave（存储）
- CDN

### 设计原则

**最小化链上逻辑**
只把必要的逻辑放链上，降低成本。

**链下计算**
复杂计算在链下进行，链上验证。

**数据可用性**
通过索引服务提供快速查询。

### 安全考虑

- 前端验证 + 链上验证
- 私钥本地存储
- 交易模拟
- 错误处理

### 性能优化

- 缓存常用数据
- 批量查询
- 预加载
- 乐观更新

### 相关概念

- **[DApp](https://learnblockchain.cn/tags/DApp)**：去中心化应用
- **架构设计**：系统结构规划
- **全栈开发**：前后端 + 智能合约
