## 什么是Layer2（二层扩容）





Layer2 指在区块链技术和网络协议中用于扩展基础区块链（Layer 1）的解决方案的统称。其目的是提高交易速度、降低交易费用，并增强网络的可扩展性和效率。  



以太坊和比特币都是 Layer1 区块链，因为它们是各种 Layer2 网络构建的底层基础。典型的Layer2 项目的示例包括以太坊上的“[Rollup](https://learnblockchain.cn/tags/Rollup)”和比特币上的[闪电网络](https://learnblockchain.cn/tags/%E9%97%AA%E7%94%B5%E7%BD%91%E7%BB%9C)。这些Layer2项目上的所有用户交易活动最终都可以回归到 Layer1。 不过 Layer2 并没有一个严格的定义， 但通常要求在安全性上继承 Layer1 ，是[链下扩容方案](https://learnblockchain.cn/tags/%E6%89%A9%E5%AE%B9)中，安全性较高的一类。



以太坊在 Layer2 上探索相对成熟，发展出了多种不同类型Layer2，每种类型都有自己的权衡和安全模型。以 Rollup 为例，工作原理录下图所示：



![img](https://img.learnblockchain.cn/pics/20240617125056.png&w=1920&q=75!/scale/60)





Rollups 将数百个交易捆绑到 Layer1 的单个交易中。因此 L1 交易费用将分担 Rollup 中的每个交易中，从而使 Layer2 每个交易的费用更便宜。Rollup中的交易数据提交到Layer 1，但执行是由 Rollup 中单独完成的。 更多参考 [Rollup 百科](https://learnblockchain.cn/tags/Rollup) 。



