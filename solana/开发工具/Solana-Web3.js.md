## Solana Web3.js 概述

[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) Web3.js 是 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 区块链的官方 [JavaScript](https://learnblockchain.cn/tags/JavaScript) SDK,为开发者提供了与 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 网络交互的完整工具集。作为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 生态系统的核心库,Web3.js 支持连接节点、管理账户、构建交易、调用程序等所有链上操作。无论是构建钱包、[DApp](https://learnblockchain.cn/tags/DApp) 还是后端服务,Web3.js 都是不可或缺的基础工具,被数千个 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 应用广泛使用。

**官方文档**: https://solana-labs.github.io/solana-web3.js/

## 核心功能

### 1. 连接管理

与 Solana 集群通信:

- **Connection**: RPC 连接管理
- **集群选择**: Mainnet、Testnet、Devnet
- **自定义 RPC**: 支持私有节点
- **WebSocket**: 实时订阅链上事件
- **批量请求**: 优化 RPC 调用效率

### 2. 账户操作

密钥和账户管理:

- **Keypair**: 生成和管理密钥对
- **PublicKey**: 公钥表示和操作
- **账户查询**: 获取账户数据和余额
- **账户订阅**: 监听账户变化
- **助记词**: BIP39 助记词支持

### 3. 交易构建

灵活的交易创建:

- **Transaction**: 交易对象
- **TransactionInstruction**: 指令构建
- **SystemProgram**: 系统程序指令
- **签名管理**: 单签和多签支持
- **交易模拟**: 发送前模拟执行

### 4. 程序交互

与链上程序通信:

- **程序调用**: 调用智能合约
- **指令编码**: 序列化指令数据
- **账户传递**: 传递所需账户
- **CPI**: 跨程序调用支持
- **事件监听**: 监听程序事件

## 快速开始

### 安装

```bash
npm install @solana/web3.js
```

### 连接到 Solana

```javascript
const { Connection, clusterApiUrl } = require('@solana/web3.js')

// 连接到 Devnet
const connection = new Connection(clusterApiUrl('devnet'), 'confirmed')

// 或连接到自定义 RPC
const customConnection = new Connection('https://api.mainnet-beta.solana.com')

// 获取版本信息
const version = await connection.getVersion()
console.log('Solana 版本:', version)
```

### 创建和管理账户

```javascript
const { Keypair } = require('@solana/web3.js')

// 生成新密钥对
const keypair = Keypair.generate()
console.log('公钥:', keypair.publicKey.toBase58())
console.log('私钥:', keypair.secretKey)

// 从私钥恢复
const restoredKeypair = Keypair.fromSecretKey(secretKey)

// 查询余额
const balance = await connection.getBalance(keypair.publicKey)
console.log('余额:', balance / 1e9, 'SOL')
```

## 核心操作

### 1. 发送 SOL

转账 SOL 代币:

```javascript
const {
  Transaction,
  SystemProgram,
  LAMPORTS_PER_SOL,
  sendAndConfirmTransaction
} = require('@solana/web3.js')

async function sendSOL(from, to, amount) {
  // 创建转账指令
  const transaction = new Transaction().add(
    SystemProgram.transfer({
      fromPubkey: from.publicKey,
      toPubkey: to,
      lamports: amount * LAMPORTS_PER_SOL
    })
  )

  // 发送并确认交易
  const signature = await sendAndConfirmTransaction(
    connection,
    transaction,
    [from]
  )

  console.log('交易签名:', signature)
  return signature
}
```

### 2. 创建账户

创建新的链上账户:

```javascript
const {
  SystemProgram,
  Keypair,
  Transaction
} = require('@solana/web3.js')

async function createAccount(payer, space, programId) {
  const newAccount = Keypair.generate()

  // 计算租金
  const lamports = await connection.getMinimumBalanceForRentExemption(space)

  // 创建账户指令
  const transaction = new Transaction().add(
    SystemProgram.createAccount({
      fromPubkey: payer.publicKey,
      newAccountPubkey: newAccount.publicKey,
      lamports,
      space,
      programId
    })
  )

  // 发送交易
  await sendAndConfirmTransaction(
    connection,
    transaction,
    [payer, newAccount]
  )

  return newAccount
}
```

### 3. 调用程序

与智能合约交互:

```javascript
const {
  TransactionInstruction,
  PublicKey
} = require('@solana/web3.js')

async function callProgram(programId, data, accounts) {
  // 构建指令
  const instruction = new TransactionInstruction({
    keys: accounts.map(acc => ({
      pubkey: acc.pubkey,
      isSigner: acc.isSigner,
      isWritable: acc.isWritable
    })),
    programId,
    data: Buffer.from(data)
  })

  // 创建交易
  const transaction = new Transaction().add(instruction)

  // 发送交易
  const signature = await sendAndConfirmTransaction(
    connection,
    transaction,
    [payer]
  )

  return signature
}
```

### 4. 查询账户信息

获取账户数据:

```javascript
async function getAccountInfo(publicKey) {
  // 获取账户信息
  const accountInfo = await connection.getAccountInfo(publicKey)

  if (!accountInfo) {
    console.log('账户不存在')
    return null
  }

  console.log('所有者:', accountInfo.owner.toBase58())
  console.log('余额:', accountInfo.lamports / 1e9, 'SOL')
  console.log('数据长度:', accountInfo.data.length)
  console.log('可执行:', accountInfo.executable)

  return accountInfo
}
```

### 5. 监听事件

订阅链上变化:

```javascript
// 监听账户变化
const subscriptionId = connection.onAccountChange(
  publicKey,
  (accountInfo, context) => {
    console.log('账户已更新:', accountInfo)
  },
  'confirmed'
)

// 监听日志
const logsSubscription = connection.onLogs(
  programId,
  (logs, context) => {
    console.log('程序日志:', logs)
  },
  'confirmed'
)

// 取消订阅
connection.removeAccountChangeListener(subscriptionId)
```

### 6. 交易历史

查询交易记录:

```javascript
async function getTransactionHistory(publicKey) {
  // 获取签名列表
  const signatures = await connection.getSignaturesForAddress(publicKey, {
    limit: 10
  })

  // 获取交易详情
  for (const sig of signatures) {
    const tx = await connection.getTransaction(sig.signature)
    console.log('交易:', tx)
  }
}
```

## 高级功能

### 1. 版本化交易

使用地址查找表:

```javascript
const {
  VersionedTransaction,
  TransactionMessage,
  AddressLookupTableProgram
} = require('@solana/web3.js')

// 创建版本化交易
const messageV0 = new TransactionMessage({
  payerKey: payer.publicKey,
  recentBlockhash: blockhash,
  instructions: [instruction]
}).compileToV0Message([lookupTableAccount])

const transaction = new VersionedTransaction(messageV0)
```

### 2. 优先费用

设置交易优先级:

```javascript
const {
  ComputeBudgetProgram
} = require('@solana/web3.js')

// 设置计算单元价格
const priorityFeeInstruction = ComputeBudgetProgram.setComputeUnitPrice({
  microLamports: 1000
})

transaction.add(priorityFeeInstruction)
```

### 3. 部分签名

多签名交易:

```javascript
// 创建交易
const transaction = new Transaction().add(instruction)
transaction.feePayer = payer.publicKey
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash

// 第一个签名者签名
transaction.partialSign(signer1)

// 序列化并传递给其他签名者
const serialized = transaction.serialize({ requireAllSignatures: false })

// 其他签名者签名
transaction.partialSign(signer2)

// 发送完整签名的交易
const signature = await connection.sendRawTransaction(transaction.serialize())
```

### 4. 模拟交易

测试交易执行:

```javascript
// 模拟交易
const simulation = await connection.simulateTransaction(transaction)

if (simulation.value.err) {
  console.error('模拟失败:', simulation.value.err)
} else {
  console.log('模拟成功')
  console.log('日志:', simulation.value.logs)
}
```

## 最佳实践

### 1. 错误处理

```javascript
try {
  const signature = await sendAndConfirmTransaction(
    connection,
    transaction,
    [payer]
  )
} catch (error) {
  if (error.message.includes('insufficient funds')) {
    console.error('余额不足')
  } else if (error.message.includes('blockhash not found')) {
    console.error('区块哈希过期,请重试')
  } else {
    console.error('交易失败:', error)
  }
}
```

### 2. 重试机制

```javascript
async function sendTransactionWithRetry(transaction, signers, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      // 更新 blockhash
      transaction.recentBlockhash = (
        await connection.getLatestBlockhash()
      ).blockhash

      const signature = await sendAndConfirmTransaction(
        connection,
        transaction,
        signers
      )
      return signature
    } catch (error) {
      if (i === maxRetries - 1) throw error
      await new Promise(r => setTimeout(r, 1000 * (i + 1)))
    }
  }
}
```

### 3. 批量查询

```javascript
// 批量获取多个账户
const publicKeys = [pubkey1, pubkey2, pubkey3]
const accounts = await connection.getMultipleAccountsInfo(publicKeys)
```

### 4. 计算单元优化

```javascript
const {
  ComputeBudgetProgram
} = require('@solana/web3.js')

// 设置计算单元限制
transaction.add(
  ComputeBudgetProgram.setComputeUnitLimit({
    units: 200000
  })
)
```

## 常见问题

### 1. Blockhash 过期

**问题**: 交易失败提示 blockhash 过期
**解决**: 获取最新的 blockhash 并重新签名

### 2. 429 错误

**问题**: 公共 RPC 限流
**解决**: 使用付费 RPC 服务或自建节点

### 3. 交易确认慢

**问题**: 交易长时间未确认
**解决**: 增加优先费用或使用更快的 commitment 级别

## 相关概念与技术

- **[Solana](https://learnblockchain.cn/tags/Solana?map=Solana)**: Solana Web3.js 所服务的区块链
- **[Anchor](https://www.anchor-lang.com/)**: Solana 智能合约框架
- **[Wallet Adapter](https://github.com/anza-xyz/wallet-adapter)**: Solana 钱包连接库
- **[Metaplex](https://www.metaplex.com/)**: Solana NFT 标准和工具
- **[SPL Token](https://spl.solana.com/)**: Solana 代币程序

## 总结

Solana Web3.js 作为 Solana 生态系统的基础 SDK,提供了完整而强大的工具集来构建 Solana 应用。从简单的转账到复杂的程序交互,Web3.js 都能提供简洁的 API 和可靠的功能。随着 Solana 的发展,Web3.js 也在不断演进,支持版本化交易、优先费用等新特性。对于 Solana 开发者而言,深入掌握 Web3.js 是构建高质量应用的基础。
