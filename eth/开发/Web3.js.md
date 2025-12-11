# Web3.js

## 概念简介

Web3.js 是以太坊官方的 JavaScript 库,用于通过 HTTP、WebSocket 或 IPC 与以太坊节点进行交互。作为最早的以太坊 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 库,Web3.js 由以太坊基金会于2015年发布,是以太坊生态系统中最成熟、使用最广泛的开发工具之一。

Web3.js 提供了完整的 API 集合,涵盖账户管理、智能合约交互、交易发送、事件监听、区块查询等所有以太坊操作。它支持以太坊主网、各种测试网以及兼容以太坊的区块链（如 BSC、Polygon 等）。虽然近年来 ethers.js 和 viem 等新库兴起,但 Web3.js 凭借其悠久历史、丰富生态和官方背景,仍然是许多项目的首选库。

## 核心特性

### 模块化架构

Web3.js 采用模块化设计,主要包含以下模块：
- **web3-eth**：与以太坊区块链交互的核心模块,处理交易、区块、账户等
- **web3-eth-contract**：智能合约交互模块,部署和调用合约
- **web3-eth-accounts**：账户管理模块,创建账户、签名交易和消息
- **web3-eth-personal**：管理节点的个人账户
- **web3-eth-abi**：[ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 编解码模块
- **web3-eth-ens**：以太坊域名服务（ENS）支持
- **web3-net**：网络相关功能,查询节点信息
- **web3-utils**：工具函数集合,单位转换、哈希等
- **web3-providers**：Provider 管理,支持多种连接方式

开发者可以根据需要导入特定模块,也可以使用完整的 Web3 对象。

### Provider 系统

Web3.js 支持多种 Provider 连接以太坊节点：
- **HttpProvider**：通过 HTTP/HTTPS 连接到节点
- **WebSocketProvider**：使用 WebSocket 进行持久连接,支持订阅
- **IpcProvider**：通过 IPC 连接本地节点（Node.js 环境）
- **自定义 Provider**：可以实现自定义 Provider,如连接到硬件钱包

Provider 可以在运行时切换,灵活支持多种部署场景。

### 智能合约交互

Web3.js 提供强大的合约交互能力：
- **合约实例化**：通过 [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 和地址创建合约对象
- **方法调用**：
  - **call()**：调用只读函数（view/pure）,不消耗 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM)
  - **send()**：发送交易,改变合约状态
  - **estimateGas()**：估算函数执行的 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 消耗
- **事件处理**：
  - **events.EventName()**：监听特定事件
  - **getPastEvents()**：查询历史事件
  - **allEvents()**：监听所有事件
- **合约部署**：`deploy()` 方法部署新合约

### 账户和签名

账户管理功能包括：
- **创建账户**：`web3.eth.accounts.create()` 生成新的以太坊账户
- **导入账户**：从私钥或 Keystore 文件导入账户
- **钱包管理**：`web3.eth.accounts.wallet` 管理多个账户
- **交易签名**：`signTransaction()` 签署交易
- **消息签名**：`sign()` 签署任意消息
- **签名恢复**：`recover()` 从签名恢复签名者地址
- **加密存储**：`encrypt()` 和 `decrypt()` 加密私钥为 Keystore 格式

### 订阅和事件

Web3.js 通过 WebSocket Provider 支持实时订阅：
- **newBlockHeaders**：订阅新区块
- **pendingTransactions**：订阅待处理交易
- **logs**：订阅符合特定过滤条件的日志
- **syncing**：订阅节点同步状态变化

订阅机制让 DApp 能够实时响应链上变化,提供流畅的用户体验。

### 工具函数

`web3.utils` 提供丰富的工具函数：
- **单位转换**：`toWei()`、`fromWei()` 在不同单位间转换
- **地址操作**：`toChecksumAddress()`、`isAddress()` 地址验证和格式化
- **哈希函数**：`sha3()`、`keccak256()`、`soliditySha3()` 等
- **十六进制转换**：`toHex()`、`hexToNumber()` 等
- **字符串编码**：`utf8ToHex()`、`hexToUtf8()` 等
- **随机数**：`randomHex()` 生成安全随机数

## 主要特点

**官方支持**：作为以太坊基金会官方维护的库,Web3.js 享有最权威的地位。新的以太坊特性通常会优先在 Web3.js 中实现。

**成熟稳定**：经过8年的发展和迭代,Web3.js 已经非常成熟。被数以万计的项目使用,在生产环境中经受了充分检验。

**功能完整**：Web3.js 提供最全面的以太坊 API 覆盖,从基础的交易到高级的合约交互、ENS、订阅等,应有尽有。

**生态丰富**：大量第三方工具、框架、教程基于 Web3.js 构建。Truffle、Ganache、Remix 等知名工具都集成了 Web3.js。

**社区庞大**：拥有最大的以太坊开发者社区,问题容易找到解决方案,有大量学习资源。

**兼容性广**：支持各种以太坊节点实现（Geth、Parity、Nethermind 等）和 EVM 兼容链。

**插件系统**：支持插件扩展功能,社区开发了大量有用的插件。

## 版本演进

**Web3.js 0.x（2015-2017）**：早期版本,奠定了基础 API。使用回调函数处理异步操作。

**Web3.js 1.x（2018-2023）**：重大重构,引入 Promise 和 async/await。模块化架构,改进了 Provider 系统。增加了订阅功能、批量请求、事件过滤等高级特性。目前最广泛使用的版本。

**Web3.js 4.x（2023）**：最新版本,进一步现代化。完全用 TypeScript 重写,提供完整的类型定义。使用原生 `BigInt`,性能提升。改进了错误处理和插件系统。支持 Tree-shaking,减小打包体积。

目前 1.x 和 4.x 并行维护,1.x 仍被大量项目使用,4.x 逐步推广。

## 基本用法示例

**连接以太坊节点**：
```javascript
const Web3 = require('web3');

// 连接到本地节点
const web3 = new Web3('http://localhost:8545');

// 或连接到 Infura
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');

// 或从浏览器钱包（如 MetaMask）获取 Provider
const web3 = new Web3(window.ethereum);
```

**查询[账户](https://learnblockchain.cn/tags/账户?map=EVM)余额**：
```javascript
const balance = await web3.eth.getBalance('0x...');
console.log(web3.utils.fromWei(balance, 'ether'));
```

**发送交易**：
```javascript
const tx = await web3.eth.sendTransaction({
  from: '0x...',
  to: '0x...',
  value: web3.utils.toWei('0.1', 'ether'),
  gas: 21000
});
```

**与[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)交互**：
```javascript
const abi = [...]; // 合约 ABI
const contract = new web3.eth.Contract(abi, '0x...');

// 调用只读函数
const result = await contract.methods.balanceOf('0x...').call();

// 发送交易改变状态
await contract.methods.transfer('0x...', '1000').send({ from: '0x...' });

// 监听事件
contract.events.Transfer({}, (error, event) => {
  console.log(event);
});
```

## 应用场景

**DApp 前端**：Web3.js 是 [DApp](https://learnblockchain.cn/tags/DApp) 前端最常用的库之一,处理[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)连接、交易发送、合约调用等核心功能。

**钱包集成**：许多[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)（如 MetaMask、Trust Wallet）内置了 Web3.js 或兼容的 Provider,方便 [DApp](https://learnblockchain.cn/tags/DApp) 集成。

**开发工具**：Truffle、Hardhat、Remix 等开发框架使用 Web3.js 进行合约部署和测试。

**后端服务**：Node.js 后端使用 Web3.js 监听链上事件、处理交易、管理[账户](https://learnblockchain.cn/tags/账户?map=EVM)。

**自动化脚本**：批量操作脚本,如空投代币、数据迁移、批量查询等。

**区块链浏览器**：Etherscan 等浏览器使用 Web3.js 查询和展示链上数据。

**教育培训**：作为最知名的以太坊库,Web3.js 是学习以太坊开发的主要工具。

**企业应用**：许多企业区块链应用选择 Web3.js 作为与以太坊交互的标准库。

## 与其他库的比较

**Web3.js vs ethers.js**：
- Web3.js 更早,生态更成熟
- ethers.js 更轻量（88KB vs 300KB+）
- ethers.js TypeScript 支持更好（v4 之前）
- Web3.js 功能更全面
- [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) API 更现代简洁
- 两者功能基本等价,主要是风格偏好

**Web3.js vs viem**：
- viem 是新兴库,性能更优
- viem TypeScript 原生,类型安全更好
- viem 更模块化,体积更小
- Web3.js 生态和社区更成熟
- viem 正在快速崛起

**Web3.js 4.x vs 1.x**：
- 4.x 完全 TypeScript 重写
- 4.x 使用原生 BigInt,性能更好
- 4.x 改进了插件系统和错误处理
- 1.x 更稳定,兼容性更好
- 4.x 是未来方向,但需要时间成熟

## 相关概念

- **[ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM)** - 另一个主流以太坊 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 库
- **web3.py** - Web3.js 的 Python 版本
- **Truffle** - 基于 Web3.js 的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)开发框架
- **Ganache** - 集成 Web3.js 的本地[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)测试环境
- **Remix** - 在线 IDE，使用 Web3.js 进行合约交互
- **MetaMask** - 提供 Web3.js 兼容的 Provider
- **ENS** - Web3.js 原生支持的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)域名服务

## 相关链接

- 官方网站：https://web3js.org
- GitHub：https://github.com/web3/web3.js
- 4.x 文档：https://docs.web3js.org
- 1.x 文档：https://web3js.readthedocs.io
- NPM：https://www.npmjs.com/package/web3
- Discord：https://discord.gg/yjyvFRP
- 教程：https://web3js.readthedocs.io/en/v1.10.0/getting-started.html
- Ethereum.org：https://ethereum.org/en/developers/docs/apis/javascript/
