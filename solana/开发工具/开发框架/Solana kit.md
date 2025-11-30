## Kit

Kit 是 Anza（原 Solana Labs）开发的新一代 Solana 开发工具集，也是 @solana/web3.js 的 v2 版本，提供更现代化、模块化的开发体验。

GitHub: https://github.com/anza-xyz/kit

### 核心改进

**模块化设计**
- 按需导入功能模块
- 减小bundle体积
- 更清晰的依赖关系

**TypeScript 优先**
- 完整的类型定义
- 更好的IDE支持
- 类型安全

**性能优化**
- 更快的序列化/反序列化
- 优化的RPC调用
- 减少内存占用

**现代化API**
- 更简洁的接口
- 链式调用
- Promise/Async优化

### 主要功能

**账户操作**
```typescript
import { address, account } from '@solana/kit';

const addr = address('11111111111111111111111111111111');
const accountInfo = await connection.getAccountInfo(addr);
```

**交易构建**
```typescript
import { transaction, instruction } from '@solana/kit';

const tx = transaction()
  .add(transferInstruction)
  .add(memoInstruction);
```

**RPC客户端**
```typescript
import { createSolanaRpc } from '@solana/kit';

const rpc = createSolanaRpc('https://api.mainnet-beta.solana.com');
```

### 迁移指南

从 web3.js v1 迁移到 Kit(v2)：

**v1 (旧)**
```typescript
import { Connection, PublicKey } from '@solana/web3.js';

const connection = new Connection('...');
const pubkey = new PublicKey('...');
```

**v2 (Kit)**
```typescript
import { createSolanaRpc, address } from '@solana/kit';

const rpc = createSolanaRpc('...');
const addr = address('...');
```

### 开发状态

Kit 目前处于积极开发中：
- 持续添加新功能
- API 可能有Breaking Changes
- 建议生产环境谨慎使用

### 相关概念

- **web3.js**：Solana JavaScript SDK
- **Anza**：原 Solana Labs，Kit 的开发团队
- **模块化**：按功能拆分的设计理念
