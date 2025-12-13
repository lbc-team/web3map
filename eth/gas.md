# Gas 机制

## 概念简介

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

**问题根源：**

```
图灵完备性的代价：
- EVM 是图灵完备的虚拟机
- 可以执行任意复杂的计算
- 无法预先判断程序是否会停止

风险：
恶意或错误的代码可能包含无限循环
→ 节点永远陷入死循环
→ 网络瘫痪
```

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

逻辑运算：
LT, GT, EQ, ISZERO               3 Gas
AND, OR, XOR, NOT                3 Gas
BYTE, SHL, SHR                   3 Gas

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
SELFDESTRUCT                     5,000 Gas

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

**伦敦升级（2021年8月）前后对比：**

```
传统拍卖模型（EIP-1559 之前）：

Gas Price = 用户出价
- 单一价格竞价
- 拥堵时 Gas Price 暴涨
- 费用难以预测
- 全部费用给矿工

问题：
用户 A 出价：50 gwei
用户 B 出价：51 gwei  ← 抢先打包
用户 C 出价：100 gwei ← 更优先
→ Gas 竞价战，费用不可控
```

**EIP-1559 新模型：**

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



**Gas Limit 过低/过高的影响：**

```solidity
// 场景 1：Gas Limit 过低
用户设置：Gas Limit = 100,000
实际需要：150,000 Gas

执行过程：
1. 交易开始执行
2. 执行到 100,000 Gas 时耗尽
3. 抛出 "Out of Gas" 错误
4. 所有状态更改回滚
5. 100,000 Gas 费用已支付（不退还）

结果：
✗ 交易失败
✗ 损失 Gas 费
✗ 浪费时间

// 场景 2：Gas Limit 过高
用户设置：Gas Limit = 1,000,000
实际需要：150,000 Gas

执行过程：
1. 交易执行完成
2. 实际消耗 150,000 Gas
3. 剩余 850,000 Gas 退还

结果：
✓ 交易成功
✓ 仅支付实际消耗
✓ 多余 Gas 退还

注意：
- 设置过高的 Gas Limit 没有额外成本
- 但会影响交易能否被打包（见区块 Gas Limit）
```

**区块 Gas Limit：**

```
定义：单个区块允许包含的最大总 Gas 量

当前设置（2025低）：
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

// 方法 2：静态调用测试
const result = await contract.callStatic.myFunction(params);
// 如果成功，再发送实际交易

// 方法 3：历史数据
// 查询相同函数的历史交易
// 使用 90th percentile 作为参考

// 方法 4：Hardhat/Foundry 测试
// 在本地测试网精确测量
it("should measure gas", async () => {
    const tx = await contract.myFunction();
    const receipt = await tx.wait();
    console.log("Gas used:", receipt.gasUsed);
});
```

### 失败处理与退款

**Out of Gas 失败：**

```
执行流程：

1. 用户提交交易
   Gas Limit: 100,000
   Gas Price: 50 gwei

2. 验证者开始执行
   ├─ 基础成本：21,000 Gas
   ├─ 函数执行：30,000 Gas
   ├─ 存储写入：20,000 Gas
   ├─ 更多操作：29,000 Gas
   └─ 总计 100,000 Gas（耗尽）

3. 尝试下一个操作（需要 2,100 Gas）
   → Out of Gas！

4. 回滚所有状态更改
   - 存储更改撤销
   - 余额变化撤销
   - 事件不会发出

5. 费用处理
   已消耗：100,000 Gas × 50 gwei = 0.005 ETH
   → 不退还（验证者已执行工作）

结果：
✗ 交易标记为失败
✗ 用户损失 0.005 ETH
✗ 状态未改变
```

**Gas 退款机制：**

```
可退款场景：

1. 存储清除（SSTORE 非零 → 零）：
   退款：15,000 Gas

   示例：
   mapping(address => uint) balances;
   balances[user] = 100;  // 写入 20,000 Gas
   balances[user] = 0;    // 清除 -15,000 Gas（退款）

2. SELFDESTRUCT（合约自毁）：
   退款：24,000 Gas

   注意：坎昆升级后已移除此退款

3. 退款上限：
   最大退款 = 实际消耗 Gas / 5

   示例：
   消耗：100,000 Gas
   理论退款：30,000 Gas
   实际退款：min(30,000, 100,000/5) = 20,000 Gas

   净消耗：80,000 Gas

历史变化：
- 伦敦升级前：最大退款 = 消耗 Gas / 2
- 伦敦升级后：最大退款 = 消耗 Gas / 5
- 坎昆升级：移除 SELFDESTRUCT 退款
```

**交易执行结果示例：**

```javascript
// 成功交易的 Receipt
{
    status: 1,  // 成功
    gasUsed: 150000,  // 实际消耗
    effectiveGasPrice: 52000000000,  // 52 gwei

    // 费用计算
    transactionFee: 150000 × 52 gwei = 0.0078 ETH
}

// 失败交易的 Receipt
{
    status: 0,  // 失败
    gasUsed: 100000,  // Gas Limit（全部消耗）
    effectiveGasPrice: 50000000000,  // 50 gwei

    // 费用计算（不退还）
    transactionFee: 100000 × 50 gwei = 0.005 ETH

    // 错误信息
    revertReason: "ERC20: transfer amount exceeds balance"
}
```

## Gas 成本详解

### 存储成本（最昂贵）

**SSTORE 成本矩阵：**

```
存储操作的 Gas 成本（EIP-2200 后）：

初始值 → 目标值                     成本

零值 → 非零值（新增）               20,000 Gas
  - 首次写入
  - 占用新存储槽

非零值 → 不同非零值（修改）         5,000 Gas
  - 修改现有值
  - 不占用新槽

非零值 → 零值（清除）               5,000 Gas - 15,000 Gas 退款
  - 释放存储空间
  - 净成本：-10,000 Gas（实际节省）

零值 → 零值（无操作）               2,100 Gas (SLOAD 成本)
  - 仅读取检查

同值 → 同值（无变化）               2,100 Gas
  - Dirty case（同一交易内重复写入）
```

**SLOAD 成本：**

```
冷热访问机制（EIP-2929）：

首次访问（冷）：2,100 Gas
- 从存储加载到内存
- 缓存未命中

后续访问（热）：100 Gas
- 已在内存中
- 缓存命中

示例：
function multipleReads() public view {
    uint a = value;      // 2,100 Gas（冷访问）
    uint b = value;      // 100 Gas（热访问）
    uint c = value;      // 100 Gas（热访问）
}
// 总计：2,300 Gas
```

**优化技巧：**

```solidity
// ❌ 低效：多次 SLOAD
function inefficient() public {
    for (uint i = 0; i < 10; i++) {
        // 每次循环读取 totalSupply（2,100 Gas × 10 = 21,000 Gas）
        if (balances[msg.sender] < totalSupply / 10) {
            revert("Insufficient balance");
        }
    }
}

// ✅ 高效：缓存到内存
function efficient() public {
    uint _totalSupply = totalSupply;  // 2,100 Gas（一次）
    for (uint i = 0; i < 10; i++) {
        // 使用内存变量（3 Gas × 10 = 30 Gas）
        if (balances[msg.sender] < _totalSupply / 10) {
            revert("Insufficient balance");
        }
    }
}
// 节省：21,000 - 2,130 = 18,870 Gas
```

**打包存储：**

```solidity
// ❌ 低效：每个变量占一个槽（32 字节）
contract Inefficient {
    uint8 a;      // slot 0（浪费 31 字节）
    uint8 b;      // slot 1（浪费 31 字节）
    uint256 c;    // slot 2
}
// 写入成本：3 × 20,000 = 60,000 Gas

// ✅ 高效：打包到同一个槽
contract Efficient {
    uint8 a;      // slot 0 (byte 0)
    uint8 b;      // slot 0 (byte 1)
    uint240 c;    // slot 0 (byte 2-31)
}
// 写入成本：1 × 20,000 = 20,000 Gas
// 节省：40,000 Gas

// ✅ 更好的打包
contract BestPractice {
    // 将相关的小类型变量组合在一起
    address owner;      // slot 0 (20 bytes)
    uint96 balance;     // slot 0 (12 bytes) - 总共32字节

    bool isActive;      // slot 1 (1 byte)
    uint8 status;       // slot 1 (1 byte)
    uint64 timestamp;   // slot 1 (8 bytes)
    // slot 1 还剩余 22 字节
}
```

### 内存成本

**内存扩展成本：**

```
内存成本公式：
Memory Cost = (Memory Size in words)² / 512 + 3 × (Memory Size in words)

示例计算：

使用 32 字节内存（1 word）：
Cost = 1²/512 + 3×1 = 3 Gas

使用 320 字节内存（10 words）：
Cost = 10²/512 + 3×10 = 30.19 ≈ 31 Gas

使用 1024 字节内存（32 words）：
Cost = 32²/512 + 3×32 = 98 Gas

使用 10240 字节内存（320 words）：
Cost = 320²/512 + 3×320 = 1,160 Gas

规律：
- 初期线性增长
- 后期二次方增长（防止滥用）
```

**内存优化：**

```solidity
// ❌ 低效：频繁扩展内存
function inefficient(uint[] calldata data) public {
    for (uint i = 0; i < data.length; i++) {
        bytes memory temp = new bytes(1024);  // 每次分配 1KB
        // 内存不断扩展，成本指数增长
    }
}

// ✅ 高效：复用内存
function efficient(uint[] calldata data) public {
    bytes memory temp = new bytes(1024);  // 一次分配
    for (uint i = 0; i < data.length; i++) {
        // 复用同一块内存
        assembly {
            mstore(add(temp, 32), data[i])
        }
    }
}
```

### Calldata 成本

**Calldata Gas 成本：**

```
字节类型成本（EIP-2028 后）：

零字节（0x00）：4 Gas/字节
非零字节：16 Gas/字节

示例交易：
function transfer(address to, uint256 amount)

Calldata 分析：
0xa9059cbb  // 函数选择器（4字节非零）
0000000000000000000000001234567890123456789012345678901234567890  // to 地址
0000000000000000000000000000000000000000000000000000000000000064  // amount = 100

成本计算：
- 函数选择器：4 × 16 = 64 Gas
- to 地址：12 × 4 + 8 × 16 = 176 Gas（12个零字节 + 8个非零）
- amount：31 × 4 + 1 × 16 = 140 Gas（31个零字节 + 1个非零）
总计：380 Gas
```

**Calldata 优化：**

```solidity
// ❌ 低效：大量零字节
function inefficient(uint256 amount) public {
    // amount = 1
    // 编码：0x0000000000000000000000000000000000000000000000000000000000000001
    // 31 × 4 + 1 × 16 = 140 Gas
}

// ✅ 高效：使用更小的类型
function efficient(uint128 amount) public {
    // amount = 1
    // 编码：0x00000000000000000000000000000001（16字节）
    // 15 × 4 + 1 × 16 = 76 Gas
    // 节省：64 Gas
}

// ✅ 更激进：使用 uint8（适合小数值）
function mostEfficient(uint8 amount) public {
    // 编码：0x01（1字节）
    // 1 × 16 = 16 Gas
    // 节省：124 Gas
}

// 注意权衡：
// - 小类型节省 calldata 成本
// - 但在 EVM 内部仍需转换为 256 位
// - 仅当频繁外部调用时值得优化
```

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

**大型合约问题：**

```
合约大小限制（EIP-170）：
最大：24,576 字节 (24 KB)

超出限制的解决方案：

1. Diamond Pattern（钻石模式）
   - 拆分功能到多个 Facet
   - 通过 Diamond Proxy 聚合

2. Proxy Pattern（代理模式）
   - 逻辑合约可随时更换
   - 单个逻辑合约 < 24 KB

3. 代码优化
   - 使用库（Library）
   - 移除未使用代码
   - 优化器设置

4. 链下存储
   - IPFS 存储元数据
   - 链上仅存哈希
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

**案例 3：[NFT](https://learnblockchain.cn/tags/NFT) Mint**

```solidity
// ERC721.mint(to, tokenId)

Gas 消耗分解：
1. 交易基础                      21,000 Gas
2. Calldata                      ~1,000 Gas
3. _safeMint 检查                ~5,000 Gas
4. SSTORE _owners[tokenId]       20,000 Gas（新增）
5. SSTORE _balances[to]          5,000 Gas（修改）
6. Transfer 事件                 1,756 Gas
7. 元数据 URI 设置（可选）        20,000+ Gas
8. onERC721Received 回调         ~2,300 Gas

总计：约 250,000 Gas（含元数据）

成本（50 gwei）：
250,000 × 50 gwei = 0.0125 ETH ≈ $25
```

## Gas 优化技术

### 存储优化

**技巧 1：变量打包**

```solidity
// ❌ Before（3 个槽）
contract Before {
    uint128 a;    // slot 0
    uint256 b;    // slot 1
    uint128 c;    // slot 2
}
// 写入成本：60,000 Gas

// ✅ After（2 个槽）
contract After {
    uint128 a;    // slot 0
    uint128 c;    // slot 0
    uint256 b;    // slot 1
}
// 写入成本：40,000 Gas
// 节省：20,000 Gas (33%)
```

**技巧 2：短路逻辑**

```solidity
// ❌ 低效
function inefficient() public view returns (bool) {
    return expensiveCheck() && cheapCheck();
    // 总是执行 expensiveCheck
}

// ✅ 高效
function efficient() public view returns (bool) {
    return cheapCheck() && expensiveCheck();
    // cheapCheck 失败时跳过 expensiveCheck
}
```

**技巧 3：使用常量和不可变变量**

```solidity
// ❌ 状态变量（每次 SLOAD: 2,100 Gas）
contract Inefficient {
    uint256 public MAX_SUPPLY = 10000;

    function mint() public {
        require(totalSupply < MAX_SUPPLY);  // SLOAD
    }
}

// ✅ 常量（直接嵌入字节码：0 Gas）
contract Efficient {
    uint256 public constant MAX_SUPPLY = 10000;

    function mint() public {
        require(totalSupply < MAX_SUPPLY);  // 无 SLOAD
    }
}
// 节省：2,100 Gas/次调用
```

### 循环优化

```solidity
// ❌ 低效循环
function inefficient(uint[] memory arr) public {
    for (uint i = 0; i < arr.length; i++) {  // arr.length 每次读取
        // 处理 arr[i]
    }
}

// ✅ 高效循环
function efficient(uint[] memory arr) public {
    uint length = arr.length;  // 缓存长度
    for (uint i; i < length;) {  // i 初始化为 0（节省 3 Gas）
        // 处理 arr[i]

        unchecked { ++i; }  // 避免溢出检查（节省 ~40 Gas/次）
    }
}
```

### 函数优化

**技巧 1：External vs Public**

```solidity
// ❌ Public（可内部调用）
function publicFunc(uint[] memory data) public {
    // memory 复制成本高
}

// ✅ External（仅外部调用）
function externalFunc(uint[] calldata data) external {
    // calldata 直接读取，无复制
}
// 节省：视数组大小，可达数千 Gas
```

**技巧 2：函数修饰符顺序**

```solidity
// ❌ 昂贵检查在前
modifier expensiveCheck() {
    require(someComplexCondition());  // 昂贵
    _;
}

modifier cheapCheck() {
    require(msg.sender == owner);  // 便宜
    _;
}

function bad() public expensiveCheck cheapCheck {
    // 总是先执行昂贵检查
}

// ✅ 便宜检查在前
function good() public cheapCheck expensiveCheck {
    // owner 检查失败时跳过昂贵检查
}
```

### 字节码优化

**[Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 编译器优化器：**

```javascript
// hardhat.config.js
module.exports = {
    solidity: {
        version: "0.8.20",
        settings: {
            optimizer: {
                enabled: true,
                runs: 200  // 部署与运行成本平衡
            }
        }
    }
};

// Runs 参数影响：
runs = 1:     优化部署成本（部署便宜，运行昂贵）
runs = 200:   平衡（默认）
runs = 10000: 优化运行成本（部署昂贵，运行便宜）

示例：
Runs = 1:    部署 2M Gas，调用 50k Gas
Runs = 200:  部署 2.5M Gas，调用 30k Gas  ← 推荐
Runs = 10000: 部署 3M Gas，调用 25k Gas
```

## 主要特点

*   **去中心化计价**：不依赖中心化机构，而是由市场供需和协议算法动态决定资源价格。
*   **通缩机制**：EIP-1559 引入的 Base Fee 销毁机制，使得在网络活跃时，ETH 的销毁量可能超过发行量，从而实现通缩。
*   **细粒度控制**：不同的操作（计算密集型 vs 存储密集型）根据其对节点资源的占用程度有不同的定价。

## 推荐阅读

*   [Ethereum.org: Gas and Fees](https://ethereum.org/en/developers/docs/gas/) - 官方 Gas 机制文档
*   [EIP-1559: Fee market change for ETH 1.0 chain](https://learnblockchain.cn/docs/eips/EIPS/eip-1559) - EIP-1559 完整规范
*   [EVM Opcodes Gas Costs](https://www.evm.codes/) - 完整的 EVM 操作码 Gas 成本表
*   [Ethereum Gas Tracker](https://etherscan.io/gastracker) - 实时 Gas 价格监控
*   [EIP-2929: Gas cost increases for state access opcodes](https://learnblockchain.cn/docs/eips/EIPS/eip-2929) - 冷热访问机制
*   [EIP-2200: Structured Definitions for Net Gas Metering](https://learnblockchain.cn/docs/eips/EIPS/eip-2200) - SSTORE Gas 成本优化
*   [Solidity Gas Optimization Tips](https://gist.github.com/hrkrshnn/ee8fabd532058307229d65dcd5836ddc) - Gas 优化技巧合集
*   [Understanding Gas in Ethereum](https://ethereum.org/en/developers/docs/gas/) - Gas 机制深入解析

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
