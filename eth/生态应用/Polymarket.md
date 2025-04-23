## Polymarket 是什么？

Polymarket 是一个基于 Polygon 的去中心化预测市场平台，用户可以对未来事件的结果进行押注交易。

### Polymarket 的核心机制

Polymarket 运作大概分为以下几步：

![Polymarket 运作原理](https://img.learnblockchain.cn/pics/20250423214905.png)


1. 事件创建（Market Creation）
一般形式如下：“2024年美国总统选举中，特朗普是否当选？”
[Yes] / [No]
每个事件的关键要素：
事件描述（自然语言 + 结构化判断标准）
到期时间（事件截止时间）
结算源（如 Associated Press、官方网站）
市场类型：二元市场（Yes/No）或多选市场

事件创建后，会部署一个新的智能合约市场

2. 押注交易
   
每个选项的价格起始是 1/n , 二元市场起始为 0.5U，押注交易基于 LMSR（Logarithmic Market Scoring Rule） 的自动做市曲线。 
价格也表示当前市场认为该结果发生的概率。
用户买入某个选项，等于“押注该选项会发生”，价格会随供需波动。（用户买的的价格是起始与买入后的均价）
举个例子：假设“特朗普当选”的 YES 价格是 0.62（即市场认为有 62% 概率发生），用户用 USDC 买入 YES，就相当于愿意用 0.62 的成本换取 1 USDC 的回报（如果结果为真）

3.  事件结算（Resolution）
事件结果可以被验证后，Polymarket 会触发结算流程。结算来源主要有：第三方预言机（Reality.eth）、官方 API（如 Associated Press）人工提交争议/仲裁（极少）
一旦结果被确定，赢家的 token 可兑换为 1 USDC，失败的一文不值。
与买入时的差价是盈利或亏损。