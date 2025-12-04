# Rocket Pool

## 概念简介

Rocket Pool 是以太坊上领先的去中心化流动性质押（Liquid Staking）协议。它旨在解决个人独立运行验证节点（Solo Staking）的高门槛问题，同时为不想锁定 ETH 的用户提供质押收益。

与 Lido 等其他流动性质押方案相比，Rocket Pool 最显著的特点是其无需许可（Permissionless）的节点运营机制。任何只要满足最低 ETH 和 RPL（协议代币）抵押要求的用户，都可以成为节点运营商（Node Operator），为协议运行验证节点。

Rocket Pool 于 2021 年底上线主网，一直致力于维护以太坊的去中心化和抗审查属性。

## 核心机制与原理

Rocket Pool 的架构设计精巧地结合了普通质押者和节点运营商的利益。

### 1. rETH 代币
rETH 是 Rocket Pool 的流动性质押代币（LST）。
- **价值累积**：与 Lido 的 stETH（rebase 机制，数量增加）不同，rETH 采用增值模型。rETH 的数量不变，但其对 ETH 的兑换汇率会随着质押奖励的积累而不断上升。
- **税务优势**：在某些税收管辖区，增值模型可能比 rebase 模型更具税务优势（被视为资本利得而非利息收入）。
- **抵押保护**：rETH 的价值由整个协议中的 ETH 以及节点运营商抵押的 RPL 提供了额外的保险缓冲。

### 2. 迷你池 (Minipools)
为了降低运行节点的门槛，Rocket Pool 引入了“迷你池”概念。
- **以太坊要求**：传统 Solo Staking 需要 32 ETH。在 Rocket Pool 中，节点运营商只需提供 8 ETH 或 16 ETH（取决于配置，LEB8 或 LEB16）。
- **资金匹配**：协议从存款池（rETH 用户存入的 ETH）中提取剩余的 24 ETH 或 16 ETH，与节点运营商的资金合并，凑齐 32 ETH 启动一个验证节点。
- **佣金**：节点运营商除了获得自己那部分 ETH 的质押奖励外，还能从匹配的 ETH 收益中抽取一定比例（约 15%）作为佣金，从而获得比 Solo Staking 更高的收益率。

### 3. RPL 代币与保险机制
RPL 是 Rocket Pool 的治理和工具代币。
- **保险债券**：节点运营商在创建迷你池时，必须抵押一定价值的 RPL（至少占其借入 ETH 价值的 10%）。这部分 RPL 充当“保险”，如果节点因离线或作恶被罚没（Slash），首先扣除其抵押的 ETH，如果不足则扣除 RPL，从而保护 rETH 持有者的利益。
- **RPL 奖励**：为了激励运营商抵押 RPL，协议会向抵押率达标的运营商发放 RPL 通胀奖励。

## 主要特点

- **去中心化**：节点运营商无需白名单，任何人均可加入，这与依赖精选节点集的协议形成鲜明对比。
- **低门槛**：将运行节点的资金门槛从 32 ETH 降低至 8 ETH。
- **资本效率**：对于节点运营商，利用杠杆效应（使用协议资金）提高了 ETH 本位的收益率。
- **安全性**：通过超额抵押的 RPL 提供额外的安全层。

## 相关概念

- **LSD / LST**：流动性质押衍生品/代币。
- **Solo Staking**：独立运行验证节点，无需中间协议。
- **DVT (分布式验证技术)**：Rocket Pool 正在探索集成的技术，以进一步降低单点故障风险。

## 推荐阅读

- [Rocket Pool 官方文档](https://docs.rocketpool.net/)
- [Rocket Pool Whitepaper](https://rocketpool.net/files/rocket-pool-whitepaper.pdf)
