## Phoenix 概述

Phoenix 是 Solana 生态中首个完全链上的中央限价订单簿 (CLOB) DEX,为专业交易者提供与中心化交易所相媲美的交易体验。与传统 AMM 不同,Phoenix 采用订单簿模式,支持限价单、市价单等多种订单类型,提供精确的价格控制和深度流动性。通过 Solana 的高性能和低延迟优势,Phoenix 实现了完全链上的订单撮合,无需依赖中心化服务器,真正做到去中心化、透明、自托管。

**官网**: https://phoenix.trade/

## 核心特性

### 1. 中央限价订单簿 (CLOB)

专业的交易机制:

- **价格优先**: 最优价格优先成交
- **时间优先**: 同价格按时间先后成交
- **精确控制**: 设置精确的买入卖出价格
- **深度展示**: 完整的订单簿深度可视化
- **订单类型**: 限价单、市价单、IOC、POST_ONLY 等

### 2. 完全链上

真正的去中心化:

- **链上撮合**: 订单撮合在链上完成
- **无中介**: 无需托管资金到中心化服务器
- **透明可审计**: 所有订单和交易链上可查
- **抗审查**: 无法被关闭或冻结
- **自托管**: 用户完全控制自己的资产

### 3. 高性能优化

充分利用 Solana 优势:

- **低延迟**: 订单提交和成交 < 1 秒
- **高吞吐**: 支持每秒数千笔交易
- **低成本**: 每笔交易手续费 < $0.01
- **即时结算**: 无需等待区块确认
- **批量处理**: 支持批量挂单和撤单

## 工作原理

### 1. 订单簿结构

```
订单簿数据结构:

卖单 (Asks) - 按价格从低到高排列
┌─────────────────────────────┐
│ 价格    数量    累计         │
│ $25.10  100    100          │  ← 最低卖价 (Best Ask)
│ $25.12  200    300          │
│ $25.15  500    800          │
└─────────────────────────────┘

当前市价: $25.08

┌─────────────────────────────┐
│ 价格    数量    累计         │
│ $25.05  300    300          │  ← 最高买价 (Best Bid)
│ $25.03  150    450          │
│ $25.00  250    700          │
└─────────────────────────────┘
买单 (Bids) - 按价格从高到低排列
```

### 2. 订单匹配流程

```
用户提交订单 → Phoenix 程序
    ↓
检查订单有效性
    ↓
计算可成交数量
    ↓
从订单簿匹配对手单
    ↓
执行交易,更新余额
    ↓
未成交部分挂单到订单簿
    ↓
发出成交事件
```

### 3. Maker-Taker 模型

费用激励机制:

```
Maker (挂单者):
- 提交限价单,增加订单簿深度
- 费用: -0.02% (获得返佣)
- 例: 挂单买入 100 SOL,获得 0.02 SOL 返佣

Taker (吃单者):
- 提交市价单,消耗订单簿流动性
- 费用: 0.05%
- 例: 市价买入 100 SOL,支付 0.05 SOL 手续费

净效果: Maker 补贴 = Taker 费用的 40%
```

## 实际应用

### 1. 基础交易

使用 Phoenix SDK 进行交易:

```typescript
import { PhoenixClient } from '@ellipsis-labs/phoenix-sdk'
import { Connection, Keypair, PublicKey } from '@solana/web3.js'

const connection = new Connection('https://api.mainnet-beta.solana.com')
const wallet = Keypair.fromSecretKey(/* 你的密钥 */)

// 初始化 Phoenix 客户端
const phoenixClient = await PhoenixClient.create({
  connection,
  wallet,
})

// 获取 SOL/USDC 市场
const marketPubkey = new PublicKey('4DoNfFBfF7UokCC2FQzriy7yHK6DY6NVdYpuekQ5pRgg')
const market = await phoenixClient.getMarket(marketPubkey)

console.log('市场信息:', market.marketConfig)

// 限价买单: 以 $25.00 买入 10 SOL
const limitBuyOrder = await phoenixClient.placeLimitOrder({
  market: marketPubkey,
  side: 'Bid', // 买单
  price: 25.0,
  size: 10.0,
  orderType: 'Limit',
})

console.log('限价买单已提交:', limitBuyOrder.signature)

// 市价卖单: 立即卖出 5 SOL
const marketSellOrder = await phoenixClient.placeMarketOrder({
  market: marketPubkey,
  side: 'Ask', // 卖单
  size: 5.0,
})

console.log('市价卖单已成交:', marketSellOrder.signature)
```

### 2. 高级订单类型

使用不同的订单策略:

```typescript
import { PhoenixClient, OrderType } from '@ellipsis-labs/phoenix-sdk'

const phoenixClient = await PhoenixClient.create({ connection, wallet })
const market = new PublicKey('4DoNfFBfF7UokCC2FQzriy7yHK6DY6NVdYpuekQ5pRgg')

// 1. POST_ONLY 订单 (只做 Maker)
// 如果会立即成交则取消,确保获得 Maker 返佣
const postOnlyOrder = await phoenixClient.placeLimitOrder({
  market,
  side: 'Bid',
  price: 25.0,
  size: 10.0,
  orderType: 'PostOnly', // 不会吃单
})

// 2. IOC 订单 (Immediate Or Cancel)
// 立即成交,未成交部分取消(不挂单)
const iocOrder = await phoenixClient.placeLimitOrder({
  market,
  side: 'Ask',
  price: 25.1,
  size: 10.0,
  orderType: 'ImmediateOrCancel', // 不留挂单
})

// 3. FOK 订单 (Fill Or Kill)
// 全部成交或全部取消
const fokOrder = await phoenixClient.placeLimitOrder({
  market,
  side: 'Bid',
  price: 25.0,
  size: 100.0,
  orderType: 'FillOrKill', // 全部或无
})

console.log('高级订单已提交')
```

### 3. 查询订单簿和深度

获取市场数据:

```typescript
import { PhoenixClient } from '@ellipsis-labs/phoenix-sdk'

const phoenixClient = await PhoenixClient.create({ connection, wallet })
const marketPubkey = new PublicKey('4DoNfFBfF7UokCC2FQzriy7yHK6DY6NVdYpuekQ5pRgg')

// 获取订单簿
const orderbook = await phoenixClient.getOrderbook(marketPubkey)

console.log('订单簿深度:')
console.log('卖单 (Asks):')
orderbook.asks.forEach((level, index) => {
  if (index < 5) { // 显示前 5 档
    console.log(`  价格: ${level.price}, 数量: ${level.size}`)
  }
})

console.log('买单 (Bids):')
orderbook.bids.forEach((level, index) => {
  if (index < 5) {
    console.log(`  价格: ${level.price}, 数量: ${level.size}`)
  }
})

// 获取最优买卖价
const bestBid = orderbook.bids[0]?.price || 0
const bestAsk = orderbook.asks[0]?.price || 0
const spread = bestAsk - bestBid
const spreadBps = (spread / bestBid) * 10000

console.log('市场统计:')
console.log('最优买价:', bestBid)
console.log('最优卖价:', bestAsk)
console.log('买卖价差:', spread, `(${spreadBps.toFixed(2)} bps)`)

// 获取市场深度
const depth = {
  bids: orderbook.bids.slice(0, 10).reduce((sum, level) => sum + level.size, 0),
  asks: orderbook.asks.slice(0, 10).reduce((sum, level) => sum + level.size, 0),
}

console.log('前10档深度:')
console.log('买单总量:', depth.bids, 'SOL')
console.log('卖单总量:', depth.asks, 'SOL')
```

### 4. 做市策略

实现简单的做市机器人:

```typescript
import { PhoenixClient } from '@ellipsis-labs/phoenix-sdk'

const phoenixClient = await PhoenixClient.create({ connection, wallet })
const market = new PublicKey('4DoNfFBfF7UokCC2FQzriy7yHK6DY6NVdYpuekQ5pRgg')

// 做市配置
const config = {
  spread: 0.1, // 0.1% 价差
  orderSize: 5.0, // 每单 5 SOL
  levels: 3, // 3 档挂单
  tickSize: 0.01, // 价格档位
}

// 获取当前中间价
const orderbook = await phoenixClient.getOrderbook(market)
const midPrice = (orderbook.bids[0].price + orderbook.asks[0].price) / 2

// 取消现有订单
const openOrders = await phoenixClient.getOpenOrders(market)
for (const order of openOrders) {
  await phoenixClient.cancelOrder({ market, orderId: order.orderId })
}

// 双边挂单
const orders = []

for (let i = 0; i < config.levels; i++) {
  // 买单价格递减
  const bidPrice = midPrice * (1 - config.spread / 100) - i * config.tickSize
  const bidOrder = phoenixClient.placeLimitOrder({
    market,
    side: 'Bid',
    price: bidPrice,
    size: config.orderSize,
    orderType: 'PostOnly',
  })
  orders.push(bidOrder)

  // 卖单价格递增
  const askPrice = midPrice * (1 + config.spread / 100) + i * config.tickSize
  const askOrder = phoenixClient.placeLimitOrder({
    market,
    side: 'Ask',
    price: askPrice,
    size: config.orderSize,
    orderType: 'PostOnly',
  })
  orders.push(askOrder)
}

await Promise.all(orders)
console.log('做市订单已挂出:', orders.length, '个')

// 定期更新订单(每 30 秒)
setInterval(async () => {
  // 重新计算价格并更新订单...
}, 30000)
```


## Phoenix vs 其他 DEX

| 特性 | Phoenix | Raydium (AMM) | OpenBook (CLOB) |
|------|---------|---------------|-----------------|
| **交易机制** | 订单簿 | AMM 池 | 订单簿 |
| **价格控制** | ✅ 精确 | ❌ 滑点 | ✅ 精确 |
| **流动性深度** | 可见 | 池深度 | 可见 |
| **Maker 返佣** | ✅ -0.02% | ❌ 无 | ✅ -0.03% |
| **订单类型** | 多样 | 仅市价 | 多样 |
| **完全链上** | ✅ 是 | ✅ 是 | ✅ 是 |
| **适合场景** | 专业交易 | 散户交易 | 全场景 |

## 生态集成

### 1. DEX 聚合器

Phoenix 流动性聚合:

- **Jupiter**: 聚合 Phoenix 订单簿流动性
- **Mango Markets**: 集成 Phoenix 现货市场
- **1inch**: 跨链聚合 Phoenix 流动性

### 2. 交易工具

专业交易接口:

- **TradingView 集成**: 图表和技术分析
- **API 接口**: REST 和 WebSocket API
- **交易机器人**: 支持策略交易和做市
- **移动端**: iOS/Android 应用

### 3. 钱包支持

主流钱包集成:

- **[Phantom](https://learnblockchain.cn/tags/Phantom?map=Solana)**: 浏览器插件钱包
- **Backpack**: 集成 Phoenix 交易界面
- **Solflare**: 支持 Phoenix 订单管理


## 相关概念与技术

- **Solana**: 高性能区块链
- **[CLOB](https://www.investopedia.com/terms/c/central-limit-order-book.asp)**: 中央限价订单簿
- **[OpenBook](https://learnblockchain.cn/tags/OpenBook?map=OpenBook)**: Serum 继任者
- **[Jupiter](https://learnblockchain.cn/tags/Jupiter?map=Jupiter)**: DEX 聚合器
- **[做市商](https://www.investopedia.com/terms/m/marketmaker.asp)**: 提供流动性的交易者

## 总结

Phoenix 作为 Solana 生态中首个完全链上的 CLOB DEX,为专业交易者带来了与中心化交易所相媲美的交易体验。通过订单簿机制,Phoenix 提供精确的价格控制、深度流动性展示和多样化的订单类型,满足高频交易、做市等专业需求。相比 AMM 模式,Phoenix 的订单簿设计消除了滑点问题,并通过 Maker 返佣激励流动性提供者。基于 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 的高性能和低成本,Phoenix 实现了真正的完全链上撮合,无需依赖中心化服务器,保证了去中心化、透明和自托管。对于追求精确价格控制和专业交易工具的用户,Phoenix 提供了理想的链上交易解决方案。随着永续合约、期权等衍生品的推出,Phoenix 将继续丰富 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) DeFi 生态,为去中心化交易树立新的标杆。
