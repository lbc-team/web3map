# Statechain

## 什么是Statechain？

**状态链**（Statechain）是一种二层协议（在“链下”处理交易），由首尔Bitcoin Meetup的组织者、Unhashed 博客联合主持人Ruben Somsen首创，它完全颠覆了比特币交易的概念。Statechain的用户不是在地址间发送资金，而是**直接发送可以使用资金的私钥**。

## Statechain原理

如果只是简单地将直接发送密钥来代替交易，那么显然这是不安全的。我们并不知道交易发起者是否自己备份了一份密钥。因此针对这一问题，Statechain给出的解决方案是加入第二把密钥，将资金放锁在一个多签名合约中，这样只用一把钥匙是无法在链上转移这笔资金的。

第二把密钥是由一个中立的参与方 Victor 来生成的。Victor是这个Statechain的协调员，肩负着非常重要的任务：Victor**必须且仅在**临时密钥的最后一个接收者要求他签名的时候签名。

当Alice想要把这笔资产转移给Bob时，Alice把临时密钥发送给Bob并告知Victor她已经把密钥交出去了。因此Bob 是临时私钥的所有者了。现在Bob可以联系Victor并请求签名来转移资金。

Alice也还保留着这边临时密钥。但是，如果她想要Victor帮忙签名交易、转移资金，Victor会拒绝。对于Victor来说，这些资金已经不属于Alice了。而因为Alice只有一笔私钥，光靠自己是没法转移其中的资金的。

自然这也会引出另一个问题，如果Victor接到了交易请求后不签名交易，那么这些资产就无法取出了。针对这个问题，Statechain也给出了解决方案：

在Alice初始化这个Statechain时，她采取了预防措施：在把资金发送到这个多签名地址之前，她创建了一笔 “**备份交易**”，**将资金从这个多签名地址发送到一个新的地址**。Alice不把这笔备份交易发送到网络中。相反，她把交易发给Victor，要求他签名并发回给自己。

在 Alice 收到签过名（但没有广播）的备份交易之后，她再把资金发到多签名地址里面。这样一来，即使 Victor 消失了，她也可以把备份交易广播出去、在一段时间后拿回自己的钱。

现在，假设 Alice 要给 Bob 发送临时密钥了，她先联系 Victor 并让他为 Bob 签名一条新的备份交易并交给 Bob。所以，当 Bob 拿到临时密钥时，就已经有一笔**未广播但签过名**的备份交易了，所以他也能在 Victor 玩失踪的时候拿回自己的钱。

Alice和Bob（以及后续所有获得了临时密钥的人）使用一个为闪电网络设计的密码学方法，叫做 “**Eltoo**”。Eltoo 使得Bob可以用自己的备份交易 “**覆盖**”Alice的备份交易。所以，如果Alice尝试欺诈，把自己的旧备份交易广播出去，Bob 既可以在 Alice 的等待期里与Victor联系，联手拿回自己的钱；也可以使用自己的备份交易直接覆盖掉 Alice 的交易。

![statechain](https://img.learnblockchain.cn/web3map/statechain.png)

***

参考文章：https://bitcoinmagazine.com/technical/statechains-sending-keys-not-coins-to-scale-bitcoin-off-chain
