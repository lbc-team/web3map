# PeerDAS

## 概念简介

PeerDAS（Peer Data Availability Sampling，对等数据可用性采样）是以太坊通过 EIP-7594 在 Fusaka 升级（2025 年 12 月）中引入的关键技术，旨在通过优化数据可用性机制大幅扩展[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)的 blob 容量，同时不增加验证者的硬件要求。

PeerDAS 允许节点仅下载一小部分数据即可验证整体数据可用性，通过数据可用性采样（DAS）和纠删码技术，将每个节点的数据下载量降低到 1/8（未来可能降至 1/16 或 1/32），为最终实现 8 倍 blob 容量增长铺平道路，支持[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)向完整 Danksharding 迈进。

## 核心原理

### 数据可用性采样（DAS）

**问题背景：**
- EIP-4844 引入的 blob 要求所有节点下载全部 blob 数据
- 随着 blob 数量增加，存储和带宽需求线性增长
- 家庭质押者难以承受数据中心级别的硬件要求
- 限制了 blob 容量的进一步扩展

**DAS 解决方案：**
- 节点只需下载一小部分数据样本
- 通过随机采样验证整体数据可用性
- 利用纠删码保证数据冗余
- 节点数量越多，安全性越高

### 列采样机制

**列（Column）vs 行（Row）：**
- **行（Row）**：完整的 blob 数据
- **列（Column）**：跨所有 blob 的横截面

**为什么选择列：**
- PeerDAS 将样本定义为"列"而非"行"
- 列采样比行采样更高效
- 更好地分布数据负载
- 优化网络传输和存储

**采样参数：**
- 每个节点采样 **1/8** 的数据（当前参数）
- 未来可降至 1/16 或 1/32
- 通过减小样本大小增加列数
- 灵活调整以适应网络状况

## 技术实现

### 纠删码

**Reed-Solomon 纠删码：**
- 将数据编码为 N 个块
- 只需任意 k 个块即可重构完整数据
- N - k 个块可以丢失而不影响恢复
- 提供数据冗余和容错能力

**应用到 PeerDAS：**
- Blob 数据通过纠删码扩展
- 分布到多个列中
- 节点随机选择列进行采样
- 确保数据始终可恢复

### 伪随机采样

**随机性保证：**
- 使用伪随机数生成器选择采样列
- 防止攻击者预测采样模式
- 网络规模越大，攻击成功概率越低
- 呈次线性下降趋势

**安全性：**
- 解决数据扣留攻击（withholding attacks）
- 攻击者无法预先知道哪些节点会采样哪些数据
- 需要控制绝大多数节点才能成功隐藏数据
- 网络去中心化程度越高越安全

## 对节点的影响

### 降低硬件要求

**存储需求：**
- 完整 blob 存储：100% 数据
- PeerDAS (1/8)：仅 12.5% 数据
- 未来 (1/16)：仅 6.25% 数据
- **降幅**：约 87.5% 的存储节省

**带宽需求：**
- 下载量减少 87.5%
- 上传量也相应减少
- 降低网络传输压力
- 支持家庭宽带运行节点

**计算要求：**
- 验证计算量显著降低
- 仅需验证采样的列
- 降低 CPU 和内存压力
- 普通硬件即可胜任

### 支持家庭质押

**民主化验证：**
- 无需数据中心级别的硬件
- 普通笔记本电脑或 NUC 可运行
- 降低运行成本
- 提高网络去中心化程度

**激励更多参与：**
- 降低技术门槛
- 减少运营开支
- 吸引更多散户质押者
- 增强网络安全性

## 扩容潜力

### 当前 vs 未来

**EIP-4844（Dencun）：**
- 目标：3 blob/区块
- 最大：6 blob/区块
- 总容量：768 KB/区块

**EIP-7691（Pectra）：**
- 目标：6 blob/区块
- 最大：9 blob/区块
- 总容量：1.125 MB/区块

**PeerDAS（Fusaka）：**
- 优化数据分发机制
- 为更大规模扩容铺路
- 目标：支持 8 倍容量增长
- 最终：每区块数十甚至上百个 blob

### 通往完整 Danksharding

**渐进式扩容路线：**
1. **Proto-Danksharding**（Dencun）：引入 blob 概念
2. **增加 blob 容量**（Pectra）：3/6 → 6/9
3. **PeerDAS**（Fusaka）：优化数据分发，降低节点负担
4. **进一步增加 blob**：随着 PeerDAS 成熟，逐步增加 blob 数量
5. **完整 Danksharding**：目标 16 MB/秒数据吞吐量

**长期愿景：**
- 每个区块数百个 blob
- 16 MB/秒的数据吞吐量
- 完全分片的数据可用性层
- 支持海量 L2 交易

## 与 EIP-4844 的兼容性

**完全向后兼容：**
- PeerDAS 建立在 EIP-4844 基础上
- 不改变 blob 的基本结构
- 仅优化数据分发和采样机制
- 现有 L2 无需修改

**渐进式部署：**
- 可以逐步推出
- 节点可以选择性升级
- 不影响网络正常运行
- 降低升级风险

## 对 Layer 2 的影响

**更低成本：**
- 更多 blob 容量意味着更多数据可用性
- L2 可以发布更多交易数据
- 进一步降低 L2 交易费用
- 提高 L2 吞吐量

**支持更多 Rollup：**
- 更大的数据可用性空间
- 支持更多 [Rollup](https://learnblockchain.cn/tags/Rollup) 同时运行
- 降低 [Rollup](https://learnblockchain.cn/tags/Rollup) 之间的竞争
- 促进 L2 生态繁荣

**更快结算：**
- 更多 blob 空间减少拥堵
- L2 可以更频繁地提交数据
- 加快最终确定时间
- 改善用户体验

## 部署时间线

- **2024 年**：EIP-7594 提案和规范制定
- **2025 年上半年**：测试网部署和测试
- **2025 年 12 月 3 日**：Fusaka 升级主网激活 PeerDAS

## 技术挑战

**网络协议优化：**
- 需要高效的 P2P 数据分发机制
- Gossip 协议的优化
- 减少网络延迟和开销
- 确保数据快速传播

**安全性保证：**
- 防止数据扣留攻击
- 确保足够的数据冗余
- 应对恶意节点
- 维护网络健壮性

**客户端实现：**
- 所有客户端需要支持 PeerDAS
- 实现复杂的采样逻辑
- 优化存储和检索
- 确保互操作性

## 推荐阅读

- [EIP-7594: PeerDAS - Peer Data Availability Sampling](https://learnblockchain.cn/docs/eips/EIPS/eip-7594)
- [EIP-7594 on GitHub - Ethereum EIPs](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7594.md)
- [Unbundling PeerDAS - DeFi Planet](https://defi-planet.com/2025/08/unbundling-peerdas-ethereum-scaling-data-availability/)
- [Unpacking EIP-7594: PeerDAS Deep Dive - Medium](https://medium.com/@Krieger69/unpacking-eip-7594-a-technical-deep-dive-into-peerdas-and-ethereums-scalability-roadmap-28caf9dcaf16)
- [EIP-7594 (PeerDAS) - IQ.wiki](https://iq.wiki/wiki/eip-7594-peerdas)

## 相关概念

- **数据可用性采样**
- **EIP-7594**
- **Blob**
- **Danksharding**
- **纠删码**
- **Reed-Solomon**
- **Fusaka**
- **Layer 2**
