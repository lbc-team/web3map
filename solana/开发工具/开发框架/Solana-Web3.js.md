## web3.js

@solana/web3.js 是 Solana 官方的 JavaScript SDK，用于在浏览器和 Node.js 中与 Solana 区块链交互。它是 Solana 前端开发的基础库。

### 核心功能

**1. 连接 RPC**
```javascript
import { Connection } from '@solana/web3.js';

const connection = new Connection('https://api.mainnet-beta.solana.com');
```

**2. 创建交易**
```javascript
import { Transaction, SystemProgram } from '@solana/web3.js';

const transaction = new Transaction().add(
  SystemProgram.transfer({
    fromPubkey: sender.publicKey,
    toPubkey: recipient,
    lamports: 1000000,
  })
);
```

**3. 签名和发送**
```javascript
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.sign(sender);
const signature = await connection.sendRawTransaction(transaction.serialize());
await connection.confirmTransaction(signature);
```

**4. 查询数据**
```javascript
// 获取余额
const balance = await connection.getBalance(publicKey);

// 获取账户信息
const accountInfo = await connection.getAccountInfo(publicKey);

// 获取交易
const transaction = await connection.getTransaction(signature);
```

### 常用类和方法

**PublicKey**
```javascript
import { PublicKey } from '@solana/web3.js';
const pubkey = new PublicKey('地址字符串');
```

**Keypair**
```javascript
import { Keypair } from '@solana/web3.js';

// 生成新密钥对
const keypair = Keypair.generate();

// 从私钥恢复
const keypair = Keypair.fromSecretKey(secretKey);
```

**SystemProgram**
系统程序的指令构造器。

**Transaction**
交易对象，包含指令列表。

### SPL Token 操作

需要额外安装 `@solana/spl-token`：
```javascript
import { getAssociatedTokenAddress, createTransferInstruction } from '@solana/spl-token';

const ata = await getAssociatedTokenAddress(mint, owner);
```

### 最佳实践

**1. 使用 Commitment 级别**
```javascript
await connection.confirmTransaction(signature, 'confirmed');
```

**2. 错误处理**
```javascript
try {
  await connection.sendTransaction(transaction, [signer]);
} catch (error) {
  console.error('Transaction failed:', error);
}
```

**3. 批量请求**
使用 `getMultipleAccountsInfo` 减少 RPC 调用。


web3.js 2.0 改名为 kit

### 相关概念

- **Anchor**：高级 Solana 程序框架
- **Wallet Adapter**：钱包连接库
- **SPL Token**：代币标准库
