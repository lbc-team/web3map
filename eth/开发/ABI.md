# ABI (Application Binary Interface)

## 概念简介

ABI（Application Binary Interface，应用程序二进制接口）是[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)智能合约的标准化接口规范，定义了如何编码函数调用和数据，使得外部应用程序（如前端、脚本、其他合约）能够与[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)进行交互。ABI 是连接链上合约和链下应用的桥梁，类似于传统软件开发中的 API 接口定义。

**核心作用：**

```
智能合约生命周期中的 ABI：

开发阶段：
Solidity 源代码 → 编译器 → 字节码 + ABI JSON

部署阶段：
字节码 → 部署到区块链 → 合约地址

调用阶段：
前端应用 + ABI JSON + 合约地址
    ↓
编码函数调用（ABI 编码）
    ↓
发送交易到区块链
    ↓
EVM 解码并执行
    ↓
返回结果（ABI 解码）
    ↓
前端应用接收数据
```

**ABI vs API：**

```
传统 API（应用程序接口）：
- 高级语言定义（如 JSON、XML）
- 人类可读
- 通过 HTTP 等协议传输

区块链 ABI：
- 二进制编码（字节序列）
- 机器可读，需要解码
- 通过交易 calldata 传输
- 严格的编码规则（确定性）
```

**历史发展：**

- **2014年**：[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)早期版本定义基础 ABI 规范
- **2015年**：正式化 ABI 编码规则（[Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) ABI specification）
- **2017年**：引入 ABI 编码 v2（支持复杂类型如嵌套结构体）
- **2020年+**：工具生态成熟（ethers.js、viem 等提供完善支持）

## ABI 描述格式

### JSON 格式规范

ABI 使用 JSON 数组描述合约接口，每个元素描述一个函数、事件、错误或构造函数。

**完整示例：**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Example {
    uint256 public value;
    address public owner;

    event ValueChanged(uint256 indexed oldValue, uint256 newValue, address indexed changer);
    error Unauthorized(address caller);

    constructor(uint256 _initialValue) {
        value = _initialValue;
        owner = msg.sender;
    }

    function setValue(uint256 _newValue) public {
        if (msg.sender != owner) revert Unauthorized(msg.sender);
        uint256 oldValue = value;
        value = _newValue;
        emit ValueChanged(oldValue, _newValue, msg.sender);
    }

    function getValue() public view returns (uint256) {
        return value;
    }

    function transfer(address _newOwner) external {
        require(msg.sender == owner, "Not owner");
        owner = _newOwner;
    }
}
```

**对应的 ABI JSON：**

```json
[
  {
    "type": "constructor",
    "inputs": [
      {
        "name": "_initialValue",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "setValue",
    "inputs": [
      {
        "name": "_newValue",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "getValue",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "transfer",
    "inputs": [
      {
        "name": "_newOwner",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "value",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "owner",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "event",
    "name": "ValueChanged",
    "inputs": [
      {
        "name": "oldValue",
        "type": "uint256",
        "indexed": true,
        "internalType": "uint256"
      },
      {
        "name": "newValue",
        "type": "uint256",
        "indexed": false,
        "internalType": "uint256"
      },
      {
        "name": "changer",
        "type": "address",
        "indexed": true,
        "internalType": "address"
      }
    ],
    "anonymous": false
  },
  {
    "type": "error",
    "name": "Unauthorized",
    "inputs": [
      {
        "name": "caller",
        "type": "address",
        "internalType": "address"
      }
    ]
  }
]
```

### 字段说明

**通用字段：**

```
type: 类型
- "function": 函数
- "constructor": 构造函数
- "receive": receive 函数（接收ETH）
- "fallback": fallback 函数
- "event": 事件
- "error": 自定义错误

name: 名称
- 函数/事件/错误的名称
- constructor、receive、fallback 无 name 字段

inputs: 输入参数数组
- name: 参数名
- type: 参数类型（规范类型）
- internalType: 内部类型（Solidity 类型）
- indexed: (仅事件) 是否索引
- components: (复杂类型) 子字段

outputs: 输出参数数组
- 仅函数有此字段
- 结构同 inputs

stateMutability: 状态可变性
- "pure": 不读取不修改状态
- "view": 读取状态但不修改
- "nonpayable": 修改状态，不接受 ETH
- "payable": 修改状态，接受 ETH

anonymous: (仅事件) 是否匿名
- false: 普通事件（包含事件签名）
- true: 匿名事件（不包含事件签名，节省 Gas）
```

## ABI 编码规则

### 函数选择器 (Function Selector)

**计算方法：**

```
步骤：
1. 获取函数签名（不含参数名）
2. 计算 keccak256 哈希
3. 取前 4 字节

示例：
function transfer(address _to, uint256 _amount)

1. 函数签名：
   "transfer(address,uint256)"
   注意：
   - 无空格
   - 无参数名
   - 使用规范类型名

2. keccak256 哈希：
   keccak256("transfer(address,uint256)")
   = 0xa9059cbb2ab09eb219583f4a59a5d0623ade346d962bcd4e46b11da047c9049b

3. 前 4 字节：
   0xa9059cbb
```

**代码实现：**

```solidity
// Solidity
bytes4 selector = bytes4(keccak256("transfer(address,uint256)"));
// selector = 0xa9059cbb

// JavaScript (ethers.js)
const selector = ethers.utils.id("transfer(address,uint256)").slice(0, 10);
// selector = "0xa9059cbb"

// JavaScript (viem)
import { keccak256, toBytes } from 'viem';
const selector = keccak256(toBytes("transfer(address,uint256)")).slice(0, 10);
```

**常见函数选择器：**

```
ERC20:
- transfer(address,uint256): 0xa9059cbb
- approve(address,uint256): 0x095ea7b3
- transferFrom(address,address,uint256): 0x23b872dd
- balanceOf(address): 0x70a08231

ERC721:
- safeTransferFrom(address,address,uint256): 0x42842e0e
- ownerOf(uint256): 0x6352211e

常用函数:
- initialize(): 0x8129fc1c
- upgradeTo(address): 0x3659cfe6
```

### 基本类型编码

**编码规则：**

```
所有类型都编码为 32 字节（256 位）：

uint<N> (N = 8 to 256, steps of 8):
- 右对齐，左侧补零
- 示例: uint256(42)
  → 0x000000000000000000000000000000000000000000000000000000000000002a

int<N>:
- 有符号整数，二补码表示
- 示例: int256(-1)
  → 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

address:
- 20 字节地址，右对齐
- 示例: 0x1234567890123456789012345678901234567890
  → 0x0000000000000000000000001234567890123456789012345678901234567890

bool:
- true = 1, false = 0
- 示例: true
  → 0x0000000000000000000000000000000000000000000000000000000000000001

bytes<N> (N = 1 to 32):
- 定长字节，左对齐，右侧补零
- 示例: bytes4(0x12345678)
  → 0x1234567800000000000000000000000000000000000000000000000000000000
```

**代码示例：**

```solidity
// Solidity 编码
function encodeBasicTypes() public pure returns (bytes memory) {
    return abi.encode(
        uint256(42),              // 0x000...02a
        int256(-1),               // 0xfff...fff
        address(0x1234...7890),   // 0x000...1234567890
        true,                     // 0x000...001
        bytes4(0x12345678)        // 0x123...000
    );
}

// JavaScript (ethers.js)
const encoded = ethers.utils.defaultAbiCoder.encode(
    ['uint256', 'int256', 'address', 'bool', 'bytes4'],
    [42, -1, '0x1234567890123456789012345678901234567890', true, '0x12345678']
);
```

### 动态类型编码

**动态类型包括：**
- `bytes`（不定长字节）
- `string`（字符串）
- 动态数组（`T[]`）

**编码规则：**

```
动态类型的编码分为两部分：
1. 头部（Head）：数据偏移量（32 字节）
2. 尾部（Tail）：实际数据

结构：
[头部] [尾部]
  ↓       ↓
offset  length + data
```

**示例：bytes**

```solidity
function encodeBytes() public pure returns (bytes memory) {
    bytes memory data = hex"1234";
    return abi.encode(data);
}

编码结果：
0x0000000000000000000000000000000000000000000000000000000000000020  // offset = 32
  0000000000000000000000000000000000000000000000000000000000000002  // length = 2
  1234000000000000000000000000000000000000000000000000000000000000  // data (左对齐)

解释：
- 第1个32字节：偏移量 = 0x20 (32)，表示数据从第32字节开始
- 第2个32字节：长度 = 0x02，表示2个字节
- 第3个32字节：数据 = 0x1234（左对齐，右侧补零）
```

**示例：string**

```solidity
function encodeString() public pure returns (bytes memory) {
    return abi.encode("Hello");
}

编码结果：
0x0000000000000000000000000000000000000000000000000000000000000020  // offset
  0000000000000000000000000000000000000000000000000000000000000005  // length = 5
  48656c6c6f000000000000000000000000000000000000000000000000000000  // "Hello" (UTF-8)

"Hello" 的 UTF-8 编码：
H = 0x48
e = 0x65
l = 0x6c
l = 0x6c
o = 0x6f
```

**示例：动态数组**

```solidity
function encodeDynamicArray() public pure returns (bytes memory) {
    uint256[] memory arr = new uint256[](3);
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;
    return abi.encode(arr);
}

编码结果：
0x0000000000000000000000000000000000000000000000000000000000000020  // offset
  0000000000000000000000000000000000000000000000000000000000000003  // length = 3
  0000000000000000000000000000000000000000000000000000000000000001  // arr[0] = 1
  0000000000000000000000000000000000000000000000000000000000000002  // arr[1] = 2
  0000000000000000000000000000000000000000000000000000000000000003  // arr[2] = 3
```

### 复杂类型编码

**多个参数混合：**

```solidity
function complexEncode(
    uint256 a,
    bytes memory b,
    uint256 c
) public pure returns (bytes memory) {
    return abi.encode(a, b, c);
}

调用：complexEncode(42, hex"1234", 100)

编码结果：
// 头部（Head）
0x000000000000000000000000000000000000000000000000000000000000002a  // a = 42 (静态)
  0000000000000000000000000000000000000000000000000000000000000060  // b 的偏移 = 96
  0000000000000000000000000000000000000000000000000000000000000064  // c = 100 (静态)

// 尾部（Tail）- b 的数据
  0000000000000000000000000000000000000000000000000000000000000002  // b.length = 2
  1234000000000000000000000000000000000000000000000000000000000000  // b.data

规则：
- 静态类型（uint256）直接编码在头部
- 动态类型（bytes）在头部存储偏移量，数据在尾部
- 偏移量从头部开始计算
```

**结构体编码：**

```solidity
struct Person {
    string name;
    uint256 age;
    address wallet;
}

function encodeStruct() public pure returns (bytes memory) {
    Person memory p = Person({
        name: "Alice",
        age: 30,
        wallet: 0x1234567890123456789012345678901234567890
    });
    return abi.encode(p);
}

编码结果：
// 头部
0x0000000000000000000000000000000000000000000000000000000000000020  // struct 偏移
  0000000000000000000000000000000000000000000000000000000000000060  // name 偏移(从struct开始)
  000000000000000000000000000000000000000000000000000000000000001e  // age = 30
  0000000000000000000000001234567890123456789012345678901234567890  // wallet

// 尾部 - name 数据
  0000000000000000000000000000000000000000000000000000000000000005  // name.length = 5
  416c696365000000000000000000000000000000000000000000000000000000  // "Alice"
```

**嵌套数组：**

```solidity
function encodeNestedArray() public pure returns (bytes memory) {
    uint256[][] memory nested = new uint256[][](2);
    nested[0] = new uint256[](2);
    nested[0][0] = 1;
    nested[0][1] = 2;
    nested[1] = new uint256[](1);
    nested[1][0] = 3;

    return abi.encode(nested);
}

编码结果：
// 主数组头部
0x0000000000000000000000000000000000000000000000000000000000000020  // 偏移
  0000000000000000000000000000000000000000000000000000000000000002  // 外层数组长度 = 2
  0000000000000000000000000000000000000000000000000000000000000040  // nested[0] 偏移
  00000000000000000000000000000000000000000000000000000000000000a0  // nested[1] 偏移

// nested[0] 数据
  0000000000000000000000000000000000000000000000000000000000000002  // 长度 = 2
  0000000000000000000000000000000000000000000000000000000000000001  // nested[0][0] = 1
  0000000000000000000000000000000000000000000000000000000000000002  // nested[0][1] = 2

// nested[1] 数据
  0000000000000000000000000000000000000000000000000000000000000001  // 长度 = 1
  0000000000000000000000000000000000000000000000000000000000000003  // nested[1][0] = 3
```

## 函数调用编码

### Calldata 结构

**完整格式：**

```
Calldata = Function Selector (4 bytes) + Encoded Arguments

示例：
transfer(address _to, uint256 _amount)

调用：
transfer(0x1234567890123456789012345678901234567890, 100)

Calldata:
0xa9059cbb                                                          // 选择器 (4 bytes)
  0000000000000000000000001234567890123456789012345678901234567890  // _to (32 bytes)
  0000000000000000000000000000000000000000000000000000000000000064  // _amount = 100 (32 bytes)

总长度：4 + 32 + 32 = 68 字节
```

**生成 Calldata：**

```javascript
// ethers.js
const iface = new ethers.utils.Interface([
    "function transfer(address _to, uint256 _amount)"
]);

const calldata = iface.encodeFunctionData("transfer", [
    "0x1234567890123456789012345678901234567890",
    100
]);
// calldata = "0xa9059cbb0000000000000000000000001234567890123456789012345678901234567890000000000000000000000000000000000000000000000000000000000000064"

// viem
import { encodeFunctionData } from 'viem';

const calldata = encodeFunctionData({
    abi: [{
        name: 'transfer',
        type: 'function',
        inputs: [
            { name: '_to', type: 'address' },
            { name: '_amount', type: 'uint256' }
        ]
    }],
    functionName: 'transfer',
    args: ['0x1234567890123456789012345678901234567890', 100n]
});

// Solidity
bytes memory calldata = abi.encodeWithSelector(
    bytes4(keccak256("transfer(address,uint256)")),
    0x1234567890123456789012345678901234567890,
    100
);
// 或者
calldata = abi.encodeCall(
    IERC20.transfer,
    (0x1234567890123456789012345678901234567890, 100)
);
```

### 解码 Calldata

**手动解码：**

```solidity
contract CalldataDecoder {
    function decodeTransfer(bytes calldata data)
        public
        pure
        returns (address to, uint256 amount)
    {
        require(data.length >= 68, "Invalid calldata length");

        // 检查函数选择器
        bytes4 selector = bytes4(data[0:4]);
        require(
            selector == bytes4(keccak256("transfer(address,uint256)")),
            "Wrong function"
        );

        // 解码参数
        assembly {
            // 跳过选择器（4字节），读取第一个参数
            to := calldataload(add(data.offset, 4))
            // 读取第二个参数
            amount := calldataload(add(data.offset, 36))
        }
    }
}

// JavaScript
function decodeCalldata(calldata) {
    // 提取选择器
    const selector = calldata.slice(0, 10); // "0x" + 8 hex chars

    // 提取参数
    const to = "0x" + calldata.slice(34, 74);  // 跳过 0x + 选择器(8) + 填充(24)
    const amount = parseInt(calldata.slice(74, 138), 16);

    return { selector, to, amount };
}
```

**使用库解码：**

```javascript
// ethers.js
const iface = new ethers.utils.Interface([
    "function transfer(address _to, uint256 _amount)"
]);

const decoded = iface.decodeFunctionData("transfer", calldata);
// decoded = {
//     _to: "0x1234567890123456789012345678901234567890",
//     _amount: BigNumber(100)
// }

// viem
import { decodeFunctionData } from 'viem';

const decoded = decodeFunctionData({
    abi: [...],
    data: calldata
});
```

## 事件编码

### Log 结构

**事件日志格式：**

```solidity
event Transfer(address indexed from, address indexed to, uint256 value);

emit Transfer(0xaaa..., 0xbbb..., 100);

Log 结构：
{
    address: "0x合约地址",
    topics: [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",  // 事件签名
        "0x000000000000000000000000aaa...",  // indexed: from
        "0x000000000000000000000000bbb..."   // indexed: to
    ],
    data: "0x0000000000000000000000000000000000000000000000000000000000000064"  // value = 100
}
```

**事件签名计算：**

```
步骤类似函数选择器，但使用完整 32 字节：

1. 事件签名：
   "Transfer(address,address,uint256)"

2. keccak256 哈希：
   keccak256("Transfer(address,address,uint256)")
   = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef

3. 完整 32 字节作为 topics[0]

注意：
- 匿名事件（anonymous）没有 topics[0]
- 最多 3 个 indexed 参数（topics[1-3]）
- 非 indexed 参数编码在 data 中
```

**常见事件签名：**

```
ERC20:
Transfer(address,address,uint256):
0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef

Approval(address,address,uint256):
0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925

ERC721:
Transfer(address,address,uint256):
0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef

Approval(address,address,uint256):
0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925

ApprovalForAll(address,address,bool):
0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31
```

### 解析事件日志

**代码示例：**

```javascript
// ethers.js
const iface = new ethers.utils.Interface([
    "event Transfer(address indexed from, address indexed to, uint256 value)"
]);

// 解析日志
const log = {
    topics: [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x000000000000000000000000aaa...",
        "0x000000000000000000000000bbb..."
    ],
    data: "0x0000000000000000000000000000000000000000000000000000000000000064"
};

const parsed = iface.parseLog(log);
// parsed = {
//     name: "Transfer",
//     args: {
//         from: "0xaaa...",
//         to: "0xbbb...",
//         value: BigNumber(100)
//     }
// }

// viem
import { decodeEventLog } from 'viem';

const decoded = decodeEventLog({
    abi: [{
        name: 'Transfer',
        type: 'event',
        inputs: [
            { name: 'from', type: 'address', indexed: true },
            { name: 'to', type: 'address', indexed: true },
            { name: 'value', type: 'uint256', indexed: false }
        ]
    }],
    data: log.data,
    topics: log.topics
});
```

**过滤事件日志：**

```javascript
// 获取特定地址的 Transfer 事件
const filter = {
    address: contractAddress,
    topics: [
        ethers.utils.id("Transfer(address,address,uint256)"),
        null,  // from (任意)
        ethers.utils.hexZeroPad(myAddress, 32)  // to (我的地址)
    ],
    fromBlock: 'latest',
    toBlock: 'latest'
};

const logs = await provider.getLogs(filter);
```

## ABI 编码变体

### abi.encode vs abi.encodePacked

**标准编码（abi.encode）：**

```solidity
// 每个参数占 32 字节
bytes memory encoded = abi.encode(uint8(1), uint16(2));

结果：
0x0000000000000000000000000000000000000000000000000000000000000001  // uint8(1) - 32字节
  0000000000000000000000000000000000000000000000000000000000000002  // uint16(2) - 32字节

长度：64 字节
```

**紧密编码（abi.encodePacked）：**

```solidity
// 最小字节表示，无填充
bytes memory packed = abi.encodePacked(uint8(1), uint16(2));

结果：
0x010002  // uint8(1) - 1字节，uint16(2) - 2字节

长度：3 字节

警告：
- 不可逆解码（丢失类型信息）
- 可能导致哈希碰撞
```

**安全问题示例：**

```solidity
// ❌ 危险：哈希碰撞
bytes32 hash1 = keccak256(abi.encodePacked("a", "bc"));
bytes32 hash2 = keccak256(abi.encodePacked("ab", "c"));
// hash1 == hash2 ✅ 碰撞！

// ✅ 安全：使用标准编码
bytes32 hash1 = keccak256(abi.encode("a", "bc"));
bytes32 hash2 = keccak256(abi.encode("ab", "c"));
// hash1 != hash2 ✅ 不同
```

### abi.encodeWithSelector vs abi.encodeWithSignature

**使用选择器：**

```solidity
bytes4 selector = bytes4(keccak256("transfer(address,uint256)"));
bytes memory data = abi.encodeWithSelector(
    selector,
    0x1234567890123456789012345678901234567890,
    100
);
```

**使用签名字符串：**

```solidity
bytes memory data = abi.encodeWithSignature(
    "transfer(address,uint256)",
    0x1234567890123456789012345678901234567890,
    100
);

// 等价于 encodeWithSelector，但在运行时计算选择器
// Gas 成本更高
```

**类型安全版本（[Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 0.8.13+）：**

```solidity
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

// ✅ 类型安全，编译时检查
bytes memory data = abi.encodeCall(
    IERC20.transfer,
    (0x1234567890123456789012345678901234567890, 100)
);

// 优点：
// - 类型检查
// - IDE 自动补全
// - 防止拼写错误
```

## 工具与库

### Web3 库支持

**[ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM)：**

```javascript
const { ethers } = require("ethers");

// 1. 创建接口
const iface = new ethers.utils.Interface([
    "function transfer(address to, uint256 amount)",
    "event Transfer(address indexed from, address indexed to, uint256 value)"
]);

// 2. 编码函数调用
const calldata = iface.encodeFunctionData("transfer", [
    "0x1234567890123456789012345678901234567890",
    ethers.utils.parseEther("1.0")
]);

// 3. 解码函数调用
const decoded = iface.decodeFunctionData("transfer", calldata);

// 4. 编码函数结果
const result = iface.encodeFunctionResult("transfer", [true]);

// 5. 解码函数结果
const [success] = iface.decodeFunctionResult("transfer", result);

// 6. 解析事件
const log = {
    topics: [...],
    data: "0x..."
};
const event = iface.parseLog(log);

// 7. 编码事件过滤器
const filter = iface.encodeFilterTopics("Transfer", [
    "0xaaa...",  // from
    null         // to (任意)
]);
```

**viem：**

```typescript
import {
    encodeFunctionData,
    decodeFunctionData,
    encodeFunctionResult,
    decodeFunctionResult,
    encodeEventTopics,
    decodeEventLog
} from 'viem';

// 编码函数
const data = encodeFunctionData({
    abi: [...],
    functionName: 'transfer',
    args: ['0x...', 100n]
});

// 解码函数
const result = decodeFunctionData({
    abi: [...],
    data: '0x...'
});

// 编码事件主题
const topics = encodeEventTopics({
    abi: [...],
    eventName: 'Transfer',
    args: {
        from: '0x...',
        to: null  // 通配符
    }
});

// 解码事件
const event = decodeEventLog({
    abi: [...],
    data: log.data,
    topics: log.topics
});
```

**web3.py：**

```python
from web3 import Web3

# 编码函数调用
encoded = contract.encode_abi(
    fn_name='transfer',
    args=['0x1234567890123456789012345678901234567890', 100]
)

# 解码函数调用
decoded = contract.decode_function_input(encoded)

# 解析事件
event = contract.events.Transfer().processLog(log)
```

### 在线工具

**ABI 编解码工具：**

```
1. ChainTool
   - URL: https://chaintool.tech/calldata
   - 功能：Calldata 编解码、可视化

2. HashEx ABI Decoder
   - URL: https://abi.hashex.org/
   - 功能：解码交易输入数据

3. OpenChain
   - URL: https://openchain.xyz/tools/abi
   - 功能：ABI 编解码、调用堆栈分析

4. Ethereum Signature Database
   - URL: https://www.4byte.directory/
   - 功能：函数签名查询

5. Samczsun's Calldata Decoder
   - URL: https://calldata.swiss-knife.xyz/
   - 功能：高级 calldata 解码
```

**函数选择器查询：**

```
ChainTool querySelector:
https://chaintool.tech/querySelector

输入：函数签名
输出：4字节选择器

示例：
输入：transfer(address,uint256)
输出：0xa9059cbb
```

## 最佳实践

### 类型安全

```solidity
// ❌ 不安全：字符串拼接，易出错
bytes memory data = abi.encodeWithSignature(
    "tranfer(address,uint256)",  // 拼写错误！
    to,
    amount
);

// ✅ 安全：使用接口，编译时检查
bytes memory data = abi.encodeCall(
    IERC20.transfer,
    (to, amount)
);
```

### Gas 优化

```solidity
// ❌ 高 Gas：运行时计算选择器
function badCall(address token, address to, uint256 amount) external {
    bytes memory data = abi.encodeWithSignature(
        "transfer(address,uint256)",
        to,
        amount
    );
    token.call(data);
}

// ✅ 低 Gas：预计算选择器
bytes4 constant TRANSFER_SELECTOR = bytes4(keccak256("transfer(address,uint256)"));

function goodCall(address token, address to, uint256 amount) external {
    bytes memory data = abi.encodeWithSelector(
        TRANSFER_SELECTOR,
        to,
        amount
    );
    token.call(data);
}

// ✅✅ 最优：直接调用
function bestCall(address token, address to, uint256 amount) external {
    IERC20(token).transfer(to, amount);
}
```

### 安全注意事项

**1. 验证解码数据：**

```solidity
function processCalldata(bytes calldata data) external {
    // ✅ 验证长度
    require(data.length >= 4, "Invalid calldata");

    // ✅ 验证选择器
    bytes4 selector = bytes4(data[0:4]);
    require(
        selector == this.expectedFunction.selector,
        "Wrong function"
    );

    // ✅ 解码并验证参数
    (address to, uint256 amount) = abi.decode(data[4:], (address, uint256));
    require(to != address(0), "Invalid address");
    require(amount > 0, "Invalid amount");
}
```

**2. 避免 encodePacked 的哈希碰撞：**

```solidity
// ❌ 危险
function dangerousHash(string memory a, string memory b)
    public
    pure
    returns (bytes32)
{
    return keccak256(abi.encodePacked(a, b));
}

// ✅ 安全
function safeHash(string memory a, string memory b)
    public
    pure
    returns (bytes32)
{
    return keccak256(abi.encode(a, b));
}

// ✅ 或使用分隔符
function safeHashWithSeparator(string memory a, string memory b)
    public
    pure
    returns (bytes32)
{
    return keccak256(abi.encodePacked(a, "|", b));
}
```

## 推荐阅读

- [Solidity ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) - 官方 ABI 规范
- [Ethereum Contract ABI](https://learnblockchain.cn/docs/solidity/abi-spec.html) - ABI 规范中文版
- [ethers.js Documentation](https://docs.ethers.org/) - [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) ABI 编码文档
- [viem Documentation](https://viem.sh/) - viem [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 工具文档
- [EIP-712: Typed structured data hashing](https://learnblockchain.cn/docs/eips/EIPS/eip-712) - 结构化数据签名
- [4byte Directory](https://www.4byte.directory/) - 函数签名数据库
- [OpenChain ABI Tools](https://openchain.xyz/tools) - [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 工具集

## 相关概念

- **Calldata**：交易输入数据
- **Function Selector**：函数选择器（前4字节）
- **Event Signature**：事件签名（32字节）
- **Topics**：事件日志的索引字段
- **Bytecode**：合约字节码
- **Interface**：合约接口定义
- **EIP-712**：结构化数据签名标准
- **Type Hashing**：类型哈希
