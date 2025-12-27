## Solidity 

[Solidity](https://learnblockchain.cn/docs/solidity/) 是一门面向合约的、为实现智能合约而创建的高级编程语言，也是用于开发[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)智能合约)最受欢迎的语言之一。这门语言受到了 C++，Python 和 Javascript 语言的影响，其设计目的是能在 [以太坊虚拟机（EVM）](https://learnblockchain.cn/2019/04/09/easy-evm/) 上运行。

Solidity 是静态类型高级语言，具备面向对象特性：支持继承、库、接口和复杂的用户定义类型。
推荐参考 [Solidity 开发教程](https://learnblockchain.cn/course/93) 系统学习 Solidity。

Solidity 中文文档：可阅读[Solidity最新中文文档](https://learnblockchain.cn/docs/solidity/) 


### Solidity 的实例

一个简单的 Solidity 智能合约示例如下：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private data;

    // 设置数据
    function set(uint256 _data) public {
        data = _data;
    }

    // 获取数据
    function get() public view returns (uint256) {
        return data;
    }
}
```

- `pragma solidity ^0.8.0;`：指定 Solidity 编译器的版本。
- `contract SimpleStorage`：定义一个名为 `SimpleStorage` 的合约。 很类似其他语言定义一个类。
- `uint256 private data;`：定义一个私有的 `uint256` 类型变量 `data`。
- `function set(uint256 _data) public`：定义一个公开的 `set` 函数，用于设置 `data` 的值。
- `function get() public view returns (uint256)`：定义一个公开的 `get` 函数，用于返回 `data` 的值。

### Solidity 开发工具

开发 Solidity 智能合约时，可以使用以下工具：

1. **Remix IDE**：
   - [Remix](https://remix.ethereum.org/) 是一个基于浏览器的开发环境，提供了编写、编译、调试和部署 Solidity 智能合约的全套工具。
2. **Hardhat**：
   - [Hardhat](https://learnblockchain.cn/tags/Hardhat?map=EVM) 是一个 Solidity 开发工具，可以轻松地编写、测试和部署智能合约。Hardhat 使用 Node 进行包管理，如果你熟悉 Node 及 Javascript， Hardhat 将非常简单上手。
3. **Foundry**：
   - [Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM) 是一个 Solidity 开发工具，用于构建、测试、模糊、调试和部署Solidity智能合约， Foundry 的优势是以Solidity 作为第一公民，完全使用 Solidity 进行开发与测试，如果你不太熟悉 JavaScript ， 使用 Foundry 是一个非常好的选择，而且Foundry 构建、测试的执行速度非常快。
4. Truffle： 不推荐使用
5. **OpenZeppelin**：
   - [OpenZeppelin](https://learnblockchain.cn/tags/OpenZeppelin?map=EVM) 提供了可复用的智能合约库和安全工具，帮助开发者编写安全的合约。


## 更多学习资料

1. Solidity 开发教程【必读】：https://learnblockchain.cn/course/93
2. 线上课程：https://learnblockchain.cn/course/28
3. 线下集训：[OpenSpace Web3 集训营](https://learnblockchain.cn/openspace/1)

