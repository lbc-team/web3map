## NFT 是什么

NFT（非同质化代币，Non-Fungible Token）是一种基于区块链技术的数字资产，与传统的同质化代币（如比特币、以太币、USDT等 [Token](https://learnblockchain.cn/tags/Token?map=EVM) ）不同，NFT 是独一无二的，每一个 NFT 都具有唯一的标识符和元数据，无法互换。NFT 常用于表示数字艺术品、音乐、视频、游戏道具、虚拟地产等独特的数字资产。



### NFT 标准

在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)区块链（或 EVM 兼容链）上，NFT 通常遵循以下标准：

1. **[ERC-721](https://learnblockchain.cn/tags/ERC721?map=EVM)**：ERC-721 是最早的、最广泛使用的 NFT 标准，定义了一组基本接口和事件，用于管理和交易 NFT。
2. **[ERC-1155](https://learnblockchain.cn/tags/ERC1155?map=EVM)**：ERC-1155 是一种多代币标准，可以同时支持同质化代币和非同质化代币。这种标准在游戏和收藏品领域特别有用，因为它允许批量转移和高效的代币管理。

在其他链上有不同的标准，比特币上通过 Ordinals 协议定义 NFT ， 在 Solana 上，并不严格区分 NFT 与 同质Token， 而是统一使用 SPL Token 标准。 



### 如何创建 NFT

在 EVM 生态链上 创建 NFT 的过程通常包括以下步骤：

1. **编写智能合约**：
   - 使用 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 编写智能合约，定义 NFT 的属性和行为。
   
    以下是 ERC-721 智能合约示例：
   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.0;
   
   import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
   import "@openzeppelin/contracts/access/Ownable.sol";
   
   contract MyNFT is ERC721, Ownable {
       uint256 public nextTokenId;
       string private _baseTokenURI;
   
       constructor(string memory baseTokenURI) ERC721("MyNFT", "MNFT") {
           _baseTokenURI = baseTokenURI;
       }
   
       function mint() external onlyOwner {
           uint256 tokenId = nextTokenId;
           _mint(msg.sender, tokenId);
           nextTokenId++;
       }
   
       function _baseURI() internal view override returns (string memory) {
           return _baseTokenURI;
       }
   }
   ```

2. **部署智能合约**：
   - 使用 [Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM)、[Hardhat](https://learnblockchain.cn/tags/Hardhat?map=EVM) 等工具将智能合约部署到区块链上。

3. **铸造（Minting）NFT**：
   - 调用智能合约中的 `mint` 函数，创建新的 NFT 并将其分配给用户。

### 交易 NFT

NFT 的交易通常在去中心化的 NFT 市场上进行，如 OpenSea、Blur、MagicEden 等。交易过程如下：

1. **上架**：
   - 将 NFT 上架到市场，设置价格和销售条件。

2. **买卖**：
   - 买家浏览市场，选择并购买 NFT。交易通过智能合约完成。

3. **转移所有权**：
   - 一旦交易完成，NFT 的所有权从卖家转移到买家，交易记录将被永久记录在区块链上。



### 知名 NFT 项目

* **CryptoPunks** 是由 Larva Labs 创建的 10,000 个独特的 24x24 像素艺术角色。每个 CryptoPunk 都是独一无二的，并存储在以太坊区块链上。CryptoPunks 是最早的 NFT 项目之一，因其历史意义和稀缺性而备受收藏家青睐。
* **CryptoKitties** 是一款区块链养猫游戏，玩家可以收集、饲养和繁殖虚拟猫咪，每只猫咪都是独特的 NFT。CryptoKitties 是最早的 NFT 游戏之一，CryptoKitties 展示了区块链技术在游戏和收藏领域的潜力。
* **Bored Ape Yacht Club** 是由 Yuga Labs 创建的一系列 10,000 个独特的 Bored Ape NFT，每个猿猴都有不同的外观和特征。持有者不仅可以拥有独特的数字艺术品，还可以加入俱乐部，享受独家会员福利和活动。
* **Art Blocks** 是一个生成艺术平台，允许艺术家创建和销售基于算法生成的艺术作品。每件作品都是独一无二的，并在购买时生成。
* **Decentraland** 是一个基于区块链的虚拟现实平台，用户可以购买、开发和出售虚拟土地和资产。所有资产都以 NFT 形式存在。Decentraland 提供了一个完全由用户控制的虚拟世界，用户可以在其中创建和体验各种互动内容。
* **NBA Top Shot** 是由 Dapper Labs 开发的一个数字收藏品平台，允许用户购买、出售和交易 NBA 的精彩时刻（视频剪辑）。每个时刻都是一个 NFT，具有独特的稀缺性和收藏价值，受到了大量篮球迷的欢迎。
* **ENS** 是以太坊名称服务， 使用 NFT 来记录域名的所有权，并提供很好的交易方式。
* **Uniswap V3** 通过 NFT 来表示用户提供的独一无二的流动性。



### 未来展望

随着区块链技术的不断发展和应用场景的扩展，NFT 将在更多领域发挥重要作用，推动数字经济的发展和变革。NFT 的独特性和可编程性为创造新的商业模式和用户体验提供了无限可能。
