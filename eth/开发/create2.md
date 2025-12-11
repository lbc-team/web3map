## Create2

`CREATE2` 是以太坊在君士坦丁堡 (Constantinople) 升级中引入的一个操作码 (EIP-1014)，它允许在合约部署之前就确定性地计算出合约的地址。

### 解决的问题
使用传统的 `CREATE` 操作码部署合约时，新合约的地址由发送者的地址 (`sender`) 和发送者当前的 `nonce` 决定 (`keccak256(sender, nonce)`). 这意味着如果 `nonce` 发生变化（例如发送了其他交易），预测的地址就会失效。
`CREATE2` 使得合约地址的生成与 `nonce` 无关，而是依赖于合约的初始化代码、发送者地址和一个用户提供的“盐值” (salt)。这使得即使合约尚未部署，用户也可以安全地向该未来地址发送资金或与其交互（反事实交互）。

### 实现机制与原理
`CREATE2` 的地址计算公式如下：
```
address = keccak256(0xff ++ senderAddress ++ salt ++ keccak256(init_code))[12:]
```
*   `0xff`: 一个常数，用于防止与 `CREATE` 操作码生成的地址冲突。
*   `senderAddress`: 部署合约的工厂合约地址（或调用者地址）。
*   `salt`: 一个 32 字节的随机数或特定值，由开发者指定。
*   `init_code`: 待部署合约的初始化字节码（包含构造函数逻辑）。

只要这三个参数确定，合约的地址就是固定的，无论何时部署。

### 主要特点
*   **确定性地址:** 可以在链下预先计算合约地址。
*   **反事实实例化 (Counterfactual Instantiation):** 允许与尚未在链上存在的合约进行交互（例如充值），只要确信该合约未来会被正确部署。
*   **状态通道:** 在状态通道中，参与者可以签署状态更新，声称如果发生争议，将部署特定的仲裁合约。`CREATE2` 保证了该仲裁合约地址的一致性。
*   **Metamorphic Contracts (变形合约):** 结合 `SELFDESTRUCT` 和 `CREATE2`，可以在同一个地址重新部署代码不同的合约（通过改变 `init_code` 中的逻辑但保持 `keccak256(init_code)` 不变，通常利用代理模式或特定技巧），实现“原地升级”或代码修改。

### 推荐阅读
*   [EIP-1014: Skinny CREATE2](https://learnblockchain.cn/docs/eips/EIPS/eip-1014)
*   [Metamorphic Smart Contracts](https://0age.com/)

### 相关概念
*   **Nonce:** 交易计数器，传统合约地址生成的关键参数。
*   **Factory Pattern:** 工厂模式通常利用 `CREATE2` 来部署确定性地址的子合约。
*   **Salt:** 用于干扰哈希结果的随机数据。
