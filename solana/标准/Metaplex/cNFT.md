## cNFT (Compressed NFT)

cNFT（Compressed NFT，压缩 NFT）是 Metaplex 开发的突破性技术，通过状态压缩大幅降低 NFT 的铸造和存储成本，使大规模 NFT 发行成为可能。

### 核心问题

**传统 NFT 成本高**
- 每个 NFT 需要独立的 Token 账户
- 租金豁免余额：约 0.012 SOL
- 铸造 100 万个 NFT：12,000 SOL（数百万美元）
- 限制了大规模应用

### cNFT 解决方案

**状态压缩**
使用 Merkle 树压缩 NFT 数据：
- 链上只存储树根（32 字节）
- 完整数据存储在链下（Arweave/Shadow Drive）
- 通过 Merkle 证明验证所有权

**成本对比**
- 传统 NFT：约 0.012 SOL/个
- cNFT：约 0.0001 SOL/个
- **降低 100 倍**

### 工作原理

**Merkle 树结构**
```
              Root (链上)
             /              Hash    Hash
         /  \    /         H1  H2  H3  H4
       |   |   |   |
     NFT1 NFT2 NFT3 NFT4
```

**铸造流程**
1. 将 NFT 数据添加到 Merkle 树
2. 更新树根到链上
3. 完整数据存储到 Arweave

**验证所有权**
1. 用户提供 NFT 数据
2. 提供 Merkle 证明（路径）
3. 链上验证：计算根是否匹配
4. 验证通过 = 拥有该 NFT

### 技术实现

**Bubblegum [Program](https://learnblockchain.cn/tags/Program?map=Solana)**
[Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) 的 cNFT 程序：
- 管理 Merkle 树
- 验证所有权
- 处理转移

**并发 Merkle 树**
使用并发 Merkle 树数据结构：
- 支持并行更新
- 避免冲突
- 提高吞吐量

**树配置**
```
树深度：14-30（最多 2^30 个 NFT）
并发缓冲区：8-2048
```

### 使用场景

**大规模空投**
- 社区奖励
- 活动纪念品
- 用户留存

**游戏资产**
- 游戏道具
- 角色装备
- 消耗品

**会员系统**
- 会员卡
- 积分凭证
- 访问权限

**实用 NFT**
- 票务
- 优惠券
- 证书

### 创建 cNFT

**使用 Bubblegum**
```typescript
import { createTree, mintV1 } from "@metaplex-foundation/mpl-bubblegum";

// 创建 Merkle 树
await createTree(umi, {
  merkleTree,
  maxDepth: 14,
  maxBufferSize: 64,
}).sendAndConfirm(umi);

// Mint cNFT
await mintV1(umi, {
  leafOwner: owner.publicKey,
  merkleTree: merkleTree.publicKey,
  metadata: {
    name: "My cNFT",
    uri: "https://arweave.net/...",
    sellerFeeBasisPoints: 500,
    collection: { key: collectionMint, verified: false },
    creators: [{ address: creator, verified: false, share: 100 }],
  },
}).sendAndConfirm(umi);
```

### 读取 cNFT

**需要索引服务**
由于数据不完全在链上，需要索引器：
- [Helius](https://learnblockchain.cn/tags/Helius?map=Solana)（最佳 cNFT 支持）
- SimpleHash
- Shyft

**API 查询**
```javascript
// Helius API
const response = await fetch(
  `https://mainnet.helius-rpc.com/?api-key=${API_KEY}`,
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-id',
      method: 'getAssetsByOwner',
      params: { ownerAddress: walletAddress },
    }),
  }
);
```

### 限制与权衡

**优点**
- 极低成本
- 可扩展性强
- 适合大规模发行

**缺点**
- 需要链下索引
- 查询比传统 NFT 复杂
- 钱包支持正在完善
- 转移需要 Merkle 证明

### 生态支持

**钱包**
- [Phantom](https://learnblockchain.cn/tags/Phantom?map=Solana)（支持）
- Backpack（支持）
- Solflare（支持）

**市场**
- Tensor（原生支持）
- Magic Eden（支持）

**工具**
- [Helius](https://learnblockchain.cn/tags/Helius?map=Solana)（最佳索引）
- [Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Solana) SDK

### 案例

**大规模采用**
- Mad Lads（10,000 cNFT 系列）
- Claynosaurz 宠物（数十万）
- 各种游戏项目

**成本节省**
铸造 100 万个 cNFT：
- 传统方式：约 $100,000
- cNFT：约 $100
- **节省 99.9%**

### 未来发展

**更广泛采用**
随着工具和支持完善，cNFT 将成为主流。

**新用例**
- 链上身份
- 社交图谱
- 大规模忠诚度计划

### 相关概念

- **Merkle 树**：cNFT 的数据结构基础
- **状态压缩**：核心技术原理
- **Bubblegum**：cNFT 程序
- **[Helius](https://learnblockchain.cn/tags/Helius?map=Solana)**：cNFT 索引领导者
- **传统 NFT**：每个 NFT 独立账户的标准方式
