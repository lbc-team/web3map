## Gas 优化 (Gas Optimization)

Gas 优化是指在开发[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)时，通过编写高效的代码和采用特定的设计模式，以减少合约部署和执行所需的 Gas 消耗的过程。

### 解决的问题
在[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)网络中，每一行代码的执行和每一个数据的存储都需要支付 Gas。由于区块空间有限且 Gas 价格波动，低效的合约代码会导致极其昂贵的交易成本，降低用户体验，甚至导致交易因 Gas 不足而失败。[Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 优化旨在在保证合约功能和安全性的前提下，最小化这些成本。

### 实现机制与原理
[Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 优化主要围绕减少 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 操作码的执行数量和降低昂贵操作（如存储读写 `SSTORE`/`SLOAD`）的使用频率。

常见的优化技术包括：
1.  **变量打包 (Storage Packing):**
    *   EVM 的存储槽 (Storage Slot) 大小为 32 字节 (256位)。
    *   通过将多个小变量（如 `uint128`, `address`, `bool`）按顺序声明，Solidity 编译器会将它们打包进同一个槽位中。
    *   这样在读取或写入时，只需一次 `SLOAD` 或 `SSTORE` 操作，显著节省 Gas。
2.  **Unchecked Arithmetic (不检查算术):**
    *   Solidity 0.8+ 默认开启溢出检查，这会消耗额外 Gas。
    *   如果在循环或确定不会溢出的场景下，可以使用 `unchecked { ... }` 代码块来跳过检查。
3.  **使用 Calldata 代替 Memory:**
    *   对于外部函数 (external function) 的数组或结构体参数，使用 `calldata` 关键字而不是 `memory`，因为 `calldata` 是只读的且直接从交易输入中读取，比复制到内存更便宜。
4.  **内联汇编 (Inline Assembly):**
    *   使用 `assembly { ... }` 直接编写 Yul 代码，绕过 Solidity 的某些开销，直接操作 EVM 堆栈和内存。
5.  **避免昂贵的循环:**
    *   尽量减少循环次数，避免在循环中进行存储写入操作。
6.  **使用常量和不可变量:**
    *   使用 `constant` (常量) 和 `immutable` (不可变量) 关键字，它们的值在编译时或部署时确定，直接嵌入字节码中，读取时无需访问存储槽。

在执行 Gas 优化的同时， 需要注意 **复杂性权衡:** 过度优化（尤其是使用汇编时）可能会降低代码的可读性和安全性。


### 推荐阅读
*   [Gas 优化手册](https://learnblockchain.cn/course/95)

### 相关概念

*   **[EVM](https://learnblockchain.cn/tags/EVM?map=EVM) Opcodes:** [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)虚拟机的指令集，每个指令都有对应的 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本。
*   **Storage Slot:** [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 永久存储的基本单元。
*   **Optimizer:** [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 编译器自带的优化器，可以在编译时开启。
