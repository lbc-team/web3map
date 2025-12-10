# 哈希时间锁合约（HTLC）

## 概念简介

哈希时间锁合约（Hash Time Locked Contract, HTLC）是一种条件支付机制，最初由闪电网络引入，现已被广泛应用于 Interledger、Raiden Network、Sprites channels 等多个系统。

HTLC 结合了哈希锁（Hashlock）和时间锁（Timelock）两种机制，使得资产接收方必须在截止时间前确认收到资产并生成收据证明，否则资产将退还给发送方。这种机制实现了无需信任第三方中介的去中心化条件支付。

## 核心机制

**哈希锁（Hashlock）**
- 接收方 Eric 生成一个秘密值 R
- 计算 R 的哈希值 H = Hash(R)
- 将 H 发送给发送方 Alice，但不透露 R
- 只有提供正确的 R 才能解锁资金

**时间锁（Timelock）**
- 设定一个截止时间（如 24 小时）
- 如果在截止时间前接收方未能提供 R
- 资金自动退还给发送方
- 防止资金永久锁定

**工作流程**
1. **准备阶段**：Eric 生成 R，发送 H 给 Alice
2. **锁定阶段**：Alice 创建 HTLC，锁定资金，条件是提供 R 或超时
3. **解锁阶段**：Eric 在截止时间前提供 R，获得资金
4. **退款阶段**：如果超时，Alice 可以取回资金

## 闪电网络中的应用

**支付通道网络**
HTLC 是闪电网络被称为"网络"的关键：
- Alice 和 Bob 之间没有直接通道
- 但可以通过中间节点 Charlie 完成支付
- 每一跳都使用 HTLC 确保安全

**路由支付示例**
```
Alice → Charlie → Bob
  100 sats   100 sats
```

1. Bob 生成秘密 R，发送 H 给 Alice
2. Alice 创建 HTLC 给 Charlie：提供 R 或退款
3. Charlie 创建 HTLC 给 Bob：提供 R 或退款
4. Bob 提供 R 给 Charlie，获得资金
5. Charlie 用同一个 R 向 Alice 索取资金
6. 支付完成，Bob 收到钱，Alice 得到支付证明（R）

**原子性保证**
- 要么整个支付路径成功
- 要么整个支付失败并退款
- 不会出现部分成功的情况
- 中间节点无法窃取资金

## 技术细节

**HTLC 脚本**
比特币中的 HTLC 可以用脚本表示：
```
OP_IF
  OP_HASH160 <H> OP_EQUALVERIFY
  <接收方公钥> OP_CHECKSIG
OP_ELSE
  <超时时间> OP_CHECKLOCKTIMEVERIFY OP_DROP
  <发送方公钥> OP_CHECKSIG
OP_ENDIF
```

**时间锁递减**
多跳支付中，每一跳的时间锁必须递减：
- Alice → Charlie：48 小时
- Charlie → Bob：24 小时
- 确保下游先解锁，上游有时间响应

## 应用场景

**跨链原子交换**
- Alice 的[比特币](https://learnblockchain.cn/tags/比特币?map=BTC) ↔ Bob 的以太币
- 使用相同的哈希锁 H
- 两条链上同时创建 HTLC
- 要么都成功，要么都失败

**去中心化交易所**
- 无需信任的资产交换
- 点对点交易
- 消除对手方风险

**跨境支付**
- 通过多个中介完成跨境转账
- 每一跳都有 HTLC 保护
- 快速且低成本

**证券结算**
- 证券交付与资金支付同步
- DvP（Delivery versus Payment）
- 降低结算风险

## 演进：PTLC

闪电网络最近提出了 PTLC（Point Time Locked Contracts）：

**HTLC 的问题**
- 所有参与方使用相同的哈希 H
- 中间节点可以关联支付
- 隐私性不足

**PTLC 的改进**
- 使用椭圆曲线点而非哈希
- 每一跳使用不同的点
- 更好的隐私保护
- 需要 Schnorr 签名支持（Taproot 启用）

## 安全考虑

**时间参数设置**
- 时间锁不能太短：接收方需要足够时间响应
- 时间锁不能太长：发送方资金锁定时间过久
- 需要考虑网络延迟和区块确认时间

**哈希函数安全性**
- 必须使用抗碰撞的哈希函数
- 秘密值 R 必须有足够的熵
- 防止哈希猜测攻击

**链重组风险**
- 时间锁依赖区块高度或时间戳
- 链重组可能改变时间锁状态
- 需要适当的确认深度

## 意义和影响

HTLC 是区块链技术的重要创新：
- 实现了无需信任的条件支付
- 使得支付通道网络成为可能
- 推动了闪电网络等 Layer 2 方案
- 启发了跨链和互操作性解决方案

作为闪电网络的"主心骨"，HTLC 让比特币能够实现快速、低成本的小额支付，是[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)扩展性方案的关键组成部分。

## 推荐阅读

- [哈希时间锁合约原理](https://blog.csdn.net/qq_38123961/article/details/122990589)
- [闪电网络深入解读](https://learnblockchain.cn/article/3008)
- [HTLC 机制详解](https://blog.csdn.net/shangsongwww/article/details/90052826)

## 相关概念

- **闪电网络 (Lightning Network)**
- **支付通道 (Payment Channel)**
- **原子交换 (Atomic Swap)**
- **PTLC (Point Time Locked Contract)**
- **时间锁 (Timelock)**
- **哈希锁 (Hashlock)**
