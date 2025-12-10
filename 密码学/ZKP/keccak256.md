# keccak256

## 概念简介

Keccak256 是以太坊使用的核心哈希函数，基于 Keccak 算法（SHA-3 竞赛获胜者）。需要注意的是，以太坊使用的 Keccak256 与 NIST 标准化的 SHA3-256 略有不同，主要区别在于填充方式。

Keccak 算法在 2007 年由 Guido Bertoni、Joan Daemen、Michaël Peeters 和 Gilles Van Assche 设计，2012 年赢得 NIST SHA-3 竞赛，但 NIST 在标准化时修改了填充参数，导致与原始 Keccak 不兼容。

## 核心特性

**固定输出长度**：Keccak256 接受任意长度输入，输出固定 256 位（32 字节）哈希值。

**单向性**：从哈希值无法反推原始输入。

**抗碰撞性**：找到两个不同输入产生相同输出在计算上不可行，碰撞概率约为 2^(-256)。

**雪崩效应**：输入的微小改变导致输出完全不同。

**Sponge 结构**：Keccak 使用海绵构造（Sponge Construction），分为吸收和挤压两个阶段，这与传统的 Merkle-Damgård 结构（SHA-1/SHA-2）不同。

## 在以太坊中的应用

**地址生成**：
1. 从私钥生成公钥（椭圆曲线 secp256k1）
2. 对公钥（去掉前缀的 64 字节）进行 Keccak256 哈希
3. 取哈希结果的后 20 字节（160 位）作为地址
4. 添加 0x 前缀得到最终地址

**交易哈希**：每笔交易的唯一标识符是其 RLP 编码后的 Keccak256 哈希。

**区块哈希**：区块头的 Keccak256 哈希用作区块标识符。

**Merkle Patricia Trie**：以太坊状态树、交易树、收据树都使用 Keccak256 构建。

**[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)**：
- 函数选择器：函数签名的 Keccak256 哈希前 4 字节
- 事件主题：事件签名的 Keccak256 哈希
- 存储槽计算：映射类型的存储位置

## Keccak256 vs SHA3-256

| 特性 | Keccak256（以太坊）| SHA3-256（NIST）|
|------|-------------------|-----------------|
| 核心算法 | Keccak | Keccak |
| 填充方式 | 原始 Keccak 填充 | NIST 修改的填充 |
| 结果 | 不同 | 不同 |
| 标准化 | 以太坊标准 | NIST 标准 |

**重要提示**：由于填充差异，同一输入在 Keccak256 和 SHA3-256 下会产生不同结果，两者不可互换。

## [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 中的使用

```solidity
// 计算字符串的哈希
bytes32 hash = keccak256(abi.encodePacked("Hello World"));

// 计算多个参数的哈希
bytes32 hash = keccak256(abi.encodePacked(address, uint256, string));

// 函数选择器
bytes4 selector = bytes4(keccak256("transfer(address,uint256)"));

// 事件签名
bytes32 topic = keccak256("Transfer(address,address,uint256)");
```

## Gas 成本

**链上计算**：在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)上调用 Keccak256 消耗 Gas：
- 基础成本：30 Gas
- 每 32 字节数据：6 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM)
- 例如 64 字节输入：30 + 2×6 = 42 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM)

**高效性**：相比其他密码学操作（如椭圆曲线运算），Keccak256 相对便宜且快速。

## 安全性

**密码学强度**：Keccak256 被认为是密码学安全的，没有已知的实际攻击方法。

**量子抵抗**：Grover 算法将搜索复杂度从 2^256 降至 2^128，但在可预见的未来仍然安全。

**广泛审查**：作为 SHA-3 竞赛获胜者，Keccak 经过了密码学界的广泛审查。

## 常见陷阱

**abi.encodePacked 碰撞**：
```solidity
// 危险：可能产生相同哈希
keccak256(abi.encodePacked(a, b)) == keccak256(abi.encodePacked(c, d))
// 当 a="AA", b="BB" 与 c="AAB", d="B" 时
```

**解决方案**：使用 `abi.encode` 而非 `abi.encodePacked`，或在参数间添加固定长度分隔符。

## 工具和库

**Web3.js**：`web3.utils.keccak256("Hello World")`

**Ethers.js**：`ethers.utils.keccak256(ethers.utils.toUtf8Bytes("Hello World"))`

**Python**：`from eth_hash.auto import keccak`

## 推荐阅读

- [Keccak - 官方网站](https://keccak.team/)
- [以太坊黄皮书](https://ethereum.github.io/yellowpaper/paper.pdf)
- [理解以太坊地址生成 - 登链社区](https://learnblockchain.cn/article/1593)
- [SHA-3 vs Keccak - Ethereum Stack Exchange](https://ethereum.stackexchange.com/questions/550/which-cryptographic-hash-function-does-ethereum-use)

## 相关概念

- **[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)地址**
- **函数选择器**
- **Merkle Patricia Trie**
- **SHA-3**
- **Sponge构造**
