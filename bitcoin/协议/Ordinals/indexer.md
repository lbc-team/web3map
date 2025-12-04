# Ordinals Indexer

Ordinals Indexer 是一个专门为 Ordinals 协议设计的工具，它负责扫描、解析和存储比特币区块链上的数据，以便跟踪和查询“铭文（Inscriptions）”的所有权和状态。它是 Ordinals 生态系统正常运行的关键基础设施组件。

## 要解决的问题

比特币区块链本身并没有内建的机制来识别或管理“非同质化代币（NFT）”或“可替代代币”等复杂资产。比特币网络只关心 UTXO（未花费交易输出）的所有权和数量。当 Ordinals 协议允许用户在比特币的最小单位——聪（satoshi）上“铭刻”任意数据时，就需要一种方式来：

1.  **识别和跟踪铭文**：比特币客户端不会自动识别哪些聪包含了铭文数据，也不会跟踪这些铭文从一个用户转移到另一个用户时的所有权变化。
2.  **建立所有权链**：需要一个独立的系统来追踪特定铭文从创建到每次转移的历史，确保其唯一性和所有权的合法性。
3.  **提供查询服务**：用户和应用需要一个可靠的接口来查询特定的铭文、查找某地址拥有的铭文、或获取铭文的详细内容。

Ordinals Indexer 就是为了解决这些问题而生，它作为一个链下但可验证的账本，为 Ordinals 协议提供了必要的数据服务。

## 实现机制与原理

Ordinals Indexer 的核心原理是**全量扫描比特币区块链数据，并根据 Ordinals 协议的特定规则进行解析和索引**。

### 工作流程
1.  **同步比特币区块链**：Indexer 首先会运行一个完整的比特币核心节点（Bitcoin Core），并同步所有的区块数据。
2.  **扫描区块和交易**：Indexer 逐个处理每个比特币区块中的交易。
3.  **识别铭文**：当发现一个包含特定 `OP_RETURN` 输出或 Taproot Script Path Spend Script（使用 `OP_IF` 条件）的交易时，Indexer 会解析其中嵌入的铭文数据。
    *   铭文数据通常通过 Taproot 脚本路径的“信封（Envelope）”结构嵌入，以 `OP_FALSE OP_IF ... OP_ENDIF` 的形式封装任意数据，这使得铭文数据不会被比特币脚本引擎执行，但会永久记录在区块链上。
4.  **追踪聪的转移**：Ordinals 协议引入了“第一次输入，第一次输出（First-In, First-Out, FIFO）”的原则来追踪聪的流向。当一个比特币 UTXO 被花费时，其中包含的聪会按其被收到的顺序，分配给新的输出 UTXO。Indexer 会精确跟踪每个铭文所在的聪的转移。
5.  **构建索引数据库**：Indexer 将解析出的铭文数据、其所有者地址、位置（所在的 UTXO）、内容类型等信息存储在一个高性能的数据库中（通常是 RocksDB 或 PostgreSQL）。这个数据库就是 Ordinals 铭文的“账本”。

## 主要特点

*   **链下索引，链上溯源**：索引数据存储在链下，但其有效性可追溯到比特币主链上的铭刻交易。
*   **完全去中心化（理论上）**：任何人都可以运行自己的 Indexer 来验证和跟踪铭文，避免了对单一中心化服务的依赖。
*   **支持多种资产类型**：除了非同质化铭文（NFTs），也支持 BRC-20 等可替代代币协议，这些协议同样依赖 Ordinals Indexer 来追踪其余额和转移。
*   **严格遵循 Ordinals 规则**：Indexer 必须严格按照 Ordinals 协议的创世和转移规则来识别铭文，以确保共识和数据一致性。

## 推荐阅读

*   [Ordinals Handbook: Inscriptions](https://docs.ordinals.com/inscriptions.html)
*   [Ordinals Indexer GitHub Repository](https://github.com/ordinals/ordinals)
*   [BIP-342: Tapscript](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)

## 相关概念

*   **Ordinals 协议**
*   **聪 (Satoshi)**
*   **铭文 (Inscription)**
*   **BRC-20**
*   **Taproot**
*   **UTXO**
