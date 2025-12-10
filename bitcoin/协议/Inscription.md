# Inscription（铭文）

## 概念简介

Inscription（铭文）是基于比特币 Ordinals 协议的 NFT 实现，由 Casey Rodarmor 于 2023 年 1 月 20 日推出。Ordinals 协议为每个聪（satoshi，比特币最小单位，1 BTC = 1 亿聪）分配唯一的序号，而 Inscriptions 则是在这些有序的聪上"刻"入数据，包括图片、文本、视频等内容。

与以太坊 NFT 不同，Inscription 的元数据不是存储在链外或中心化服务器上，而是完全嵌入到比特币交易的见证数据（witness data）中，实现了真正的"链上"存储。

## 技术原理

**Ordinals 编号系统**
- 按照比特币被挖出的顺序为每个聪分配唯一编号
- 编号在交易中被追踪（先进先出原则）
- 每个聪都可以被识别和追踪

**Inscription 过程**
通过隔离见证（SegWit）和 Pay-to-Taproot（P2TR）实现，分为两个阶段：
1. **Commit（承诺）**：创建包含铭文内容的 Taproot 脚本
2. **Reveal（揭示）**：执行脚本，将内容写入区块链

**数据存储**
- 铭文内容存储在 Taproot 脚本路径花费脚本中
- 利用见证折扣，存储成本相对经济
- 内容完全在链上，永久不可篡改

## 与[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) NFT 的区别

| 特性 | 比特币 Inscription | [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) [NFT](https://learnblockchain.cn/tags/NFT) |
|------|-------------------|------------|
| 元数据存储 | 完全链上 | 通常链外（[IPFS](https://learnblockchain.cn/tags/IPFS)、中心化服务器）|
| 实现方式 | 嵌入交易见证数据 | 智能合约 + 链外存储 |
| 可编程性 | 有限 | 丰富（智能合约）|
| 成本 | 较高（链上存储）| 较低（链外存储）|
| 永久性 | 保证（在比特币上）| 依赖链外服务 |

**概念类比**
- Ordinals 协议 ≈ [ERC-721](https://learnblockchain.cn/tags/ERC721?map=EVM) 的 tokenID
- Inscriptions ≈ [NFT](https://learnblockchain.cn/tags/NFT) 的 metadata

## BRC-20 协议

BRC-20 是基于 Inscription 的同质化代币标准：
- 本质上是包含特定 JSON 格式文本的 Inscription
- 使用 JSON 而非[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)定义代币规则
- 提供创建和管理同质化代币的规范

**BRC-20 格式示例**
```json
{
  "p": "brc-20",
  "op": "mint",
  "tick": "ordi",
  "amt": "1000"
}
```

## 技术优势

**真正的去中心化**
- 数据完全存储在比特币区块链上
- 不依赖任何第三方存储服务
- 与比特币网络同等的安全性和持久性

**抗审查性**
- 一旦铭刻，永久存在
- 无法被删除或修改
- 不受中心化平台控制

**可验证性**
- 任何人都可以验证 Inscription 的真实性
- 完整的所有权历史可追溯
- 透明的创建时间和顺序

## 争议和挑战

**区块空间占用**
- Inscription 占用比特币宝贵的区块空间
- 推高了普通[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)交易的费用
- 引发社区关于[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)用途的讨论

**技术限制**
- 缺乏[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)功能
- 铭刻成本较高
- 大文件存储不经济

## 生态发展

**市场平台**
- Magic Eden、UniSat、OrdinalSwap 等交易市场
- 专门的 Inscription [钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)（如 Unisat Wallet、Xverse）
- 铭文浏览器和分析工具

**应用类型**
- 数字艺术和收藏品
- BRC-20 代币交易
- 链上文档存储
- 实验性协议和应用

## 推荐阅读

- [比特币 Ordinals 铭文与 BRC-20](https://learnblockchain.cn/article/8094)
- [Ordinals 铭文完全指南](https://www.panewslab.com/zh/articledetails/1301r1ibp79c.html)
- [什么是 Ordinals](https://learnblockchain.cn/article/5717)

## 相关概念

- **Ordinals 协议**
- **BRC-20**
- **Taproot**
- **隔离见证 (SegWit)**
- **Casey Rodarmor**
- **Runes**
