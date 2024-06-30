### EVM 是什么？

[EVM](https://learnblockchain.cn/tags/EVM?map=EVM)（Ethereum Virtual Machine，以太坊虚拟机）是[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)的核心组件之一。它是一种图灵完备的虚拟机，允许任何人通过[智能合约](https://learnblockchain.cn/tags/智能合约?map=EVM)在区块链上运行代码。

[Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM)语言 与 EVM， 类似语 Java 与 JVM，由于 EVM 的存在，让以太坊成为一个全球无需可的计算机。



### EVM 执行原理

1. **合约编译/部署**：智能合约通常使用[Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM)语言编写，然后编译成[EVM字节码](https://learnblockchain.cn/tags/EVM%E5%AD%97%E8%8A%82%E7%A0%81)，编译后的字节码通过交易的方式部署到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)链。
2. **执行交易**：每次调用智能合约方法时，都会生成一个交易，这个交易包含了要执行的函数（选择器）以及相关的输入数据。
3. **Gas 计算**：在EVM中，每条指令的执行都需要消耗一定的[Gas](https://learnblockchain.cn/tags/Gas?map=EVM)。Gas 机制用于防止网络资源被滥用。每个交易发送者在发起交易时需要预先指定愿意支付的最大 Gas 量。
4. **指令执行**：EVM 以堆栈为基础架构，字节码被加载到 EVM 后，依次执行每条指令。这些指令可以进行算术运算、堆栈操作、存储操作、条件跳转等。
5. **存储与内存**：EVM 具有两种主要的存储区域：永久存储（Storage）和临时内存（Memory）。永久存储用于保存智能合约状态，存储在区块链上；临时内存用于在交易执行过程中存储中间数据，交易结束后会被清空。
6. **结果返回**：指令执行完毕后，EVM 返回执行结果。如果执行成功，状态改变和输出结果会被记录到区块链上；如果执行失败，则回滚所有状态变化，并返回错误信息。
7. **账户状态更新**：根据交易的执行结果，更新相关账户的状态（例如余额、存储数据等）。



EVM 执行过程中的关键点在于其去中心化和一致性。所有节点都运行相同的EVM代码，确保每个节点在处理同一交易时都能得到相同的结果。

EVM 是一个封闭沙盒环境，只能读取链内部的状态。



## EVM 兼容链

由于 EVM 具有灵活性和强大的计算能力，能够支持各种复杂的去中心化应用（DApps），这也是[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)生态系统繁荣的基础。

也因此发展出了很多 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 兼容链，他们是实现（EVM）规范的区块链，使得这些链能够运行以太坊上编写的智能合约，并与以太坊上的工具和基础设施兼容。



常见的 EVM 兼容链：**BNB Chain （原币安智能链 BSC）**、**Polygon（以前称为 Matic）**、Avalanche、Fantom



##  进一步阅读

文章：[深入以太坊虚拟机](https://learnblockchain.cn/article/8564)

[专栏：理解 EVM - 探究Solidity 背后的秘密](https://learnblockchain.cn/column/22)

[专栏：以太坊 EVM 谜题破解](https://learnblockchain.cn/column/21)