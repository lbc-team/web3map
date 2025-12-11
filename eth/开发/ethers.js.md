# ethers.js

## 概念简介

ethers.js 是一个完整、紧凑的 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 库,用于与以太坊区块链进行交互。由 Richard Moore（ricmoo）于2016年创建,ethers.js 以其简洁的 API、完善的文档、强大的 TypeScript 支持和安全的设计理念,成为以太坊开发者的首选库之一。

ethers.js 提供了连接以太坊节点、管理钱包、与智能合约交互、签名交易等全方位的功能。相比更早的 Web3.js,ethers.js 采用了更现代的设计,体积更小（压缩后约88KB）、API 更简洁、类型安全更好。它被广泛应用于 [DApp](https://learnblockchain.cn/tags/DApp) 前端、Node.js 脚本、钱包应用等场景,支撑着以太坊生态中数以万计的项目。

## 核心特性

### Provider（提供者）

Provider 是 ethers.js 与区块链通信的核心组件：
- **JsonRpcProvider**：连接到以太坊 JSON-RPC 节点
- **WebSocketProvider**：通过 WebSocket 连接,支持实时事件订阅
- **AlchemyProvider / InfuraProvider**：快速连接到 Alchemy、Infura 等节点服务
- **EtherscanProvider**：通过 Etherscan API 查询链上数据
- **FallbackProvider**：配置多个 Provider,自动故障转移
- **BrowserProvider**：从浏览器钱包（MetaMask 等）获取 Provider

Provider 提供只读的链上数据访问,如查询余额、获取区块、估算 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 等。

### Signer（签名者）

Signer 代表一个可以签署交易和消息的[账户](https://learnblockchain.cn/tags/账户?map=EVM)：
- **Wallet**：从私钥或助记词创建的钱包,可以签署交易
- **JsonRpcSigner**：从 Provider 获取的签名器,通常来自浏览器钱包
- **VoidSigner**：只读签名器,用于模拟交易但不实际签名
- **HDNodeWallet**：层级确定性钱包,支持助记词和派生路径

Signer 是 Provider 的超集,既可以读取链上数据,又可以发送交易。

### Contract（合约）

Contract 类提供与智能合约交互的高级接口：
- **合约实例化**：通过合约地址、[ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 和 Provider/Signer 创建合约对象
- **调用只读函数**：自动识别 `view` 和 `pure` 函数,无需发送交易
- **发送交易**：调用状态改变函数,自动构建和发送交易
- **事件监听**：监听合约事件,实时响应链上变化
- **事件过滤**：查询历史事件,支持复杂的过滤条件
- **函数重载支持**：正确处理 Solidity 函数重载
- **估算 Gas**：在发送交易前估算 Gas 消耗

### 工具函数（Utilities）

ethers.js 提供丰富的工具函数库：
- **单位转换**：`parseEther`、`formatEther` 等,在 wei 和 ether 间转换
- **地址操作**：地址校验、校验和格式化、ENS 解析
- **哈希函数**：`keccak256`、`sha256`、`ripemd160` 等
- **ABI 编解码**：`AbiCoder` 用于编码和解码函数调用
- **签名和验证**：签署消息、验证签名、ERC712 结构化签名
- **Big Number**：`BigNumber` 类处理大整数运算,避免精度问题
- **字节操作**：十六进制字符串、Uint8Array、字节拼接等

### TypeScript 支持

ethers.js 使用 TypeScript 编写,提供完整的类型定义：
- **类型安全**：编译时检查类型错误,减少运行时 bug
- **智能提示**：IDE 提供精准的代码补全和参数提示
- **接口定义**：自动从合约 ABI 生成类型化的接口
- **泛型支持**：复杂的泛型类型确保类型推断准确

即使在 JavaScript 项目中,也能通过 `.d.ts` 文件享受类型提示。

### 安全性设计

ethers.js 在设计上高度重视安全：
- **不可变对象**：大部分对象是不可变的,防止意外修改
- **默认安全配置**：Gas 估算、nonce 管理等默认采用安全策略
- **参数验证**：严格验证所有输入参数,防止注入攻击
- **审计和测试**：代码经过严格审计,测试覆盖率高
- **无依赖性**：核心库零依赖,减少供应链攻击风险

## 主要特点

**API 设计优秀**：ethers.js 的 API 简洁直观,符合 JavaScript 开发者的习惯。异步操作使用 Promise,支持 async/await,代码可读性强。

**文档完善**：官方文档详尽,包含 API 参考、迁移指南、教程示例。每个函数都有清晰的说明和代码示例。

**体积小**：核心库压缩后约88KB,远小于 Web3.js。模块化设计允许按需导入,进一步减小打包体积。

**TypeScript 原生**：使用 TypeScript 编写,类型定义准确完整,提供最佳的开发体验。

**活跃维护**：作者 Richard Moore 持续维护,快速响应问题和更新。社区活跃,有大量第三方插件和工具。

**兼容性好**：支持现代浏览器、Node.js、React Native 等多种环境。兼容以太坊主网、测试网和各种 Layer 2、侧链。

**插件生态**：支持插件扩展功能,如硬件钱包集成、ENS 增强、自定义 Provider 等。

## 版本演进

**ethers v4**：早期版本,奠定了 ethers.js 的设计理念和 API 风格。

**ethers v5（2020年）**：重大重构,完全用 TypeScript 重写。改进了 API 设计,增强了类型安全,成为最流行的版本。支持 EIP1559、ENS、ERC20/ERC721 等标准。

**ethers v6（2023年）**：最新版本,进一步现代化。采用 ES2020 特性,使用原生 `BigInt` 替代自定义 `BigNumber`,性能提升。改进了 Provider 和 Wallet API,增强了 WebSocket 支持。更好的 Tree-shaking 支持,减小打包体积。

目前 v5 和 v6 并行维护,v5 仍被广泛使用,v6 逐步成为主流。

## 基本用法示例

**连接以太坊网络**：
```javascript
import { ethers } from 'ethers';

// 连接到以太坊主网（通过默认 Provider）
const provider = ethers.getDefaultProvider('mainnet');

// 或连接到自定义 RPC
const provider = new ethers.JsonRpcProvider('https://eth.llamarpc.com');
```

**查询[账户](https://learnblockchain.cn/tags/账户?map=EVM)余额**：
```javascript
const balance = await provider.getBalance('vitalik.eth');
console.log(ethers.formatEther(balance)); // 将 wei 转换为 ETH
```

**创建钱包并发送交易**：
```javascript
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

const tx = await wallet.sendTransaction({
  to: '0x...',
  value: ethers.parseEther('0.1')
});

await tx.wait(); // 等待交易确认
```

**与[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)交互**：
```javascript
const abi = ['function balanceOf(address) view returns (uint)'];
const contract = new ethers.Contract('0x...', abi, provider);

const balance = await contract.balanceOf('0x...');
```

## 应用场景

**DApp 前端开发**：几乎所有以太坊 [DApp](https://learnblockchain.cn/tags/DApp) 的前端都使用 ethers.js 或 Web3.js 与链交互。ethers.js 轻量、易用,是首选库。

**钱包应用**：MetaMask、Frame、Rainbow 等钱包使用 ethers.js 处理交易签名、余额查询、合约交互等核心功能。

**后端服务**：Node.js 后端使用 ethers.js 监听链上事件、自动化交易、数据索引等。

**自动化脚本**：开发者编写脚本执行批量操作,如空投代币、批量转账、数据统计等。

**测试和部署**：Hardhat、[Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM) 等开发框架集成 ethers.js 用于合约测试和部署脚本。

**链上数据分析**：研究人员使用 ethers.js 提取链上数据,进行分析和可视化。

**机器人和自动化**：MEV 机器人、清算机器人、套利机器人使用 ethers.js 快速响应链上事件。

**教育和原型开发**：简洁的 API 使 ethers.js 成为学习以太坊开发的理想工具。

## 与其他库的比较

**ethers.js vs Web3.js**：
- ethers.js 更轻量（88KB vs 300KB+）
- ethers.js 有更好的 TypeScript 支持
- ethers.js API 更简洁现代
- Web3.js 历史更悠久,生态更成熟
- 两者功能基本等价,可根据喜好选择

**ethers.js vs viem**：
- viem 是新兴的 TypeScript 优先库,性能更优
- viem 使用原生 `BigInt`,更现代
- viem 模块化更好,支持更好的 Tree-shaking
- ethers.js 生态更成熟,文档更完善
- viem 正在快速崛起,可能成为未来主流

## 相关概念

- **Web3.js** - 另一个主流[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) [JavaScript](https://learnblockchain.cn/tags/JavaScript) 库
- **viem** - 新兴的 TypeScript 优先[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)库
- **Hardhat** - 集成 ethers.js 的[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)开发框架
- **MetaMask** - 可与 ethers.js 配合使用的浏览器钱包
- **WalletConnect** - 支持 ethers.js 的[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)连接协议
- **RainbowKit** - 基于 ethers.js/wagmi 的[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)连接组件
- **ERC712** - [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) 支持的结构化数据签名标准

## 相关链接

- 官方网站：https://ethers.org
- GitHub：https://github.com/ethers-io/[ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM)
- v6 文档：https://docs.ethers.org/v6/
- v5 文档：https://docs.ethers.org/v5/
- Playground：https://playground.ethers.org
- Discord：https://discord.gg/6jyGVDK6Jx
- NPM：https://www.npmjs.com/package/ethers
- Twitter：https://twitter.com/ethersproject
