## Solana 交互库

交互库是用于与 Solana 区块链交互的软件库，不同语言有不同实现。

### 主要库

**JavaScript/TypeScript**
- `@solana/web3.js`：官方 JS SDK
- `@coral-xyz/anchor`：Anchor 框架客户端

**Rust**
- `solana-sdk`：官方 Rust SDK
- `solana-client`：RPC 客户端

**Python**
- `solana-py`：Python SDK

**Go**
- `solana-go`：Go SDK

### 功能

- 连接 RPC 节点
- 构建和发送交易
- 查询账户和余额
- 程序调用
- 事件监听

### 选择建议

**Web 前端**
使用 `@solana/web3.js` + Wallet Adapter

**后端服务**
根据技术栈选择对应语言的 SDK

**智能合约**
使用 `solana-sdk`（Rust）

### 相关概念

- **SDK**：软件开发工具包
- **RPC**：远程过程调用
- **API**：应用程序接口
