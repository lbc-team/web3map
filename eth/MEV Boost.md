# MEV-Boost

## 概念简介

MEV-Boost 是由 Flashbots 开发的开源软件，实现了以太坊的提议者-构建者分离（PBS）架构。它作为信标节点的"sidecar"（辅助软件）运行，允许验证者通过竞争性市场从专业的区块构建者那里获取高 MEV（最大可提取价值）区块，从而最大化质押收益，同时保持以太坊的去中心化。

自以太坊合并转向权益证明以来，约 60% 的网络验证者使用 MEV-Boost，它已成为[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)生态系统中不可或缺的基础设施。

## 核心架构

### 三层结构

**验证者（Proposers）：**
- 运行信标节点和执行客户端
- 安装 MEV-Boost 软件作为中间件
- 在指定时隙提议区块
- 从多个中继中选择最高出价

**中继（Relays）：**
- 聚合来自多个构建者的区块
- 验证区块的有效性
- 保护构建者和提议者的利益
- 选择出价最高的区块传递给提议者
- 处理支付和数据传输

**构建者（Builders）：**
- 专业的区块构建实体
- 优化交易排序，提取 MEV
- 向中继提交区块和出价
- 竞争赢得区块空间

### 工作流程

1. **构建阶段**：
   - 构建者监控 mempool 和私有订单流
   - 构建优化的区块，包括 MEV 提取策略
   - 计算愿意支付给提议者的出价

2. **提交阶段**：
   - 构建者将区块和出价提交给一个或多个中继
   - 中继验证区块有效性（不执行）
   - 中继存储区块和出价信息

3. **竞标阶段**：
   - 提议者的 MEV-Boost 查询连接的所有中继
   - 每个中继返回其最高出价的区块头
   - 提议者看不到区块内容（盲选）

4. **选择阶段**：
   - 提议者选择出价最高的区块
   - 向对应中继发送签名的区块头

5. **揭示阶段**：
   - 中继验证签名后，向提议者提供完整区块体
   - 提议者广播完整区块到网络
   - 构建者的支付包含在区块中

## MEV 与 PBS

### MEV 的问题

**最大可提取价值（MEV）：**
- 套利：[DEX](https://learnblockchain.cn/tags/DEX?map=EVM) 价格差套利
- 清算：[DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议清算奖励
- 三明治攻击：在用户交易前后插入交易
- 抢跑：复制有利可图的交易

**中心化风险：**
- 复杂的 MEV 提取需要专业技术和资源
- 散户验证者难以竞争
- 可能导致验证者集中化
- 威胁网络的去中心化和安全

### MEV-Boost 的解决方案

**民主化 MEV 收益：**
- 所有验证者都能访问专业构建的区块
- 无需自己运行复杂的 MEV 搜索基础设施
- 散户和大型质押池处于公平竞争环境
- 显著增加验证者收益（15-30% 额外收益）

**保持去中心化：**
- 降低运行验证者的技术门槛
- 防止技术优势导致的中心化
- 鼓励更多人参与质押
- 增强网络安全性

## 盲区块构建

### 为什么需要"盲选"

**保护构建者：**
- 如果提议者能看到区块内容
- 可能窃取 MEV 策略并自己构建相似区块
- 构建者失去竞争优势
- 不愿意分享高价值区块

**解决方案：**
- 提议者只能看到区块头和出价金额
- 区块内容在提议者承诺后才揭示
- 使用密码学承诺保证区块不可篡改
- 确保构建者愿意分享最优区块

### 信任模型

**中继的角色：**
- 作为可信中介
- 验证构建者提交的区块有效
- 确保提议者收到承诺的支付
- 防止恶意行为

**风险：**
- 中继可能审查某些交易或构建者
- 中继之间可能存在串通
- 需要多个独立中继增加去中心化

**缓解措施：**
- 运行多个独立的中继
- 中继代码开源，可审计
- 社区监督和信誉机制
- 未来转向 Enshrined PBS 减少对中继的依赖

## 当前生态

### 主要中继

**公共中继：**
- **Flashbots Relay**：最大的中继，由 Flashbots 运营
- **BloXroute**：提供低延迟、高性能的中继服务
- **Blocknative**：专注于实时 mempool 数据的中继
- **Eden Network**：支持优先交易的中继
- **Aestus**：独立运营的中继

**中继多样性：**
- 验证者可以同时连接多个中继
- 提高出价竞争和收益
- 增加网络韧性
- 降低单点故障风险

### 构建者市场

**市场集中度：**
- 顶级构建者占据 95%+ 的中标拍卖
- 构建者保留 27%+ 的利润率
- 存在正反馈循环：更多私有订单流 → 更高胜率 → 更多订单流

**主要构建者：**
- Beaver Build
- Titan Builder
- Flashbots Builder
- BuildAI
- 其他专业构建者

**私有订单流（Private Order Flow）：**
- 用户/应用直接向构建者发送交易
- 避免公共 mempool 的抢跑风险
- 构建者竞争提供最优执行
- 占中标区块的重要部分

## 收益提升

### 额外收入

**验证者收益组成（使用 MEV-Boost）：**
- **共识层奖励**：区块提议和证明奖励
- **执行层奖励**：优先费（tips）
- **MEV-Boost 支付**：构建者的出价
- **总提升**：通常增加 15-30% 的收益

**实际案例：**
- 不使用 MEV-Boost：仅获得基础奖励和优先费
- 使用 MEV-Boost：额外获得数百美元到数千美元（取决于区块）
- 高 MEV 区块可能支付数万美元

### 收益优化

**连接多个中继：**
- 增加竞争，提高出价
- 不同中继可能有不同构建者
- 某些中继在特定时段表现更好

**配置选项：**
- 设置最低出价阈值
- 选择中继偏好
- 启用本地区块构建作为后备

## 安全与审查问题

### OFAC 合规

**监管压力：**
- 某些中继遵守 OFAC（美国财政部外国资产控制办公室）制裁
- 审查与受制裁地址相关的交易
- 引发社区对审查抗性的担忧

**社区响应：**
- 出现非审查中继（如 Aestus）
- 验证者可以选择连接非审查中继
- 争论网络层审查 vs 应用层合规

### 中心化风险

**构建者集中度：**
- 少数顶级构建者控制大部分区块
- 私有订单流形成进入壁垒
- 可能影响交易包含和定价

**缓解措施：**
- 鼓励更多构建者参与
- 开发开源构建者软件
- 研究去中心化构建者协议

## 未来发展：Enshrined PBS

### 协议内置

**目标：**
- 将 PBS 直接集成到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)协议
- 成为共识规则的一部分
- 减少对第三方中继的依赖

**优势：**
- 信任最小化
- 更强的抗审查保证
- 协议级别的公平性
- 消除中继作为单点故障

**挑战：**
- 设计复杂性
- 向后兼容性
- 平衡效率和去中心化
- 需要充分的研究和测试

### 包含列表（Inclusion Lists）

**[Vitalik](https://learnblockchain.cn/tags/Vitalik?map=EVM) 提案：**
- 提议者可以强制包含某些交易
- 防止构建者完全审查交易
- 保证交易的最终包含性
- 平衡构建者权力

## 安装和配置

### 基本设置

**安装 MEV-Boost：**
```bash
# 下载 MEV-Boost 二进制文件
wget https://github.com/flashbots/mev-boost/releases/download/vX.X.X/mev-boost_X.X.X_linux_amd64.tar.gz
tar -xzf mev-boost_X.X.X_linux_amd64.tar.gz

# 运行 MEV-Boost
./mev-boost -relay-check \
  -relay https://relay1.example.com \
  -relay https://relay2.example.com
```

**配置信标节点：**
- 添加 MEV-Boost 端点到信标节点配置
- 通常是 `http://localhost:18550`
- 信标节点通过该端点查询 MEV-Boost

### 中继选择

**考虑因素：**
- 中继的审查政策
- 历史出价表现
- 延迟和可靠性
- 信誉和透明度

**示例中继列表：**
- Flashbots: `https://boost-relay.flashbots.net`
- BloXroute Max Profit: `https://bloxroute.max-profit.blxrbdn.com`
- BloXroute Regulated: `https://bloxroute.regulated.blxrbdn.com`
- Aestus: `https://mainnet.aestus.live`

## 监控和工具

**仪表板：**
- [MEV-Boost Dashboard](https://mevboost.pics/)：实时监控中继和构建者
- [MEV-Boost Relay Monitor](https://www.mevboost.org/)：中继性能对比
- [Relayscan](https://www.relayscan.io/)：中继数据分析

**指标：**
- 中继出价分布
- 构建者市场份额
- 审查率统计
- 验证者收益提升

## 推荐阅读

- [MEV-Boost - Flashbots](https://boost.flashbots.net/)
- [mev-boost - GitHub](https://github.com/flashbots/mev-boost)
- [mev-boost-relay - GitHub](https://github.com/flashbots/mev-boost-relay)
- [Flashbots Documentation](https://docs.flashbots.net/)
- [Flashbots MEV-boost explained - Medium](https://medium.com/roverx/flashbots-mev-boost-explained-in-5-mins-68e191140224)

## 相关概念

- **PBS**
- **MEV**
- **Flashbots**
- **中继（Relay）**
- **构建者（Builder）**
- **提议者（Proposer）**
- **盲区块构建**
- **OFAC**
