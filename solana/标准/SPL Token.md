## SPL Token

[SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) 是 Solana 上的代币标准，相当于以太坊的 ERC-20。SPL（Solana Program Library）Token 程序定义了如何在 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 上创建、管理和转移可替代和不可替代代币。

### 核心概念

**Mint [账户](https://learnblockchain.cn/tags/账户?map=EVM)**
代币的定义和配置：
- 代币总供应量
- 小数位数
- 铸币权限（Mint Authority）
- 冻结权限（Freeze Authority）

**Token 账户**
存储用户的代币余额：
- 所属的 Mint
- 所有者（Owner）
- 余额（Amount）
- 委托信息（Delegate）

**关联 Token 账户（ATA）**
用户的默认 Token 账户，地址由用户钱包和 Mint 派生（[PDA](https://learnblockchain.cn/tags/PDA?map=Solana)）。

### 创建代币

```bash
# 创建 Mint
spl-token create-token

# 创建 Token 账户
spl-token create-account <MINT>

# 铸造代币
spl-token mint <MINT> <AMOUNT>

# 转账
spl-token transfer <MINT> <AMOUNT> <RECIPIENT>
```

### 代币操作

**铸造**
只有拥有 Mint Authority 的账户才能铸造新代币。

**销毁**
用户可以销毁自己的代币，减少总供应量。

**冻结**
如果设置了 Freeze Authority，可以冻结特定 Token 账户。

**委托**
允许其他账户代表你转移一定数量的代币。

### Token-2022

[SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) 的升级版，增加了：
- 转账手续费
- 转账钩子
- 保密转账
- 元数据扩展
- 兴趣bearing代币

### 相关概念

- **[ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM)**：以太坊的可替代代币标准
- **ATA**：关联 Token 账户
- **Token-2022**：[SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) 的扩展版本
