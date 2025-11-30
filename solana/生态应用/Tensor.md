## Tensor 概述

Tensor 是 Solana 生态中专业的 [NFT](https://learnblockchain.cn/tags/NFT) 交易平台,通过创新的 AMM 池和专业交易工具,为 [NFT](https://learnblockchain.cn/tags/NFT) 交易者提供深度流动性和极致交易体验。与传统 [NFT](https://learnblockchain.cn/tags/NFT) 市场的挂单模式不同,Tensor 引入了 [NFT](https://learnblockchain.cn/tags/NFT) AMM 机制,允许用户即时买卖 [NFT](https://learnblockchain.cn/tags/NFT),无需等待买家或卖家。作为 Solana [NFT](https://learnblockchain.cn/tags/NFT) 生态的核心基础设施,Tensor 处理着超过 60% 的 Solana [NFT](https://learnblockchain.cn/tags/NFT) 交易量,为专业交易者、收藏家和做市商提供最强大的 [NFT](https://learnblockchain.cn/tags/NFT) 交易工具。

**官网**: https://www.tensor.trade/

## 核心特性

### 1. NFT AMM 池

革命性的流动性机制:

- **即时交易**: 无需等待买卖双方匹配
- **深度流动性**: AMM 池提供持续流动性
- **价格发现**: 基于供需的自动定价
- **批量操作**: 一键买卖多个 NFT
- **MEV 保护**: 批量拍卖机制防抢跑

### 2. 专业交易工具

为高级用户设计:

- **高级图表**: 地板价、交易量、稀有度分析
- **实时通知**: 价格异动、listing 提醒
- **批量挂单**: 同时挂出多个 NFT
- **稀有度过滤**: 按特征和稀有度筛选
- **扫地板**: 一键扫描地板价 NFT

### 3. 低费率

最具竞争力的费率:

- **交易费用**: 0.5% (市场最低)
- **版税可选**: 可选择支付或不支付版税
- **Taker 费用**: 做市商返佣机制
- **TNSR 代币**: 质押可减免费用
- **无隐藏费用**: 透明的费用结构

## 工作原理

### 1. NFT AMM 机制

```
传统 NFT 市场:
用户 A 挂单 100 SOL → 等待 → 用户 B 购买
(可能等待数天甚至数周)

Tensor AMM:
用户 → AMM 池 (即时成交)
├─ 买入: 从池中提取 NFT,支付 SOL
└─ 卖出: 将 NFT 存入池,获得 SOL

AMM 定价公式:
价格 = 地板价 × (1 + 价格影响)
价格影响 = f(池中 NFT 数量, 交易数量)
```

### 2. 挂单与出价系统

灵活的交易方式:

**挂单 (Listing)**:
```
卖家设置价格 → 链上挂单
    ↓
买家看到挂单 → 接受价格购买
    ↓
即时成交,NFT 转移
```

**出价 (Bid)**:
```
买家出价 → 链上出价单
    ↓
卖家看到出价 → 接受出价卖出
    ↓
即时成交,SOL 转移
```

**集合出价 (Collection Bid)**:
```
买家对整个集合出价 → 任意 NFT 皆可成交
    ↓
卖家接受 → 根据稀有度调整价格
    ↓
公平成交
```

### 3. 交易聚合

最优价格发现:

```
Tensor 聚合多个来源:
├─ Tensor 挂单
├─ Magic Eden 挂单
├─ Tensor AMM 池
├─ 私人出价
└─ 其他市场

自动选择最优价格执行
```

## 实际应用

### 1. 买卖 NFT

基础交易操作:

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'
import { Connection, PublicKey } from '@solana/web3.js'

const connection = new Connection('https://api.mainnet-beta.solana.com')
const tensorClient = new TensorClient({ connection, wallet })

// 获取集合信息 (以 DeGods 为例)
const collectionId = new PublicKey('DeGods_Collection_Mint')
const collection = await tensorClient.getCollection(collectionId)

console.log('集合信息:')
console.log('地板价:', collection.floorPrice / 1e9, 'SOL')
console.log('交易量(24h):', collection.volume24h / 1e9, 'SOL')
console.log('上架数量:', collection.listedCount)

// 购买地板价 NFT
const buyTx = await tensorClient.buyNFT({
  collection: collectionId,
  maxPrice: collection.floorPrice * 1.05, // 允许 5% 滑点
})

console.log('购买成功:', buyTx.signature)

// 挂单卖出 NFT
const nftMint = new PublicKey('Your_NFT_Mint_Address')
const listTx = await tensorClient.listNFT({
  mint: nftMint,
  price: 150 * 1e9, // 150 SOL
})

console.log('挂单成功:', listTx.signature)
```

### 2. 批量交易

扫地板和批量挂单:

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'

const tensorClient = new TensorClient({ connection, wallet })

// 扫地板: 买入 10 个地板价 NFT
const sweepTx = await tensorClient.sweepFloor({
  collection: collectionId,
  count: 10, // 购买 10 个
  maxPricePerNFT: 100 * 1e9, // 每个最高 100 SOL
  maxTotalPrice: 950 * 1e9, // 总价最高 950 SOL
})

console.log('扫地板成功,购买了', sweepTx.nfts.length, '个 NFT')

// 批量挂单: 将所有 NFT 以地板价 +10% 挂出
const userNFTs = await tensorClient.getUserNFTs(wallet.publicKey, collectionId)
const floorPrice = (await tensorClient.getCollection(collectionId)).floorPrice

const bulkListTx = await tensorClient.bulkList({
  nfts: userNFTs.map(nft => ({
    mint: nft.mint,
    price: floorPrice * 1.1, // 地板价 +10%
  })),
})

console.log('批量挂单成功:', bulkListTx.signature)
```

### 3. 集合出价

对整个集合出价:

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'

const tensorClient = new TensorClient({ connection, wallet })

// 创建集合出价
const collectionBidTx = await tensorClient.createCollectionBid({
  collection: collectionId,
  price: 80 * 1e9, // 出价 80 SOL
  quantity: 5, // 愿意购买 5 个
  expiryTime: Date.now() + 7 * 24 * 3600 * 1000, // 7 天后过期
})

console.log('集合出价已创建:', collectionBidTx.signature)

// 特征出价: 只购买特定特征的 NFT
const traitBidTx = await tensorClient.createTraitBid({
  collection: collectionId,
  traits: {
    'Background': 'Gold',
    'Eyes': 'Laser',
  },
  price: 150 * 1e9, // 150 SOL
  quantity: 2,
})

console.log('特征出价已创建:', traitBidTx.signature)

// 查询我的出价
const myBids = await tensorClient.getUserBids(wallet.publicKey)
console.log('我的出价:', myBids)

// 取消出价
const cancelBidTx = await tensorClient.cancelBid({
  bidId: myBids[0].id,
})

console.log('出价已取消:', cancelBidTx.signature)
```

### 4. AMM 做市

创建和管理 NFT AMM 池:

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'

const tensorClient = new TensorClient({ connection, wallet })

// 创建 AMM 池
const createPoolTx = await tensorClient.createAMMPool({
  collection: collectionId,
  curveType: 'exponential', // 指数曲线
  delta: 5, // 每次价格变化 5%
  spotPrice: 90 * 1e9, // 起始价格 90 SOL
  depositNFTs: [nft1, nft2, nft3], // 存入 3 个 NFT
  depositSOL: 270 * 1e9, // 存入 270 SOL
})

console.log('AMM 池已创建:', createPoolTx.poolAddress)

// AMM 定价示例:
// 起始价格: 90 SOL
// Delta: 5%
// 买入价格:
//   第 1 个: 90 SOL
//   第 2 个: 90 * 1.05 = 94.5 SOL
//   第 3 个: 94.5 * 1.05 = 99.2 SOL
// 卖出价格:
//   第 1 个: 90 / 1.05 = 85.7 SOL
//   第 2 个: 85.7 / 1.05 = 81.6 SOL

// 管理 AMM 池
const pool = await tensorClient.getPool(createPoolTx.poolAddress)

console.log('池状态:')
console.log('NFT 数量:', pool.nftCount)
console.log('SOL 余额:', pool.solBalance / 1e9)
console.log('累计手续费:', pool.accumulatedFees / 1e9, 'SOL')

// 提取收益
const withdrawTx = await tensorClient.withdrawFromPool({
  pool: createPoolTx.poolAddress,
  withdrawNFTs: true,
  withdrawSOL: true,
})

console.log('已提取收益:', withdrawTx.signature)
```

### 5. 数据分析

获取市场数据和分析:

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'

const tensorClient = new TensorClient({ connection, wallet })

// 获取热门集合
const trendingCollections = await tensorClient.getTrendingCollections({
  period: '24h',
  limit: 10,
})

console.log('24h 热门集合:')
trendingCollections.forEach((col, index) => {
  console.log(`${index + 1}. ${col.name}`)
  console.log(`   地板价: ${col.floorPrice / 1e9} SOL`)
  console.log(`   交易量: ${col.volume24h / 1e9} SOL`)
  console.log(`   涨跌: ${col.change24h > 0 ? '+' : ''}${col.change24h}%`)
})

// 获取集合详细统计
const stats = await tensorClient.getCollectionStats(collectionId, {
  period: '7d',
})

console.log('7 天统计:')
console.log('交易量:', stats.volume / 1e9, 'SOL')
console.log('交易数:', stats.sales)
console.log('独立买家:', stats.uniqueBuyers)
console.log('独立卖家:', stats.uniqueSellers)
console.log('地板价变化:', stats.floorPriceChange, '%')

// 获取稀有度排名
const rarity = await tensorClient.getRarityRanking(collectionId)
const myNFT = new PublicKey('Your_NFT_Mint')

const myNFTRank = rarity.find(r => r.mint.equals(myNFT))
console.log('我的 NFT 稀有度排名:', myNFTRank.rank, '/', rarity.length)
console.log('稀有度得分:', myNFTRank.score)
```


## Tensor vs 其他 NFT 市场

| 特性 | Tensor | Magic Eden | [OpenSea](https://learnblockchain.cn/tags/OpenSea) |
|------|--------|-----------|---------|
| **区块链** | Solana | Multi-chain | Multi-chain |
| **交易费用** | 0.5% | 2% | 2.5% |
| **AMM 池** | ✅ 有 | ❌ 无 | ❌ 无 |
| **批量操作** | ✅ 强大 | ⚠️ 基础 | ⚠️ 基础 |
| **高级工具** | ✅ 专业 | ⚠️ 一般 | ⚠️ 一般 |
| **交易速度** | < 1s | < 1s | 10-60s |
| **[Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 费** | < $0.01 | < $0.01 | $10-100 |
| **目标用户** | 专业交易者 | 大众用户 | 大众用户 |

## TNSR 代币经济

### 代币效用

TNSR 代币用途:

- **费用折扣**: 质押 TNSR 减免交易费用
- **治理权**: 投票决定协议参数
- **收入分享**: 质押者分享协议收入
- **AMM 激励**: AMM 做市奖励
- **空投资格**: 持有者获得项目空投

### 质押收益

```typescript
import { TensorClient } from '@tensor-hq/tensor-sdk'

const tensorClient = new TensorClient({ connection, wallet })

// 质押 TNSR 代币
const stakeTx = await tensorClient.stakeTNSR({
  amount: 10000 * 1e9, // 质押 10,000 TNSR
  lockPeriod: 365, // 锁定 1 年
})

// 收益计算:
// 基础 APR: 15%
// 锁定加成: +5% (1 年锁定)
// 交易量加成: +3% (高交易量用户)
// 总 APR: 23%

console.log('预计年收益:', 10000 * 0.23, 'TNSR')
```


## 相关概念与技术

- **Solana**: 高性能区块链
- **[Metaplex](https://learnblockchain.cn/tags/Metaplex?map=Metaplex)**: Solana NFT 标准
- **[Magic Eden](https://learnblockchain.cn/tags/MagicEden?map=MagicEden)**: 综合 NFT 市场
- **[cNFT](https://learnblockchain.cn/tags/cNFT?map=cNFT)**: 压缩 NFT
- **[AMM](https://learnblockchain.cn/tags/AMM?map=AMM)**: 自动做市商

## 总结

Tensor 通过引入 NFT AMM 机制和专业交易工具,彻底改变了 Solana NFT 交易体验。其创新的 AMM 池为 NFT 提供了即时流动性,消除了传统挂单模式的等待时间,使 NFT 交易如同代币交易一样流畅。凭借 0.5% 的超低费率和强大的批量操作功能,Tensor 成为专业 NFT 交易者的首选平台,占据了 Solana NFT 市场 60% 以上的份额。基于 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 的高性能和低成本,Tensor 实现了毫秒级的交易体验和几乎可忽略的 Gas 费用。对于 NFT 交易者,Tensor 提供了深度流动性、精准数据分析和高级交易工具;对于做市商,AMM 池提供了稳定的收益来源。随着借贷、租赁、衍生品等新功能的推出,Tensor 将继续引领 NFT 交易创新,为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) NFT 生态注入更强活力。
