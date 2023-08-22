# Omnilayer

## 背景

闪电网络致力于为比特币网络扩容，它能在网络中的独立对等节点之间协助快速的比特币链下支付。基于闪电网络的基础理论，OmniBOLT 为比特币网络上的智能资产层，尤其是那些通过 OmniLayer 协议发布的资产，定义了快速流通协议。OmniBOLT 极大地延伸了比特币闪电网络的功能。

**因为对智能资产的基础性支持，当前的 LND 和 BOLT 实现不仅能支持瞬时的 BTC 支付，还有下列优势**：

- 通过 OmniLayer 发行的智能资产的即时支付。
- 不同资产的跨通道原子化互换。
- 基于闪电通道的去中心化交易所，而且具有极快的交易速度。
- 基于原子化互换的担保借贷合约。
- 为去中心化金融而生的更灵活的合约。

（LND 是一种闪电网络节点实现；BOLT 的全称是 “Basis of Lightning Technology”，闪电网络基础。）

## 什么是Omnilayer？

Omnilayer是BTC上的二层协议，可以基于这个协议发行代币，并通过property_id来唯一标识。其中最有名的是**USDT**，它是编号为 31 的 Omni Token。OmniLayer使用的仍然是比特币的主链，只是通过在标准交易中加入一些标识，使得OmniLayer客户端可以分辨哪些交易是OmniLayer协议的交易。Omnilayer上的交易有专门的区块链浏览器[omniexplorer](https://omniexplorer.info/)可以查看。

## 闪电网络和OmniLayer

基于闪电网络的基础协议，OmniBOLT 规范定义了让 OmniLayer 资产通过闪电通道转移的方法，以及 OmniLayer 资产如何能从神奇的快速支付理论中获益。根据链下比特币转账的 Layer-2 协议规范BOLT (Basis of Lightning Technology)，我们提出了 OmniBOLT 特殊协议来延伸基础理论的范围，以支持更广泛的资产类别。

OmniBOLT 自身并不发行代币。所有代币都会发行在 OmniLayer 上，然后通过基于 P2(W)SH 的通道进入 OmniBOLT 网络；由此，代币会被锁定在主链上，但随时可以在 OmniLayer 主链上赎回。

## 相关概念

- **OBD**：OmniBOLT 后台程序。
- **通道**：闪电网络中的 Poon-Dryja 式通道（Poon 和 Dryja 是闪电网络白皮书的两位作者）。通道写成 `[Alice, USDT, Bob]` ，表示 Alice 和 Bob 开设的、注入了 USDT 的通道。
- **财产**：在 OmniLayer 上发行的代币，等同于 “资产”。
- **RSMC**：可撤销的序列式到期合约（Revocable Sequence Maturity Contract）的设计用意是惩罚恶意的对等节点，他们可能会广播更老的承诺交易以获得相比最新余额更多的钱。
- **HTLC**：哈希时间锁合约，将多个通道串联在一起，为并无直接通道相连的对等节点传送代币。
- **承诺交易**：创建出来但默认不会广播出去的交易，在下一笔承诺交易出现后就会 “作废”。
- **BR**：RSMC 所用的违约救济交易，如果 Alice 靠广播更老的承诺交易搞诈骗，BR 将把她所有的通道余额都发给 Bob。
- **RD**：从 2-2 P2SH 交易的输出中支付的可撤销分发交易，在 Alice 广播最新的合法承诺交易时生效。它将立即给 Bob 分发其应得的余额，并在一段时间（比如 100 个区块以后）后给 Alice 分发余额。
- **HED**：哈希时间锁合约执行分发。
- **HT**：哈希时间锁超时。
- **HBR**：哈希时间锁违约救济，也就是 HTLC 中的违约救济交易
- **HTRD**：HTLC 中的可撤销分发交易。
- **HTBR**：HTLC 超时违约救济，惩罚在时间锁期间广播更早的哈希时间锁交易的 Alice。
- **原子化互换**：原子化互换技术使得密码货币可以彼此互换，而不必使用中心化的中介（比如交易所）。
- **HTLSC**：哈希时间锁互换合约，由两笔单独的 HTLC 组成，带有额外指定的交换汇率和时间锁定器。

***

参考文章：

https://medium.com/omnibolt/part-i-omnibolt-detailed-introduction-178f00fe9364

