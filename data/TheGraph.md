## The Graph

[The Graph](https://thegraph.com/zh/) 是一个去中心化的索引协议，专门用于查询区块链数据。它使开发者能够通过创建和使用“子图”（Subgraph），快速高效地查询和访问区块链上的数据，尤其是去中心化应用程序（[DApps](https://learnblockchain.cn/tags/DApp)）中的数据。The Graph 的设计目标是解决区块链数据访问的困难，特别是在链上数据复杂、实时性要求高的应用场景，如去中心化金融（[DeFi](https://learnblockchain.cn/tags/DEFi)）和 [NFT](https://learnblockchain.cn/tags/NFT) 市场等。

### The Graph 主要概念

1. **子图（Subgraph）**：子图是 The Graph 的核心组成部分，是一种定义和索引特定区块链数据的方式。开发者通过编写子图的模式来指定哪些智能合约、事件和函数需要被索引，并定义如何提取这些数据。子图可以被任何应用查询，提供快速的数据访问。

2. **Graph Node**：Graph Node 是 The Graph 网络中的核心组件，它负责从区块链中监听区块、提取数据、执行索引，并将数据存储在可查询的数据库中。Graph Node 可以从 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 和其他兼容区块链中抓取数据。

3. **GraphQL**：The Graph 使用 GraphQL 作为查询语言。GraphQL 是一种灵活的 API 查询语言，允许用户通过定义明确的数据结构和需求，精确查询子图中所需的数据。这种机制极大提高了查询效率。

4. **去中心化网络**：The Graph 最终目标是构建一个去中心化的网络，通过运行节点的索引者（Indexers）、提供查询的提供者（Curators）和验证者（Delegators）来共同维护整个网络。用户通过支付 GRT 代币来获取数据查询服务，索引者和提供者则通过提供服务获得激励。

### The Graph 的工作原理

1. **数据索引**：开发者在创建子图时，定义需要从区块链上索引的数据。这些定义包括合约地址、事件和函数，以及如何提取和组织这些数据。Graph Node 会根据这些定义自动抓取区块链中的数据，并将其存储在可索引的数据库中。

2. **查询数据**：一旦数据被索引，用户可以使用 GraphQL 来查询子图中的数据。由于 GraphQL 的灵活性，用户只需请求他们关心的字段，而不需要获取不必要的信息。这种方法大大提高了查询的效率和响应速度。

3. **去中心化查询和激励机制**：在 The Graph 网络的去中心化版本中，索引者和查询提供者通过运行 Graph Node 来索引和提供数据服务。索引者通过质押 GRT 代币获得查询任务，验证者通过委托他们的 GRT 参与网络安全，并获得相应的奖励。

4. **子图市场**：子图是公开的，任何人都可以使用现有的子图或创建自己的子图。开发者可以发布他们的子图供社区使用，或者通过自定义子图满足特定应用的数据需求。

