# BOLT11

## 概念简介

BOLT11 是闪电网络（Lightning Network）的发票格式标准，定义了闪电网络支付请求的编码规范。BOLT 是 "Basis of Lightning Technology" 的缩写，而 BOLT11 专门规定了如何构造和解析闪电网络支付发票。

闪电网络发票包含完成支付所需的所有信息，如金额、接收方节点、过期时间、路由提示等。这些发票由接收方生成，使用 bech32 编码格式（与[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)隔离见证地址相同的编码方式）。

## 发票结构

**人类可读部分**
- 前缀：`ln` + BIP-0173 货币前缀（如 `lnbc` 表示比特币主网）
- 金额：可选的支付金额
- 乘数：金额单位（m=毫比特币, u=微比特币, n=纳比特币, p=皮比特币）

**数据部分**
- 时间戳：自1970年以来的秒数（35位，大端序）
- 支付哈希：用于 HTLC 的哈希值
- 接收方公钥：闪电节点的公钥
- 过期时间：发票的有效期
- 路由提示：帮助找到支付路径的信息
- 签名：确保发票真实性

## 使用方式

**URI 方案**
推荐使用 `lightning:` 作为前缀（注意：不是 `lightning://`），例如：
```
lightning:lnbc1500n1...
```

也可以使用 BIP-21 的 `bitcoin:` URI，通过 `lightning` 参数包含 BOLT11 编码：
```
bitcoin:bc1qxy...?amount=0.0001&lightning=lnbc1500n1...
```

## 应用场景

1. **在线支付**：商家生成发票供客户扫描支付
2. **点对点转账**：用户之间快速交换发票进行转账
3. **自动化支付**：应用程序解析发票自动完成支付
4. **跨境汇款**：利用闪电网络的低费用和快速确认

## 工具和库

- 多种编程语言都有 BOLT11 编码/解码库
- 在线解码器可以查看发票详细信息
- 闪电[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)自动处理发票的生成和解析

## 推荐阅读

- [The Lightning Invoice](https://www.bolt11.org/)
- [BOLT #11 Specification](https://github.com/lightning/bolts/blob/master/11-payment-encoding.md)
- [Understanding Lightning Invoices](https://docs.lightning.engineering/the-lightning-network/payment-lifecycle/understanding-lightning-invoices)

## 相关概念

- **闪电网络 (Lightning Network)**
- **HTLC (哈希时间锁合约)**
- **BIP-0173 (Bech32)**
- **BIP-21 (URI Scheme)**
- **支付通道 (Payment Channel)**
