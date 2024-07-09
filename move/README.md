## Move 语言

Move 语言是专为区块链平台设计的编程语言，是一种安全、沙盒式和形式化验证的下一代编程语言，它由 Facebook（现为 Meta）为 Diem 区块链项目开发。
Move 允许开发人员编写灵活管理和转移数字资产的程序，同时提供安全保护，防止对链上资产的攻击。

Move 的诞生从Rust中吸取了灵感，Move也是因为使用具有移动(move)语义的资源类型作为数字资产(例如货币)的显式表示而得名。

应用 Move 的两个突出的项目是 [Sui](https://learnblockchain.cn/tags/Sui) 和 [Aptos](https://learnblockchain.cn/tags/Aptos) 。 


### Move 的关键特性：

1. **面向资源的编程**：
   - Move 引入了资源的概念，这些数据类型不能被复制或意外丢弃，确保交易的安全性和正确性。
   - 资源模拟数字资产，确保它们永远不会被意外复制或丢失。

2. **模块化和重用**：
   - 该语言支持模块，这些模块是可重用和可组合的代码单元，允许开发人员通过组装较小的经过验证的组件来创建复杂的应用程序。

3. **安全性和保障**：
   - Move 包括形式验证工具，以确保智能合约不受某些类别的错误和漏洞影响。
   - 其类型系统和资源模型有助于防止可能导致安全问题的常见编程错误。


### 与其他语言的比较：

- **Solidity**：[EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 的主要语言。 Solidity 使用广泛并拥有庞大的生态系统， Move 更注重安全性和形式验证。
- **Rust**和**Go**：这些语言用于区块链开发，因为它们具有出色的性能和安全功能，但并非专为智能合约设计。
- **Cairo**：一种为 zk-rollups 和 StarkNet 设计的语言，专注于零知识证明。

### Awesome-Move
Move 更多开发者资料，可参考： https://github.com/MystenLabs/awesome-move
