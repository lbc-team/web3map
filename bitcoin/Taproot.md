# Taproot

## 介绍

Taproot是比特币网络的一次升级，于2021年11月14日上线。自SegWit（隔离见证）问世以来，Taproot与Schnorr签名一直是备受期待的比特币技术升级。Taproot旨在改变比特币脚本的运作方式，提升私密性、可扩展性与安全性。Taproot与名为Schnorr签名的相关升级结合后，将有望实现上述目标及更多计划。

## 什么是比特币Taproot升级？

Taproot是一次优化比特币脚本的软分叉，提升私密性、效率以及网络处理智能合约的能力。这是自2017年SegWit升级之后，公认的比特币重大升级。

Taproot升级由3项不同的比特币改进提案(BIP)组成，其中包括：**Taproot**、**Tapscript**及其核心，即名为“**Schnorr签名**”的全新数字签名方案。Taproot旨在为比特币用户带来诸多好处，例如**提升交易私密性和降低交易费用**。还将让比特币执行更多复杂的交易，从而拓宽用例，与以太坊一较高下，尤其是智能合约功能和网络对[去中心化金融(DeFi)](https://academy.binance.com/en/glossary/defi)和[非同质化代币(NFT)](https://academy.binance.com/en/glossary/non-fungible-token-nft)的支持。

Taproot提案最初由Bitcoin Core开发者Greg Maxwell在2018年1月提出。2020年10月，Pieter Wuille创建代码拉取请求，将Taproot并入Bitcoin Core代码库。为了全面部署升级，节点运行者须采用Taproot的全新共识规则。该提案最终得到90%的矿工支持，并于**2021年11月14日在区块709,632中正式激活**。

## Taproot如何运作？

### Schnorr签名(BIP340)

[Schnorr签名](https://academy.binance.com/zh/articles/what-do-schnorr-signatures-mean-for-bitcoin)提高了比特币网络验证交易的速度和安全性。该签名由[密码学](https://academy.binance.com/zh/articles/history-of-cryptography)签名方案组成，开发者是德国数学家兼密码学家Claus Schnorr。多年来，Schnorr的算法始终受专利保护，但该专利于2008年正式过期。Schnorr签名优点众多，尤其在短签名生成方面，以简洁高效著称。

比特币创始人中本聪采用的签名方案称为“椭圆曲线数字签名算法(ECDSA)”。选择ECDSA而非Schnorr签名算法是因为前者使用广泛、易于理解、安全稳定、轻量并且开源。

然而，Schnorr数字签名计划(SDSS)的推进可能是比特币与其他区块链网络应用新一代签名技术的起点。

Schnorr签名的一大核心优势是可以在复杂的比特币交易中提取多组密钥，生成独一无二的签名。因此，交易中各方的签名可整合为单一的Schnorr签名，这个过程称为“签名聚合”。

实际上，Taproot可以让人完全看不出来比特币脚本在运行。例如，采用Taproot后，无论是闪电网络通道交易、点对点交易还是通过复杂的智能合约交易，不同比特币支付方式看起来毫无差别。这些交易的监控者看到的只有点对点交易。然而，值得注意的是，这并未改变发送者与最终接收者的钱包信息暴露于外的事实。

