## Delegatecall

`delegatecall` 是以太坊虚拟机 (EVM) 中的一个低级操作码，它允许一个合约（调用者）执行另一个合约（目标合约）的代码，但**保留调用者的上下文**。

### 解决的问题
在智能合约开发中，主要解决两个问题：
1.  **代码复用 (库合约):** 允许不同的合约复用同一段逻辑代码，而不需要在每个合约中都部署一份副本。
2.  **合约升级 (代理模式):** 允许在不改变合约地址和状态的情况下更新业务逻辑。

### 实现机制与原理
当合约 A 对合约 B 执行 `delegatecall` 时：
*   **代码执行:** 执行的是合约 B 的代码。
*   **存储 (Storage):** 修改的是合约 A 的存储。合约 B 的代码通过存储槽 (Storage Slot) 的索引来读写数据，这些操作实际作用于合约 A 的对应槽位。
*   **上下文 (Context):**
    *   `msg.sender`: 保持不变（即最初调用合约 A 的用户）。
    *   `msg.value`: 保持不变。
    *   `address(this)`: 指向合约 A 的地址。

与之相对的是普通的 `call`，在 `call` 中，代码在被调用者（合约 B）的上下文中运行，修改的是合约 B 的存储，`msg.sender` 变为合约 A。

### 安全风险
`delegatecall` 非常强大，但也极其危险，主要风险包括：
1.  **存储冲突 (Storage Collision):**
    *   这是最常见的漏洞。如果合约 A 和合约 B 的状态变量定义的顺序或类型不完全一致，合约 B 的代码可能会错误地覆盖合约 A 中的关键变量（如修改了合约 A 的 owner 地址）。
    *   在代理模式中，通常通过非结构化存储 (Unstructured Storage) 或 EIP-1967 标准槽位来避免冲突。
2.  **权限接管:**
    *   如果攻击者能够让合约 A 对一个恶意合约发起 `delegatecall`（例如合约 A 允许用户指定目标地址），恶意合约可以包含 `selfdestruct` 指令销毁合约 A，或者修改合约 A 的所有者。

### 主要特点
*   **逻辑与状态分离:** 实现了将业务逻辑（代码）与数据（状态）分开存储的架构。
*   **节省 Gas:** 对于大型库函数，使用 `delegatecall` 比复制代码更节省部署成本。
*   **原子性:** 操作在同一个交易上下文中完成。

### 推荐阅读
*   [Solidity Docs: Delegatecall](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html#delegatecall-callcode-and-libraries)
*   [Proxy Patterns & Storage Collisions](https://blog.openzeppelin.com/proxy-patterns/)

### 相关概念
*   **Proxy Contract:** 代理合约，广泛使用 `delegatecall` 将调用转发给逻辑合约。
*   **Library:** Solidity 库，如果是 `internal` 函数，会被内联到合约中；如果是 `public/external` 函数，调用时通常使用 `delegatecall`。
*   **Storage Layout:** 存储布局，使用 `delegatecall` 时必须严格对齐。
