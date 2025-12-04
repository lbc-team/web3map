# Stacks

Stacks (前身为 Blockstack) 是一个独立的 Layer 1 区块链，旨在将智能合约和去中心化应用（DApps）引入比特币生态系统，而无需修改比特币本身。它通过其独特的“传输证明”（Proof of Transfer, PoX）共识机制与比特币区块链锚定，从而实现智能合约在比特币安全保障下的执行。

## 要解决的问题

比特币主链以其强大的安全性和去中心化而闻名，但其脚本语言功能有限，难以支持复杂的智能合约和 DApps。Stacks 旨在解决：

1.  **比特币的可编程性限制**：如何在不牺牲比特币核心价值的前提下，为比特币生态带来图灵完备的智能合约能力。
2.  **安全性继承**：确保在 Stacks 上构建的 DApps 能够继承比特币主链的安全性，而不是依赖于独立的信任假设。
3.  **开发者体验**：提供一个现代化的智能合约编程环境（Clarity 语言），吸引开发者在比特币的基础上构建。

## 实现机制与原理

Stacks 采用了一个名为**传输证明（Proof of Transfer, PoX）**的独特共识机制，它是工作量证明（PoW）和权益证明（PoS）的混合体，连接了 Stacks 链和比特币链。

### 传输证明 (Proof of Transfer, PoX)
PoX 是 Stacks 的核心创新。它解决了如何让 Stacks 链的状态更新能够安全地锚定到比特币链上的问题。
1.  **矿工**：Stacks 矿工通过“承诺”一定数量的比特币（将 BTC 发送到一个预设的比特币地址，这些 BTC 会被锁定）来竞争新的 Stacks 区块。比特币链上的最新区块哈希作为 Stacks 矿工挖矿的输入。
2.  **堆叠者 (Stackers)**：STX 代币的持有者可以将他们的 STX 代币锁定一段时间（“堆叠”），并参与共识。他们将获得 Stacks 矿工用于承诺的比特币作为奖励。
3.  **比特币锚定**：每次 Stacks 区块的提交，其哈希值都会被嵌入到比特币区块链的一个交易中。这使得 Stacks 链的整个历史都安全地锚定在比特币上。

### Clarity 智能合约语言
Stacks 引入了一种名为 Clarity 的智能合约编程语言。Clarity 是一种可判定的（Decidable）语言，这意味着在合约执行之前，可以静态地分析出其行为，从而避免了常见的智能合约漏洞和安全风险。Clarity 代码直接部署在 Stacks 区块链上。

### 区块链结构
Stacks 链是一个独立的 Layer 1 区块链，拥有自己的共识机制和代币（STX）。然而，它的状态通过 PoX 机制，定期且安全地锚定在比特币区块链上。比特币是 Stacks 的安全基石。

## 主要特点

*   **比特币安全性**：通过 PoX 共识机制，Stacks 链的安全性与比特币主链深度绑定，其状态更新最终由比特币网络保证。
*   **图灵完备智能合约**：Clarity 语言支持复杂的智能合约逻辑，为比特币生态带来了强大的可编程性。
*   **资产所有权与交易**：Stacks 上的所有交易和资产（包括 NFT、DeFi 等）都可以在比特币网络上进行最终结算。
*   **可预测的 Gas 费用**：Clarity 的可判定性有助于避免运行时错误和意外的 Gas 消耗。
*   **双代币经济**：比特币（BTC）用于 Stacks 网络的安全性承诺和奖励分配，STX 代币用于 Stacks 链上的交易费用和质押。

## 推荐阅读

*   [Stacks Whitepaper](https://stacks.co/stacks.pdf)
*   [Stacks Documentation](https://docs.stacks.co/)
*   [Clarity Language Documentation](https://docs.stacks.co/references/clarity)

## 相关概念

*   **传输证明 (Proof of Transfer, PoX)**
*   **Clarity 语言**
*   **比特币锚定**
*   **STX 代币**
*   **Layer 1 区块链**
