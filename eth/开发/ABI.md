## ABI

[ABI](https://learnblockchain.cn/tags/ABI?map=EVM)（Application Binary Interface，应用程序二进制接口）是 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 智能合约的重要组成部分，它定义了智能合约中的函数和事件的接口。ABI 是智能合约和外部应用程序（如前端应用）之间通信的桥梁。



##  ABI 描述 与 ABI 编码

使用 ABI 时，经常会接触到两个概念： ABI 描述格式和 ABI 编码，下面我将通过一个简单的智能合约来解释 ABI 格式和 ABI 编码：

```solidity
pragma solidity ^0.8.0;

contract Example {
    uint256 public value;

    event ValueChanged(uint256 newValue);

    function setValue(uint256 newValue) public {
        value = newValue;
        emit ValueChanged(newValue);
    }

    function getValue() public view returns (uint256) {
        return value;
    }
}
```



### ABI 格式

编译上述智能合约后，会生成如下的 ABI 描述（JSON 格式）：

```json
[
    {
        "constant": true,
        "inputs": [],
        "name": "getValue",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "newValue",
                "type": "uint256"
            }
        ],
        "name": "setValue",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "name": "newValue",
                "type": "uint256"
            }
        ],
        "name": "ValueChanged",
        "type": "event"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "value",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]

```



### ABI 编码示例

#### 调用 `setValue` 函数

假设我们要调用 `setValue` 函数，将 `newValue` 设置为 `42`。需要进行以下步骤：

1. 获取函数签名：`setValue(uint256)`
2. 计算函数选择器：`keccak256("setValue(uint256)")` 的前 4 字节
3. 编码参数：将 `42` 编码为 32 字节

**函数选择器计算：**

```
keccak256("setValue(uint256)") = 0x55241077da72b49e97926b4dd0cf5bc54426914c9124d1b8e4f58b3ad3c96c3b
```

前 4 字节（函数选择器）为：`0x55241077`

**参数编码：**

```
`42` 编码为 32 字节：`000000000000000000000000000000000000000000000000000000000000002a`
```

**最终编码：**

将函数选择器和参数编码组合在一起：

```
0x55241077000000000000000000000000000000000000000000000000000000000000002a
```



当调用智能合约中的`setValue`函数时， 这个最终编码就是发送到 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 网络的 payload 数据。智能合约接收到调用数据后，会根据 ABI 解析并执行相应的函数。

## ABI 工具支持

很多 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 交互库，如 [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) 和 [Web3.js](https://learnblockchain.cn/tags/ethers.js?map=EVM)，都提供了对 ABI 的支持，简化了智能合约的调用和事件监听过程。

有一些工具（如：  [Viem](https://learnblockchain.cn/tags/Viem?map=EVM)）会根据 ABI 中定义的变量类型，使用静态类型检查，让函数参数和返回值的类型在编译时就已经确定。这样可以避免许多潜在的错误，确保数据的一致性和可靠性。



有一些方便开发者的编解码工具：

*  函数名 和 函数选择器相互转换（查询）： https://chaintool.tech/querySelector

* 调用数据（Calldata）编解码： https://chaintool.tech/calldata

* ABI 可视化调用：https://chaintool.tech/abi

* OpenChain 工具，提供 ABI 编解码、调用堆栈：https://openchain.xyz

  



