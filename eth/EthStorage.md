# EthStorage

## 什么是EthStorage？

**EthStorage 是一个去中心化的存储方案**，采用 key-value 的存储范式，与处于市场头部的去中心化存储解决项目 [Arweave](https://learnblockchain.cn/tags/Arweave) 和 [Filecoin](https://learnblockchain.cn/tags/Filecoin) 采用的静态文件的存储范式不同。得益于 key-value 的存储范式，**EthStorage 可以支持 CRUD**, 即创建新的存储数据，更新存储数据，读取存储数据和删除存储数据。这在中心化存储领域是很容易实现的，但是在去中心化存储领域目前只有 EthStorage 可以支持完整的 CRUD，究其原因，是因为更新的操作跟区块链的不可篡改的特性有冲突；为实现更新数据这一功能，EthStorage 实现了一种充满智慧的存储方案：KV 的存储范式结合定制的存储证明算法 ( EthStorage 的存储证明算法是 Pow 与 Proof-of-Random-Access 的结合体 )。

**EthStorage 完美兼容EVM**。兼容 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 的 EthStorage 可以给智能合约带来一个近乎完美的互操作性，这在其他的去中心化存储方案中是无法实现的。

**EthStorage 是以太坊的存储L2**。EthStorage 实际上采用的是类似 L2 的架构，在以太坊上会部署一个存储合约作为 EthStorage 的数据操作的入口；同时数据节点链下存储数据 (off chain storage data) 的证明也需要通过这个合约验证。当前的Op Rollup或ZK Rollup的扩容的方向是扩容以太坊的计算能力 ( 链下执行出新的状态树 ) ， 而 EthStorage [Rollup](https://learnblockchain.cn/tags/Rollup) 的扩容方向是**扩容以太坊存储数据能力**。

**EthStorage 的客户端是以太坊客户端 Geth 的超集**，这意味着运行 EthStorage 的节点的时候，依然可以正常参与以太坊的任何流程。当启动一个 EthStorage Node 的时候，实际上是运行着一个 Geth 和 Data Provider 的结合体，内部运行的 Geth 可以保证节点正常参与以太坊网络，例如，一个节点可以是以太坊的验证者节点的同时也是 EthStorage 的数据节点。每个 EthStorage Node 的 Data Provider 模块会跟其他 EthStorage Node 的 Data Provider 发起建立连接请求，当它们互相连接之后，实际上就构成了一个去中心化存储网络。

## EthStorage如何存读数据？

首先 EthStorage 会在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)主网上部署一个智能合约来支持 CRUD。

合约中每个方法的具体使用场景：

- put : 这是一个写数据的方法，调用这个方法会将你给出的数据 (data) 存储在我们对应的数据分片 (shard) 中，并且你可以在读取方法中通过对应的 key 读到它
- get :  这是一个查询方法，调用这个方法可以进行获取要查询的 key 的对应数据
- remove : 这是一个删除数据的方法，调用这个方法可以会删除 key 对应的数据
- verify: 这是一个验证方法，可以检查分片 (shard) 中存储的数据的数据哈希是否是跟合约内的数据哈希匹配，如果匹配证明链下存储的数据是正确的

**存储数据流程**：

应用写数据到 EthStorage 是通过调用合约中的`put(bytes32 key, bytes memory data)`方法进行的

我们在以太坊上部署一个智能合约，当用户在`put(bytes32 key, bytes memory data)`方法中填上任意的 key 和 data 之后，发起一笔以太坊交易调用这个方法，在等到交易执行成功时，合约内会记录这次写操作的 key，以及对应数据的数据哈希 (dataHash) 以及一个 EthStorage 分配的 kvIdx; 当 EthStorage 客户端监听到有 put 交易发生时，会根据数据被分配的 kvIdx 将数据存储在数据分片中对应的位置。

在这个调用过程中，用户所需要存储的 data 存储在 EthStorage 的网络中，这是一个以太坊的链下网络，而存储在链上智能合约中的数据仅有 key，datahash，kvIdx 三个值。

假设某个用户提交了一笔存储交易（调用 `put(key,data)`），并且被当前的提案区块所包含，当这个区块中的这笔交易进入虚拟机 (EVM) 中执行并且执行成功之后；以太坊世界状态中会记录下 key 以及要存储数据 和该数据的数据哈希 (dataHash)，同时给这个 key 分配一个 kvIdx。

当整个区块完全执行成功的时候，验证者若同时运行验证节点和数据节点，验证节点会根据正常流程更新自己的世界状态 ( 更新世界状态的过程中也在合约账户内更新最新存储的 key,data,dataHash)，然后数据节点会将内存中要存储的原数据 (data) 根据分配的 kvIdx 存储到对应数据分片 (shard) 的对应位置上。

**更新数据流程**：

当用户需要更新存储在 EthStorage 上的数据的时候，依然是通过发起一笔以太坊调用合约的交易，来执行 put 方法:

- **调用方法**

  `put( key , new_data )`

  key: 用户之前存储数据对应的 key

  new_data: 用户希望存储的新数据

- **执行流程**

  更新数据的执行流程跟存储数据流程基本差不多，具体如下:

  1. 用户发起一笔调用合约 put 方法的交易: `submit Tx{ put( key , new_data )}`;

  2. 这笔交易会将记录在合约中对应的 key 的哈希更新: `dataHash = hash(new_data)`；

  3. EthStorage 客户端 的 ShardManager 监听到有新的 put 交易发生，获取到 put 方法中携带的要更新的数据 new_data;

  4. ShardManager将要更新的数据进行mask后替换之前存储的数据：`store( kvIdx , mask(new_data))`

**验证数据**：

核心原理是 EthStorage 会在合约内记录  key  所对应数据的哈希，在每次进行随机访问证明 (Proof-of-Random-Access) 的时候会将矿工上传的数据进行哈希，然后与合约内存储的数据数据哈希进行验证，只有合约内存储的数据哈希和上传的数据哈希相等，随机访问证明才会生成一个有效的证明。

**读取数据**：

可以在对 EthStorage 合约中提供的 get(key) 方法进行本地调用，可以通过 key 找到对应的 kvIdx，然后根据 kvIdx 向数据节点发送读取请求，数据节点判断该 kvIdx 对应的数据是刚好在自己存储的数据分片中的时候，会向用户回复请求的数据；如果矿工没有存储对应数据，则会帮助用户转发读取数据的请求。

**删除数据**：

假设以下场景：

> KeyA 对应的 kvIdx 为 1 ，用户此时要将 KeyA 对应的数据移除；当前最大的 kvIdx 对应的键为 KeyB。

- 调用方法:`remove(key)`

  key: 你想要删除数据的索引 key

- 删除步骤：

  1. 发起一笔调用 remove 方法的交易: `submit Tx{remove(KeyA)}`;
  2. ShardManager 将 KeyB 对应的数据读出来之后，复制到 KeyA 的数据存储位置: `copy(chunkIdx(KeyA), readMasked(keyB))`;
  3. ShardManager 将 KeyB 的数据 ( chunk99 ) 删除: `delete(chunk99)`;
  4. 合约 将 KeyB 对应的 kvIdx 从 99 改为 1: `updateKvIdx(KeyB, 1)`;
  5. 合约 将 lastKVIdx 由 99 改为 98: `lastKvIdx =lastKvIdx - 1`; 

## EthStorage的未来应用

### On-Chain [NFT](https://learnblockchain.cn/tags/NFT)

目前的NFT都是将 Metadata 存放在 [Arweave](https://learnblockchain.cn/tags/Arweave) 和IPFS里面为主，仅仅将返回的内容Hash提交上链，这是因为将NFT元数据上链的话会特别贵，因为数据会占据较大的区块空间，所以之前的NFT，大多将元数据放在链下。

但是使用EthStorage的方案，用户可以将NFT的数据直接放在链上，通过智能合约来托管数据，并通过Web3 Access Protocol访问数据在前端渲染出来。相较之下，我们最常使用的NFT交易市场Opensea，它的前端所展示出来的NFT也并不是直接获取的元数据，而是将对应NFT的元数据存储在Opensea中心化的服务器里面，以此获得更高的访问体验。使用Ethstorage的方案，用户不仅能将NFT数据直接存在链上，而且可以通过前端直接获取到链上的NFT元数据，极大的改善了用户体验。

除了可以实现On-chain NFT之外，通过利用智能合约的可编程性实现一些动态NFT，三维NFT，以及NFT的组合，可编程性意味着有无限的可能，对于On-chain Game，链上NFT的可组合和可编程可以激发游戏的创造性，诞生更多的玩法。

### Personal Website

个人网站的数据通过智能合约把本地目录的所有数据上传，通过Web3 Access Protocol把本地目录映射成为[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)上面托管的文件系统，当用户想要访问相对路径和绝对路径的资源的时候，会通过calldata去访问到需要的数据内容。

### DeWeb

我们知道以太坊是一个去中心化的网络，在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)上面诞生了很多去中心化的Dapp，可这些Dapp并不是完全去中心化的，很多应用的前端依然是通过中心化的云服务在托管，像Uniswap的前端网页宕机，删除交易对以及Tornado.Cash因为涉嫌洗钱被监管而导致前端服务停用等都是因为其前端是托管在中心化的服务器上面，无法有效抗审查。但是使用EthStorage的方案，网页文件和数据被托管在智能合约中，由去中心化的网络共同运行和维护，使得抗审查性大大提高。通过[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)的可编程性实现DeWeb，可以实现很多有意思的应用，比如De-github，De-blog，以及各种dapp的前端。

### Modifiable Mirror

我们知道Mirror使用的是Arweave来进行数据的存储，而Arweave是一个数据永存的存储协议，用户通过Mirror创作的文章最终是存储在Arweave上面的，因为是永久存储和不可篡改的特性，意味着用户通过Mirror发布的文章是没办法在原来的基础上修改的，如果要修改需要将修改后的文章重新发起交易再存储到Arweave上面，这就造成了网络上数据的重复存储，且需要承担双倍的存储成本。但是选择使用EthStorage来构建类似Mirror的应用，用户可以通过Update的操作直接更新存储的数据而不用覆盖之前存储的数据。

***

节选文章：

https://literate-wolfsbane-bf0.notion.site/EthStorage-Ethereum-L2-003f3828c1c34341ac48fe494a30d71c