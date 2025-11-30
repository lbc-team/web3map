## Solana 交易

在 Solana 中，交易（Transaction）是用户与区块链交互的基本单位。一个交易包含一个或多个指令（Instructions），每个指令调用一个程序来执行特定操作。Solana 的交易设计注重高性能和原子性。

### 交易结构

一个完整的 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 交易包含：

**1. 签名（Signatures）**
- 一个或多个签名
- 对应交易中的签名者（Signers）
- 使用 Ed25519 椭圆曲线算法

**2. 消息（Message）**
包含交易的核心内容：
- **消息头（Header）**：指定需要签名的账户数量、只读账户数量等
- **账户密钥列表（Account Keys）**：交易涉及的所有账户地址
- **最近区块哈希（Recent Blockhash）**：防止重放攻击
- **指令列表（Instructions）**：要执行的操作

### 交易生命周期

**1. 构建交易**
```javascript
const transaction = new Transaction().add(
  SystemProgram.transfer({
    fromPubkey: sender.publicKey,
    toPubkey: receiver.publicKey,
    lamports: 1000000,
  })
);
```

**2. 设置最近区块哈希**
```javascript
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
```

**3. 签名**
```javascript
transaction.sign(sender);
```

**4. 发送**
```javascript
const signature = await connection.sendTransaction(transaction, [sender]);
```

**5. 确认**
```javascript
await connection.confirmTransaction(signature, 'confirmed');
```

### 交易限制

**大小限制**
- 最大 1232 字节（序列化后）
- 限制账户数量和指令数量
- 超过限制需要分拆成多个交易

**计算限制**
- 默认 200,000 CU
- 最高可申请 1,400,000 CU
- 通过 ComputeBudgetInstruction 调整

**账户限制**
- 单个交易最多锁定 64 个可写账户
- 只读账户无限制
- 账户不能重复（同一账户只能出现一次）

### 交易费用

**基础费用**
- 每个签名 5,000 lamports
- 多签交易费用更高

**优先费用**
- 基于 CU 消耗和 CU 价格
- 网络拥堵时提高优先费用可加快确认

### 原子性

[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 交易具有原子性：
- 所有指令要么全部成功，要么全部失败
- 不会出现部分执行的情况
- 失败时状态完全回滚

这使得复杂的多步骤操作（如 [DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 交易）可以安全执行。

### 交易状态

**Processed**
- 交易已被执行并打包进区块
- 可能被回滚
- 确认时间：<1 秒

**Confirmed**
- 区块获得超过 2/3 验证者投票
- 回滚概率极低
- 确认时间：约 400-600 毫秒

**Finalized**
- 区块完全确定，不可逆
- 确认时间：约 13-15 秒

### 常见交易类型

**1. 代币转账**
```javascript
const instruction = Token.createTransferInstruction(
  TOKEN_PROGRAM_ID,
  source,
  destination,
  owner,
  [],
  amount
);
```

**2. 创建账户**
```javascript
SystemProgram.createAccount({
  fromPubkey: payer,
  newAccountPubkey: newAccount,
  lamports: rentExemption,
  space: dataSize,
  programId: ownerProgram,
});
```

**3. 跨程序调用**
在程序内部调用其他程序的指令。

### 交易优化

**1. 批量操作**
将多个操作合并到一个交易中，节省费用和时间。

**2. 优先费用设置**
```javascript
transaction.add(
  ComputeBudgetProgram.setComputeUnitPrice({
    microLamports: 1000
  })
);
```

**3. 查找表（Lookup Tables）**
通过地址查找表减少交易大小，突破 64 账户限制。

### 相关概念

- **指令（Instruction）**：交易的组成部分，调用程序执行操作
- **CU（计算单元）**：衡量交易消耗的计算资源
- **Blockhash**：用于防止交易重放的时间戳
- **原子性（Atomicity）**：交易要么全部成功，要么全部失败
