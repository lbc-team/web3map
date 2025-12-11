# PBS

## 概念简介

PBS（Proposer-Builder Separation，提议者-构建者分离）是以太坊的一项架构设计，将区块生产任务拆分为两个独立角色：区块构建者（Builder）负责创建区块内容，区块提议者（Proposer）负责选择并提议区块。这种分离旨在解决 MEV（最大可提取价值）带来的中心化风险，同时保持验证者的去中心化。

PBS 最初通过 Flashbots 的 MEV-Boost 以链外方式实现，未来计划通过"Enshrined PBS"（协议内置 PBS）集成到以太坊协议层，成为共识规则的一部分。

## 核心机制

### 角色分离

**区块提议者（Proposer）：**
- 由共识层随机选择的验证者担任
- 负责在指定时隙（slot）提议区块
- 从多个区块构建者中选择出价最高的区块
- 无需自己优化 MEV 提取
- 无需运行复杂的 MEV 搜索基础设施

**区块构建者（Builder）：**
- 专业的区块构建实体
- 负责创建和优化区块内容
- 通过排序交易、提取 MEV 最大化收益
- 向提议者竞价购买区块空间
- 处理复杂的交易排序和 MEV 策略

### 拍卖流程

**区块构建拍卖（Block Building Auction）：**
1. **构建阶段**：构建者创建包含交易的区块，优化 MEV 提取
2. **出价阶段**：构建者向中继（Relay）提交区块和出价（bid）
3. **盲选阶段**：提议者看不到区块内容，只能看到出价金额
4. **选择阶段**：提议者选择出价最高的区块
5. **支付阶段**：提议者收到构建者的出价作为收入
6. **发布阶段**：被选中的区块广播到网络

**盲选机制（Blind Block Building）：**
- 提议者在选择时看不到区块内容
- 防止提议者窃取 MEV 机会
- 确保构建者愿意分享高价值区块
- 通过承诺方案实现信任最小化

## 与 MEV 的关系

### MEV 问题

**最大可提取价值（MEV）**指验证者通过有利地排序交易来最大化利润：
- **套利**：[DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 价格差套利
- **清算**：抢先清算 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 头寸
- **三明治攻击**：在用户交易前后插入交易
- **抢跑**：复制有利可图的交易策略

**中心化风险：**
- 复杂的 MEV 提取需要专业知识和基础设施
- 散户验证者难以竞争
- 可能导致验证者集中化
- 威胁网络的去中心化和安全

### PBS 的解决方案

**重新配置 MEV 经济：**
- 提议者无需自己搜索 MEV
- 只需从众多构建者中选择最佳出价
- 将 MEV 提取专业化，但保持提议去中心化
- 散户验证者也能获得 MEV 收益

**民主化 MEV 收益：**
- 所有验证者（无论大小）都能公平参与
- 通过拍卖机制竞争确保最优定价
- 降低运行验证者的技术门槛
- 保持验证者生态的多样性

## 当前实现：MEV-Boost

### Flashbots MEV-Boost

PBS 最初通过 Flashbots 开发的 **MEV-Boost** 软件实现：
- **Sidecar 架构**：作为信标节点的独立辅助软件运行
- **可选参与**：验证者自愿选择是否使用
- **开源软件**：任何人都可以审计和运行
- **高采用率**：自合并以来，约 60% 的网络使用 MEV-Boost

**组件架构：**
```
验证者 <-> MEV-Boost <-> 中继 <-> 构建者
```

**中继（Relay）的角色：**
- 聚合多个构建者的区块
- 验证区块有效性
- 保护构建者和提议者的利益
- 选择出价最高的区块传递给提议者

### 采用现状

**网络参与：**
- 约 60% 的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)区块通过 MEV-Boost 生产
- 主要质押池和服务都支持 MEV-Boost
- 为验证者带来显著额外收益
- 推动了专业区块构建市场的发展

**市场集中度：**
- 顶级构建者占据 95% 以上的中标拍卖
- 构建者保留超过 27% 的利润率
- 存在正反馈循环：私有订单流吸引更多胜利
- 引发对市场集中化的担忧

## Enshrined PBS（协议内置PBS）

### 未来方向

[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)计划将 PBS 直接集成到协议层：
- **协议规则**：PBS 成为共识规则的一部分
- **强制执行**：所有验证者必须遵循 PBS 流程
- **信任最小化**：减少对第三方中继的依赖
- **更强保证**：协议级别的抗审查和公平性

### 研究方向

**[Vitalik](https://learnblockchain.cn/tags/Vitalik?map=EVM) Buterin 的提案：**
- 增强交易抗审查性
- 防止构建者过度集中
- 确保包含列表（Inclusion Lists）
- 平衡提议者和构建者的权力

**技术挑战：**
- 设计高效的协议内拍卖机制
- 防止时间攻击（timing games）
- 保护隐私的同时确保透明
- 与现有 MEV-Boost 生态兼容

## 优势与挑战

### 优势

**去中心化保护：**
- 防止散户验证者被淘汰
- 降低运行验证者的技术门槛
- 保持验证者生态多样性
- 增强网络安全性

**经济效率：**
- 提议者获得显著拍卖收入
- 优化交易排序和区块价值
- 提高验证者收益率
- 激励更多质押参与

### 挑战

**中心化风险：**
- 构建者市场高度集中
- 少数构建者控制大部分区块
- 私有订单流优势形成壁垒
- 需要机制防止过度中心化

**审查问题：**
- 构建者可能审查特定交易
- OFAC 合规要求影响中继行为
- 需要协议级抗审查保证
- 包含列表等机制正在研究中

**复杂性增加：**
- 增加了协议的复杂度
- 需要额外的基础设施（中继）
- 可能引入新的攻击向量
- 需要持续研究和改进

## 推荐阅读

- [Proposer-builder separation - Ethereum.org](https://ethereum.org/roadmap/pbs/)
- [What is Proposer / Builder Separation (PBS)? - Alchemy](https://www.alchemy.com/overviews/proposer-builder-separation)
- [State of research: censorship resistance under PBS - Vitalik Buterin](https://notes.ethereum.org/@vbuterin/pbs_censorship_resistance)
- [What is Proposer-Builder Separation? - Blocknative](https://www.blocknative.com/blog/proposer-builder-separation-ethereum)
- [SoK: Ethereum's Enshrined PBS - ArXiv](https://arxiv.org/abs/2506.18189)

## 相关概念

- **MEV**
- **MEV-Boost**
- **Flashbots**
- **区块构建**
- **验证者**
- **中继（Relay）**
- **抗审查**
- **去中心化**
