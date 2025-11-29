## The Graph 概述

The Graph 是一个去中心化的区块链数据索引和查询协议,旨在解决区块链数据访问的难题。它为开发者提供了一种高效的方式来索引、组织和查询区块链数据,使得构建数据密集型的去中心化应用([DApp](https://learnblockchain.cn/tags/DApp))变得简单高效。The Graph 通过 GraphQL API 提供数据服务,已成为 Web3 基础设施的重要组成部分,被称为"区块链的 Google"。

## The Graph 的核心概念

### 1. 子图(Subgraph)

子图是 The Graph 的核心组件:

- **数据定义**: 定义要索引的智能合约和事件
- **Schema**: 使用 GraphQL Schema 定义数据结构
- **Mapping**: 编写数据转换逻辑
- **部署**: 部署到去中心化网络
- **查询**: 通过 GraphQL 查询索引数据

### 2. Graph Node

运行索引服务的节点:

- **事件监听**: 监听区块链上的事件
- **数据提取**: 从区块链提取相关数据
- **数据转换**: 执行 Mapping 转换数据
- **数据存储**: 将数据存储到数据库
- **查询服务**: 响应 GraphQL 查询请求

### 3. 去中心化网络

The Graph 网络的参与者:

- **索引器(Indexer)**: 运行节点索引数据,获得奖励
- **策展人(Curator)**: 标识高质量子图,获得奖励
- **委托人(Delegator)**: 将 GRT 委托给索引器
- **开发者**: 创建子图并支付查询费用
- **消费者**: 使用子图数据的应用和用户

### 4. GRT 代币

The Graph 的原生代币:

- **查询费用**: 支付数据查询费用
- **索引奖励**: 奖励索引器和策展人
- **治理**: 参与协议治理
- **质押**: 索引器质押 GRT 参与网络

## The Graph 的工作原理

### 数据索引流程

1. **定义子图**: 开发者定义要索引的合约和事件
2. **部署子图**: 将子图部署到 The Graph 网络
3. **索引数据**: Graph Node 监听区块链并索引数据
4. **数据转换**: Mapping 函数转换原始数据
5. **存储数据**: 转换后的数据存储到数据库
6. **提供查询**: 通过 GraphQL API 提供查询服务

### GraphQL 查询

The Graph 使用 GraphQL 作为查询语言:

**优势**:
- **精确查询**: 只请求需要的字段
- **单次请求**: 一次请求获取多个资源
- **类型安全**: 强类型系统减少错误
- **实时文档**: 自动生成 API 文档
- **灵活高效**: 避免过度获取和不足获取

**查询示例**:
```graphql
{
  tokens(first: 10, orderBy: totalSupply, orderDirection: desc) {
    id
    name
    symbol
    totalSupply
    decimals
  }
}
```

## 创建子图

### 1. 安装 Graph CLI

```bash
npm install -g @graphprotocol/graph-cli
```

### 2. 初始化子图

```bash
graph init --product hosted-service username/subgraph-name
```

### 3. 定义 Schema

**schema.graphql**:
```graphql
type Token @entity {
  id: ID!
  name: String!
  symbol: String!
  decimals: Int!
  totalSupply: BigInt!
  holders: [Holder!]! @derivedFrom(field: "token")
}

type Holder @entity {
  id: ID!
  address: Bytes!
  balance: BigInt!
  token: Token!
}
```

### 4. 编写 Mapping

**src/mapping.ts**:
```typescript
import { Transfer } from "../generated/Token/Token"
import { Token, Holder } from "../generated/schema"

export function handleTransfer(event: Transfer): void {
  let token = Token.load(event.address.toHex())

  if (token == null) {
    token = new Token(event.address.toHex())
    token.name = "Token Name"
    token.symbol = "TKN"
    token.decimals = 18
    token.totalSupply = BigInt.fromI32(0)
  }

  // 更新发送者余额
  let sender = Holder.load(event.params.from.toHex())
  if (sender != null) {
    sender.balance = sender.balance.minus(event.params.value)
    sender.save()
  }

  // 更新接收者余额
  let receiver = Holder.load(event.params.to.toHex())
  if (receiver == null) {
    receiver = new Holder(event.params.to.toHex())
    receiver.address = event.params.to
    receiver.balance = BigInt.fromI32(0)
    receiver.token = token.id
  }
  receiver.balance = receiver.balance.plus(event.params.value)
  receiver.save()

  token.save()
}
```

### 5. 配置子图清单

**subgraph.yaml**:
```yaml
specVersion: 0.0.4
schema:
  file: ./schema.graphql
dataSources:
  - kind: ethereum
    name: Token
    network: mainnet
    source:
      address: "0x..."
      abi: Token
      startBlock: 12000000
    mapping:
      kind: ethereum/events
      apiVersion: 0.0.6
      language: wasm/assemblyscript
      entities:
        - Token
        - Holder
      abis:
        - name: Token
          file: ./abis/Token.json
      eventHandlers:
        - event: Transfer(indexed address,indexed address,uint256)
          handler: handleTransfer
      file: ./src/mapping.ts
```

### 6. 部署子图

```bash
# 代码生成
graph codegen

# 构建
graph build

# 部署到 Hosted Service
graph deploy --product hosted-service username/subgraph-name

# 部署到去中心化网络
graph deploy --node https://api.thegraph.com/deploy/ subgraph-name
```

## 查询子图数据

### 使用 GraphQL Playground

在浏览器中访问子图 URL:
```
https://api.thegraph.com/subgraphs/name/username/subgraph-name
```

### 在应用中集成

**使用 Apollo Client**:
```typescript
import { ApolloClient, InMemoryCache, gql } from '@apollo/client'

const client = new ApolloClient({
  uri: 'https://api.thegraph.com/subgraphs/name/username/subgraph-name',
  cache: new InMemoryCache()
})

const GET_TOKENS = gql`
  query GetTokens {
    tokens(first: 10, orderBy: totalSupply, orderDirection: desc) {
      id
      name
      symbol
      totalSupply
    }
  }
`

const { data } = await client.query({ query: GET_TOKENS })
```

**使用 fetch**:
```javascript
const query = `
  {
    tokens(first: 10) {
      id
      name
      symbol
    }
  }
`

const response = await fetch('https://api.thegraph.com/subgraphs/name/username/subgraph-name', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query })
})

const data = await response.json()
```

## The Graph 网络

### 去中心化网络 vs Hosted Service

|特性|去中心化网络|Hosted Service|
|---|---|---|
|去中心化|完全去中心化|中心化服务|
|费用|需支付 GRT|免费(已停止新子图)|
|可靠性|更高|依赖单点|
|审查抵抗|是|否|
|迁移|推荐|逐步淘汰|

### 网络参与者

**索引器**:
- 运行 Graph Node
- 质押 GRT
- 索引子图数据
- 获得查询费用和索引奖励

**策展人**:
- 标识优质子图
- 质押 GRT 信号
- 获得查询费用分成

**委托人**:
- 将 GRT 委托给索引器
- 不需要运行节点
- 获得部分索引奖励

## 支持的区块链

The Graph 支持多个区块链:

- **[以太坊](https://learnblockchain.cn/tags/以太坊?map=[EVM](https://learnblockchain.cn/tags/EVM?map=EVM))**: Mainnet、Goerli、Sepolia
- **Polygon**: Mainnet、Mumbai
- **Arbitrum**: One、Nova
- **Optimism**: Mainnet
- **Avalanche**: C-Chain
- **Celo**: Mainnet
- **BNB Chain**: Mainnet
- **Gnosis Chain**: Mainnet

## 高级特性

### 1. 实体关系

定义实体间的关系:

```graphql
type User @entity {
  id: ID!
  posts: [Post!]! @derivedFrom(field: "author")
}

type Post @entity {
  id: ID!
  author: User!
  content: String!
}
```

### 2. 全文搜索

添加全文搜索功能:

```graphql
type Article @entity {
  id: ID!
  title: String! @fulltext(name: "articleSearch", language: en)
  content: String! @fulltext(name: "articleSearch", language: en)
}
```

查询:
```graphql
{
  articleSearch(text: "blockchain") {
    id
    title
  }
}
```

### 3. 时间旅行查询

查询历史状态:

```graphql
{
  tokens(block: { number: 15000000 }) {
    id
    totalSupply
  }
}
```

### 4. 订阅

实时数据更新:

```graphql
subscription {
  transfers(orderBy: blockNumber, orderDirection: desc) {
    from
    to
    value
  }
}
```

## 最佳实践

### 1. Schema 设计

- **规范化**: 避免数据冗余
- **索引**: 为常查询字段添加索引
- **命名**: 使用清晰的实体和字段名
- **类型**: 选择合适的数据类型

### 2. Mapping 优化

- **批量处理**: 减少数据库操作
- **条件检查**: 避免不必要的操作
- **错误处理**: 妥善处理异常情况
- **[Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 优化**: 优化链上数据读取

### 3. 查询优化

- **分页**: 使用 first 和 skip 分页
- **过滤**: 减少返回数据量
- **排序**: 合理使用 orderBy
- **缓存**: 利用客户端缓存

## 监控与调试

### Graph Explorer

- **查询统计**: 查看查询次数和费用
- **索引状态**: 监控索引进度
- **错误日志**: 查看错误信息
- **性能分析**: 分析查询性能

### 本地开发

使用 Graph Node 本地开发:

```bash
git clone https://github.com/graphprotocol/graph-node
cd graph-node/docker
docker-compose up
```

## 应用场景

- **[DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM)**: 交易历史、流动性数据、价格信息
- **[NFT](https://learnblockchain.cn/tags/NFT)**: 所有权追踪、交易历史、稀有度分析
- **DAO**: 提案、投票、治理数据
- **游戏**: 游戏资产、玩家数据、排行榜
- **分析**: 链上数据分析和可视化

## 相关概念与技术

- **[GraphQL](https://graphql.org/)**: The Graph 使用的查询语言
- **[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)**: 主要支持的区块链
- **[IPFS](https://ipfs.io/)**: 去中心化存储,The Graph 也支持
- **Dune Analytics**: 另一个区块链数据分析平台

## 总结

The Graph 通过提供高效的区块链数据索引和查询服务,解决了 [DApp](https://learnblockchain.cn/tags/DApp) 开发中数据访问的痛点。其去中心化的架构、灵活的 GraphQL 查询和丰富的生态系统,使其成为 Web3 基础设施的关键组成部分。无论是 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议、[NFT](https://learnblockchain.cn/tags/NFT) 市场还是链上分析工具,The Graph 都提供了强大的数据支持。随着更多区块链的集成和网络的不断完善,The Graph 将继续在 Web3 数据层发挥重要作用。
