# Gas 机制

## Gas 简介

Gas（燃料）是以太坊网络中用于衡量执行特定操作（如交易转账、[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)计算、存储数据）所需计算工作量的单位。它是以太坊经济模型和安全机制的核心，通过市场化的资源定价机制，确保了网络的安全性、可持续性和防止滥用。

**核心角色：**

```
Gas 在以太坊中的三重作用：

1. 计量单位：
   - 衡量操作的计算复杂度
   - 独立于 ETH 价格波动
   - 反映真实资源消耗

2. 经济激励：
   - 奖励验证者维护网络
   - 优先级费用竞价机制
   - 基础费用销毁（通缩）

3. 安全机制：
   - 防止无限循环（停机问题）
   - 防御 DoS 攻击
   - 限制状态爆炸
```

**历史演进：**

- **2015年**：以太坊主网启动，引入 Gas 机制
- **2017年**：Gas Limit 从 470 万提升至 800 万（应对 ICO 热潮）
- **2021年8月**：伦敦升级（EIP-1559），引入基础费用销毁
- **2022年9月**：合并后转为 [PoS](https://learnblockchain.cn/tags/PoS)，验证者取代矿工获取 Gas 费
- **2024年**：Dencun 升级引入 Blob Gas，降低 L2 成本
- **2025年**：[Fusaka 升级](https://learnblockchain.cn/tags/Fusaka) 将 Blob 数量设计为参数控制，并且设置了单笔交易的gas 上限


## 要解决的问题

作为去中心化的世界计算机，以太坊面临两个关键的资源管理问题：

### 停机问题 (Halting Problem)

EVM 是图灵完备的虚拟机, 可以执行任意复杂的计算, 且图灵证明了没有程序可以预先判断另一个程序（合约程序）是否会停止

因此存在恶意或错误的合约代码可能包含无限循环，导致节点永远陷入死循环，引起网络瘫痪


**示例：无限循环合约**

```solidity
// ❌ 没有 Gas 限制会导致网络瘫痪
contract MaliciousContract {
    function attack() public {
        while (true) {
            // 无限循环
            uint x = 1 + 1;
        }
    }
}

// Gas 机制的保护：
// - 每次循环消耗 Gas
// - Gas 耗尽后交易自动终止
// - 攻击者需支付已消耗的 Gas
// → 攻击成本高昂，不可持续
```

### 资源滥用 (Spam Prevention)

**问题场景：**

```
链上资源的稀缺性：

全节点存储：
- 每个全节点存储完整历史
- 当前以太坊状态：> 1 TB
- 无限增长不可持续

计算资源：
- 验证者需重新执行所有交易
- 复杂计算占用 CPU
- 影响网络吞吐量

网络带宽：
- 交易在 P2P 网络传播
- 过多交易导致拥堵
```

**Gas 防护机制：**

```
成本约束：

免费场景（无 Gas）：
- 攻击者发送 100 万笔垃圾交易
- 成本：0
- 网络瘫痪

有 Gas 机制：
- 每笔交易至少 21,000 Gas
- 100 万笔交易 = 210 亿 Gas
- 成本（50 gwei）：1,050 ETH ≈ $2M+
- 攻击不经济
```

## 核心特性

### Gas 计量机制

**操作码 Gas 成本：**

每个 EVM 操作码都有预定义的 Gas 消耗，反映其计算复杂度和资源占用。

```
常见操作码 Gas 成本表（上海升级后）：

算术运算：
ADD, SUB, MUL, DIV, MOD          3 Gas
ADDMOD, MULMOD                   8 Gas
EXP (指数运算)                   10 + 50/字节

内存操作：
MLOAD (读取内存)                 3 Gas
MSTORE (写入内存)                3 Gas
MSTORE8                          3 Gas

存储操作（最昂贵）：
SLOAD (读取存储)                 2,100 Gas
SSTORE (写入存储)：
  - 零 → 非零                    20,000 Gas
  - 非零 → 非零                  5,000 Gas
  - 非零 → 零（退款）            -15,000 Gas

调用操作：
CALL, CALLCODE                   100 Gas (基础)
DELEGATECALL, STATICCALL         100 Gas
CREATE (创建合约)                32,000 Gas
CREATE2                          32,000 Gas

哈希运算：
SHA3 (keccak256)                 30 + 6/字节
```

**实际案例：简单转账**

```solidity
// ETH 转账：recipient.transfer(amount)
// Gas 消耗分解：

1. 交易基础成本：21,000 Gas
2. Calldata 成本：
   - 零字节：4 Gas/字节
   - 非零字节：16 Gas/字节
   - 地址 (20 字节)：320 Gas
   - 金额 (32 字节)：512 Gas
3. 接收方代码执行：
   - 如果是 EOA：0 Gas
   - 如果是合约（有 receive/fallback）：2,300 Gas 津贴

总计：约 21,000 - 23,300 Gas
```


### EIP-1559 费用模型

```
费用结构：

Transaction Fee = (Base Fee + Priority Fee) × Gas Used

组成部分：

1. Base Fee（基础费用）：
   - 协议自动调整
   - 根据区块拥堵程度
   - 完全销毁（Burn）
   - 不归验证者

2. Priority Fee（优先费/小费）：
   - 用户自定义
   - 给验证者的奖励
   - 激励优先打包

3. Max Fee Per Gas：
   - 用户愿支付的最高价格
   - Max Fee = Max Base Fee + Max Priority Fee

4. Max Priority Fee Per Gas：
   - 愿意支付的最高小费
```

**Base Fee 动态调整算法：**

```
假设目标：每个区块 15M Gas（弹性上限 30M）

调整公式：
New Base Fee = Current Base Fee × (1 + 0.125 × (Parent Gas Used - Target) / Target)

示例：

当前 Base Fee: 100 gwei
上个区块 Gas Used: 20M（超过目标 15M）

New Base Fee = 100 × (1 + 0.125 × (20M - 15M) / 15M)
             = 100 × (1 + 0.125 × 0.333)
             = 100 × 1.0416
             = 104.16 gwei

规则：
- 区块满 → Base Fee 上涨最多 12.5%
- 区块空 → Base Fee 下降最多 12.5%
- 每 12 秒调整一次（每个区块）
```

**实际交易费用计算：**

```javascript
// 用户设置：
Max Fee Per Gas: 200 gwei
Max Priority Fee Per Gas: 2 gwei

// 当前网络状态：
Current Base Fee: 50 gwei

// 实际费用计算：
Actual Base Fee = 50 gwei（当前基础费）
Actual Priority Fee = min(2 gwei, 200 - 50) = 2 gwei

Effective Gas Price = 50 + 2 = 52 gwei

// Gas 使用：100,000 Gas
Transaction Fee = 100,000 × 52 gwei
                = 5,200,000 gwei
                = 0.0052 ETH

// 费用分配：
Burned (Base Fee): 100,000 × 50 = 0.005 ETH  → 永久销毁
To Validator: 100,000 × 2 = 0.0002 ETH       → 验证者收入

// 用户退款：
Max Willing to Pay: 100,000 × 200 = 0.02 ETH
Actual Paid: 0.0052 ETH
Refund: 0.0148 ETH
```

### Gas Limit（Gas 限制）

**交易 Gas Limit：**

```
定义：用户为单笔交易设置的最大 Gas 消耗量

作用：
1. 防止意外消耗过多 Gas
2. 控制交易成本上限
3. 避免合约 Bug 导致资金耗尽

如果实际消耗 < Gas Limit：
- 仅支付实际消耗的 Gas
- 剩余 Gas 退还给用户

如果实际消耗 = Gas Limit：
- 交易可能成功（刚好够用）
- 或失败（Out of Gas）
- 已消耗的 Gas 不退还
```

**区块 Gas Limit：**

```
定义：单个区块允许包含的最大总 Gas 量

当前设置（2025底）：
- 目标：30,000,000 Gas
- 弹性上限：60,000,000 Gas

影响：
- 决定区块大小
- 限制网络吞吐量
- 影响交易确认时间
```

**Gas Limit 估算方法：**

```javascript
// 方法 1：eth_estimateGas（最常用）
const gasEstimate = await provider.estimateGas({
    to: contractAddress,
    data: encodedFunctionCall
});

// 建议加 10-20% 缓冲
const gasLimit = gasEstimate * 1.2;

```

## Gas 成本详解

* 存储成本（最昂贵）， 必要时，通过缓存到内存和变量打包来优化 Gas
* 内存成本：初期线性增长，后期二次方增长（防止滥用）
* Calldata 成本：最便宜

### 事件成本

**LOG 操作码成本：**

```
事件 Gas 成本 = 基础成本 + 主题成本 + 数据成本

LOG0 (无主题)：       375 Gas
LOG1 (1 个主题)：     375 + 375 = 750 Gas
LOG2 (2 个主题)：     375 + 375×2 = 1,125 Gas
LOG3 (3 个主题)：     375 + 375×3 = 1,500 Gas
LOG4 (4 个主题)：     375 + 375×4 = 1,875 Gas

数据成本：8 Gas/字节

示例：
event Transfer(address indexed from, address indexed to, uint256 value);

emit Transfer(0xaaa..., 0xbbb..., 100);

成本计算：
- 基础：375 Gas
- 3 个主题（事件签名 + from + to）：375 × 3 = 1,125 Gas
- 数据（value，32字节）：32 × 8 = 256 Gas
总计：1,756 Gas
```

**事件优化：**

```solidity
// ❌ 低效：过多 indexed 参数
event IneffientEvent(
    address indexed user,
    address indexed token,
    address indexed spender,
    uint256 amount
);
// 成本：375 + 375×4 + 32×8 = 1,881 Gas

// ✅ 高效：平衡 indexed 和数据
event EfficientEvent(
    address indexed user,
    address token,      // 不索引
    uint256 amount
);
// 成本：375 + 375×2 + (20+32)×8 = 1,541 Gas
// 节省：340 Gas

// 权衡：
// - indexed 参数：方便链下查询（可过滤）
// - 非 indexed：节省 Gas，但查询需遍历
```

### 合约部署成本

**CREATE 和 CREATE2 成本：**

```
部署成本 = 基础成本 + 代码存储成本 + 初始化成本

基础成本：
CREATE: 32,000 Gas
CREATE2: 32,000 Gas（相同）

代码存储成本：
200 Gas/字节

示例：
合约字节码大小：10,000 字节

成本计算：
- 基础：32,000 Gas
- 代码存储：10,000 × 200 = 2,000,000 Gas
- 构造函数执行：变量（例如 500,000 Gas）
总计：约 2,532,000 Gas

实际成本（50 gwei）：
2,532,000 × 50 gwei = 0.1266 ETH ≈ $250
```


### 实际成本案例

**案例 1：简单 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 转账**

```solidity
// ERC20.transfer(recipient, 1000)

Gas 消耗分解：
1. 交易基础成本                  21,000 Gas
2. Calldata（68字节）             ~900 Gas
3. SLOAD balances[sender]         2,100 Gas
4. SLOAD balances[recipient]      2,100 Gas
5. SSTORE balances[sender]        5,000 Gas（修改）
6. SSTORE balances[recipient]     5,000 Gas（修改）
7. Transfer 事件                  1,756 Gas
8. 计算和检查                     ~500 Gas

总计：约 65,000 Gas

成本（50 gwei）：
65,000 × 50 gwei = 0.00325 ETH ≈ $6.5
```

**案例 2：[Uniswap](https://learnblockchain.cn/tags/Uniswap?map=EVM) V2 Swap**

```javascript
// swapExactTokensForTokens

Gas 消耗分解：
1. 交易基础                      21,000 Gas
2. Router 函数调用               ~2,000 Gas
3. Token A transferFrom          65,000 Gas
4. Pair getReserves (SLOAD ×2)   4,200 Gas
5. Pair swap 逻辑：
   - 恒定乘积检查                ~1,000 Gas
   - 储备量更新 (SSTORE ×2)      10,000 Gas
   - Sync 事件                   1,756 Gas
6. Token B transfer to user      65,000 Gas
7. 其他计算和检查                ~5,000 Gas

总计：约 175,000 Gas

成本（50 gwei）：
175,000 × 50 gwei = 0.00875 ETH ≈ $17.5
```

## Gas 优化技术
阅读：[Gas 优化手册](https://learnblockchain.cn/course/95)

## 主要特点

*   **去中心化计价**：不依赖中心化机构，而是由市场供需和协议算法动态决定资源价格。
*   **通缩机制**：EIP-1559 引入的 Base Fee 销毁机制，使得在网络活跃时，ETH 的销毁量可能超过发行量，从而实现通缩。
*   **细粒度控制**：不同的操作（计算密集型 vs 存储密集型）根据其对节点资源的占用程度有不同的定价。

## 推荐阅读

*   [Gas 优化手册](https://learnblockchain.cn/course/95) - 系统的 Gas 优化技巧
*   [EIP-1559: Fee market change for ETH 1.0 chain](https://learnblockchain.cn/docs/eips/EIPS/eip-1559) - EIP-1559 完整规范
*   [EVM Opcodes Gas Costs](https://www.evm.codes/) - 完整的 EVM 操作码 Gas 成本表
*   [Ethereum Gas Tracker](https://etherscan.io/gastracker) - 实时 Gas 价格监控
*   [EIP-2929: Gas cost increases for state access opcodes](https://learnblockchain.cn/docs/eips/EIPS/eip-2929) - 冷热访问机制
*   [EIP-2200: Structured Definitions for Net Gas Metering](https://learnblockchain.cn/docs/eips/EIPS/eip-2200) - SSTORE Gas 成本优化


## 相关概念

*   **Gwei**：Gas 价格的常用单位，1 Gwei = $10^{-9}$ ETH
*   **Wei**：[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)最小单位，1 ETH = $10^{18}$ Wei
*   **Gas Limit (Transaction)**：单笔交易允许消耗的最大 Gas 量
*   **Gas Limit (Block)**：单个区块允许包含的最大总 Gas 量，决定区块大小
*   **Base Fee**：[EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM) 引入的基础费用，动态调整并销毁
*   **Priority Fee**：优先费/小费，奖励给验证者
*   **[EIP-1559](https://learnblockchain.cn/tags/EIP1559?map=EVM)**：伦敦升级引入的费用市场改革
*   **Out of Gas**：Gas 耗尽导致的交易失败
*   **Gas Refund**：某些操作（如存储清除）可获得 Gas 退款
*   **MEV (最大可提取价值)**：验证者通过重新排序交易获取额外收益
*   **[EVM](https://learnblockchain.cn/tags/EVM?map=EVM) ([以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)虚拟机)**：执行[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)的虚拟机
*   **Opcode**：[EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 操作码，每个有固定 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本
*   **SLOAD/SSTORE**：存储读写操作，成本最高
*   **Calldata**：交易输入数据
*   **Block Gas Target**：目标区块 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 使用量（15M）
