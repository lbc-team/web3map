## Ordinals 协议

NFT主要在以太坊、Solana 和 BNB Smart Chain等区块链上进行铸造和使用。但是，Ordinals背后的团队认为，非同质化代币在**比特币区块链**上也应占有一席之地。这促进了Ordinals项目的面世。

Ordinals 协议可以理解为一个为聪（SATS）编号的系统。通过赋予每个聪一个序列号，然后再附加上额外的数据（文本、图片、代码等），也就是NFT中常说的“**元数据**”，使每个聪都变成独一无二的 **NFT**，这个过程称之为“铭刻”或“刻录”。根据 Ordinals 协议，聪的编号是根据它们**被开采的顺序**而定的。

虽然 Ordinals NFT 是通过Ordinals理论的概念化而真正解锁的，但今天存在的 Ordinals NFT是由比特币协议的**隔离见证**（SegWit）和**Taproot**更新得以实现的，这两个更新分别发生在2017年和2021年。

值得注意的是，这些更新并不是为了实现这些新型NFT的具体目的而进行的。但是，由于每次更新都扩大了区块内链上能够存储的任意数据量 -- 这意味着现在有空间来存储图像、视频，甚至游戏 -- 使得 Ordinal NFT 在命中注定而成为可能。

虽然传统NFT在某些方面与Ordinals相似，但也存在几个关键的区别。NFT通常使用**智能合约**在以太坊、Solana和BNB Smart Chain等区块链上进行制作，有时它们所代表的资产会被托管在其他地方。相反，Ordinals直接记录在单个聪上，然后被纳入比特币区块链的区块中。**Ordinals完全驻留在区块链上**，不需要侧链或单独的代币。从这层意义上说，Ordinals记录**继承了比特币本身的简单性、不变性、安全性和耐久性**。

## 顺序理论和记录

在比特币领域，顺序理论是一种拟议方法，通过序列号识别每个聪，并在比特币供应中追踪它们，从首次铸造开始，贯穿整个交易周期。这个过程称之为“记录”。所以，序数记录就是类似于NFT的数字资产，记录在比特币网络的单个聪上。2021年11月14日发布的[Taproot升级](https://learnblockchain.cn/tags/Taproot/)使这一进程得以实现。正因如此，序数记录不需要侧链或单独的代币。

顺序理论能够追踪和转移单个的聪，所以为聪的收集提供了可能性。根据比特币的总供应量，以下等级用来表示不同聪的稀有程度：

- 普通级：除区块第一个聪外的任何聪（总供应量为2100万亿）。
- 优良级：每个区块的第一个聪（总供应量为6929999）。
- 稀有级：每个难度调整期的第一个聪（总供应量为3437）。
- 史诗级：每次减半后的第一个聪（总供应量为32）。
- 传奇级：每个周期的第一个聪*（总供应量为5）。
- 神话级：创世区块的第一个聪（总供应量为1）。

*一个周期代表时间衔接的时期，当减半和难度调整重合时就会发生。理论上，这种情况每6次减半后就会发生一次，但第一次重合还没有发生（预计将在2032年发生）。

## 比特币NFT如何工作？

要了解 Ordinals NFT是如何工作的，重要的是要区分 "Ordinals（排序系统）" 和 "铭文（Inscriptions）"这两个术语，它们一起都是用来指这种新型的比特币NFT。

- **Ordinals 是一个系统**，用于以创建NFT所需的"非同质"属性的方式排序聪。

  > 每一个聪（聪包含在UTXO中）以他们被mint出来的顺序进行编号Orinal number， 转移时，按照先进先出规则，从交易的输入转移到输出。

- **铭文（Inscriptions）**是 Ordinals NFT **本身的内容** -- 图像、文本、视频或任何其他用户认为与NFT同义的任意数据。

同质化代币是可以互换的。比如你没办法区分两个不同的比特币，就像不可能区分一个美元和另一个美元一样。Ordinal NFT 的关键创新是，他们提供了一个系统来为每个聪编号。其结果是：比特币区块链上的每个 satoshi 都有一个唯一的ID。

在 Ordinal 理论中，单个聪是按照它们被开采的顺序来编号的。第一个序号是创世纪铸造的第一个聪，可以一直追溯到2008年。当一个**比特币被转移**时，通过基于交易顺序的先进先出系统，顺序被保留下来。

![Ordinals](https://img.learnblockchain.cn/web3map/Ordinals.png)

#### 元数据（Metadata）

在非比特币区块链中，元数据是可选的一部分，它是可附加到一个非同质化代币上任意数据。它被用来代表和展示大量的艺术、游戏中的资产、个人资料图片、金融资产等等，这些都已经成为 "NFT" 这个词的同义词。

#### 铭文（Inscription）作为元数据

Ordinal NFT 不像 非比特币NFT那样 有一个指定的元数据点（tokenURI）。相反， Ordinals NFT的元数据被保存在交易的见证数据中。

为了给一个特定的比特币刻上数据，并创建一个有顺序的NFT，用户必须将一些聪作为单独的比特币交易发送到一个与 Taproot 兼容的钱包，并将所需的元数据作为交易的一部分。他们还必须注意交易的顺序，以确保所需的聪币不会被用作网络费用。实现这一过程自动化的工具有助于消除这些风险，并使这一过程对非技术用户来说更加容易。

## Bitcoin Ordinals与NFT有何不同？

比特币 Ordinals 和更标准的NFT类型之间的关键区别是它们的流动性。因为比特币协议没有正式承认Ordinals理论，一个Ordinals可以是可替代的，也可以是非同质化的。这完全取决于谁拥有这个Ordinals，以及他们是否希望保留这单个聪。

例如，如果一个比特币用户不承认或不关心一个Ordinals或附加在它身上的数据，它可以简单地像其他比特币一样被使用。这样的话，Ordinals是可替换的 --它们可以被用来支付网络费用或作为付款发送，任意数据仍将被附加。以太坊NFT就不是这样了。以太坊NFT与以太坊同质币完全不同，不可能将可替换代币与NFT混为一谈，因为以太坊网络对每种代币类型的处理方式不同。

## 相关概念

1.[什么是NFT?](https://learnblockchain.cn/tags/NFT/)

2.[BRC-20](https://learnblockchain.cn/tags/BRC20/)

参考文章：

https://academy.binance.com/zh/articles/what-are-ordinals-an-overview-of-bitcoin-nfts?&utm_campaign=web_share_copy
