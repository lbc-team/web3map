# Taproot

## 介绍

Taproot是比特币网络的一次升级，于2021年11月14日上线。自SegWit（隔离见证）问世以来，Taproot与Schnorr签名一直是备受期待的比特币技术升级。Taproot旨在改变比特币脚本的运作方式，提升私密性、可扩展性与安全性。Taproot与名为Schnorr签名的相关升级结合后，将有望实现上述目标及更多计划。

## 什么是比特币Taproot升级？

Taproot是一次优化比特币脚本的软分叉，提升私密性、效率以及网络处理智能合约的能力。这是自2017年SegWit升级之后，公认的比特币重大升级。

在不可能三角中，Taproot升级主要应对了两个方面。一个是进一步提高匿名性能力，也就是进一步提升安全性；另一个是期望通过改变区块本身的数据结构来提升交易性能，减少交易中不必要的数据负担。

![不可能三角](../graph/%E4%B8%8D%E5%8F%AF%E8%83%BD%E4%B8%89%E8%A7%92.png)

Taproot升级由3项不同的比特币改进提案(BIP)组成，其中包括：**Taproot**、**Tapscript**及其核心，即名为“**Schnorr签名**”的全新数字签名方案。Taproot旨在为比特币用户带来诸多好处，例如**提升交易私密性和降低交易费用**。还将让比特币执行更多复杂的交易，从而拓宽用例，与以太坊一较高下，尤其是智能合约功能和网络对[去中心化金融(DeFi)](https://academy.binance.com/en/glossary/defi)和[非同质化代币(NFT)](https://academy.binance.com/en/glossary/non-fungible-token-nft)的支持。

Taproot提案最初由Bitcoin Core开发者Greg Maxwell在2018年1月提出。2020年10月，Pieter Wuille创建代码拉取请求，将Taproot并入Bitcoin Core代码库。为了全面部署升级，节点运行者须采用Taproot的全新共识规则。该提案最终得到90%的矿工支持，并于**2021年11月14日在区块709,632中正式激活**。

## Taproot如何运作？

### Schnorr签名(BIP340)

Schnorr签名**提高了比特币网络验证交易的速度和安全性**。该签名由[密码学](https://academy.binance.com/zh/articles/history-of-cryptography)签名方案组成，开发者是德国数学家兼密码学家Claus Schnorr。多年来，Schnorr的算法始终受专利保护，但该专利于2008年正式过期。Schnorr签名优点众多，尤其在短签名生成方面，以简洁高效著称。

比特币创始人中本聪采用的签名方案称为“椭圆曲线数字签名算法(ECDSA)”。选择ECDSA而非Schnorr签名算法是因为前者使用广泛、易于理解、安全稳定、轻量并且开源。

然而，Schnorr数字签名计划(SDSS)的推进可能是比特币与其他区块链网络应用新一代签名技术的起点。

Schnorr签名的一大核心优势是**可以在复杂的比特币交易中提取多组密钥，生成独一无二的签名**。因此，交易中各方的签名可整合为单一的Schnorr签名，这个过程称为“**签名聚合**”。

实际上，Taproot可以让人完全看不出来比特币脚本在运行。例如，采用Taproot后，无论是闪电网络通道交易、点对点交易还是通过复杂的智能合约交易，不同比特币支付方式看起来毫无差别。这些交易的监控者看到的只有点对点交易。然而，值得注意的是，这并未改变发送者与最终接收者的钱包信息暴露于外的事实。

![聚合签名](../graph/%E8%81%9A%E5%90%88%E7%AD%BE%E5%90%8D.png)

### Taproot (BIP341)

Taproot因Taproot升级而得名，其**创建基础是2017年的SegWit升级**，并使用**默克尔化替代脚本树**(MAST)来**扩展比特币区块链中的交易数据量**。

比特币网络中的交易由公钥和私钥保护。如需支付钱包中的数字资产，用户需先提供签名证明自己的真实所有者身份，才能转移代币。除了单一签名交易，比特币网络中的交易还可通过释放[时间锁](https://academy.binance.com/en/glossary/hashed-timelock-contract)、要求[多重签名(multisig)](https://academy.binance.com/zh/articles/what-is-a-multisig-wallet)等功能来提升复杂度。 

然而，复杂的多重签名交易需要多次输入和签名验证，会给区块链增加巨大数据量，拖慢交易速度。并且，交易信息在区块链中自动显示，会暴露地址所有者的敏感数据。 

MAST集成后，**单个MAST交易即可代表多个脚本**，从而可减少所需脚本和验证的数量。复杂比特币交易发送到MAST后，并不需要默克尔树来处理交易。MAST仅允许将交易的执行条件提交到区块链，而不是发送所有的细节。这将大幅降低网络所需存储的数据量。这不仅提高了比特币区块链的可扩展性和效率，还让比特币用户享有更高的私密性。

### Tapscript (BIP342)

Tapscript是**升级到比特币脚本的编程语言**，为另外2项比特币改进提案(BIP)提供便利。它是一系列**操作码**的集合，是用于指定如何执行交易的指令。区块的可用空间变多，新功能会更加灵活，可促进比特币网络在未来支持和创建智能合约。

## Taproot如何让比特币受益？

正如前文讨论所述，Taproot可显著提升比特币的私密性并拓宽用例。其他潜在优势还包括：

1.**通过降低区块链中传输与存储的数据量来改善网络可扩展性**；

2.**每个区块处理更多交易**（提升[每秒交易量(TPS)](https://academy.binance.com/en/glossary/transactions-per-second-tps)速率）；

3.**削减交易费用**。

Taproot的另一项优势是**移除了签名延展性**，这是比特币网络中的一项已知安全风险。简而言之，从技术角度出发，签名延展性是指交易确认前，签名可以修改。通过这种手段，攻击者可伪造出交易从未发生过的假象。这会让比特币暴露于臭名昭著的[双花问题](https://academy.binance.com/zh/articles/double-spending-explained)之下，有损分布式账本的公正性。

## Taproot升级为何重要？

激活Taproot可提升比特币网络功能，促成快速可靠的交易。在Taproot之前，比特币协议的发展仍处于Layer 1阶段，而以太坊等其他协议已在Layer 2和DApp方面抢占先机。升级后，比特币开启智能合约部署、拓展用例，迎头赶上NFT和DeFi市场的未来潮流趋势。 

随着比特币网络效率提高，费用降低，其交易数量和应用范围都将受到拉动。此外，比特币还保障了用户交易私密性，成为市场中更具竞争力的隐私币。

***

参考文章：https://academy.binance.com/zh/articles/what-is-taproot-and-how-it-will-benefit-bitcoin?&utm_campaign=web_share_copy
