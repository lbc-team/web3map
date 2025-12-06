# 零知识证明

零知识证明（Zero-knowledge Proof， 简称 ZKP 或 ZK ）是密码学中的一个重要概念，它允许一方（证明者）向另一方（验证者）证明他们知道某个特定的信息，而不需要透露任何关于这个信息的具体内容。

在零知识证明(Zero-Knowledge Proof)中， 证明(Proof)指的是证明者(Prover，简写为 P )向验证者(Verifier，简写为 V)证明某个陈述或命题是正确的过程。

## ZKP 三个特性

1. 完全性(Completeness): 如果陈述是真的，验证者可以通过证明者提供的证明来验证这个陈述。
2. 可靠性(Soundness): 如果陈述是假的，证明者无法骗过验证者。
3. 零知识(Zero-Knowledge): 证明过程不会泄露证明者私有的信息。



## ZKP 应用

零知识证明最早在 1985 年就已经被提出，然而直到 2010 年后，零知识证明在区块链技术中得到广泛应用，它非常适合用于解决区块链中的隐私和扩展性问题，例如用于：

1. **计算证明**：在区块链中，每个节点的计算能力有限，但借助 ZKP 技术，节点可以将大量的计算外包给链下节点，链上只需要验证链下提交的计算结果和计算证明就可以知道计算是否正确。zkRollup 方案就是很好的例子。
2. **隐私证明**：ZKP 的零知识特性，可以成为保护隐私的工具，例如 Zcash 利用 ZKP 来实现对交易信息的保密。
3. **数据压缩**：Filecoin 运用 ZKP 构造了时空证明系统，能证明用户在本地存储了特定文件，Mina 借助递归零知识证明，将区块链账本压缩到 11 KB。



## 证明系统

证明系统是 ZKP 的底层算法实现，分为交互式和非交互式两种：

### **1. 交互式证明系统（IZK 或 IPS）**

交互证明由若干轮组成，在每一轮，P 和 V 可能需根据从对方收到的消息和自己计算的某个结果向对方发送消息。比较典型的方式是在每轮 V 都向 P 发出一个询问，P 向 V 做出一个应答。所有轮执行完后， V 根据 P 是否在每一轮对自己发出的询问都能正确应答，决定是否接受 P 的证明。

### 2. 非交互式证明系统（NIZK）

非交互式证明系统中，证明由 P 产生后直接给 V，V 对证明直接进行验证。 区块链中使用较多的是非交互式证明系统。常见的 NIZK 又分为以下类别[参考](https://github.com/matter-labs/awesome-zero-knowledge-proofs)：

**SNARKs**(Succinct Non-interactive ARguments of Knowledge)：

特点：简洁证明大小，证明验证耗时相比较短，但需要对每一个电路进行可信设置。

代表项目：Groth16。

**STARKs** (Succinct (Scalable) Transparent ARguments of Knowledge)：

特点：证明尺寸较大，不需要进行可信设置，具有良好的可扩展性， 后量子安全。

代表项目：STARK。

**Bulletproofs**：

特点：简洁证明大小，无需可信设置，但证明生成和验证耗时相比较长。

代表项目：Bulletproofs, Halo, Halo2。

**SNORKs** (Succinct Non-interactive Oecumenical (Universal) aRguments of Knowledge)

特点：简洁证明大小，只需要进行一次可信设置即可用于所有电路。

代表项目：Sonic, Plonk, Marlin, Plonky2。



## 构造零知识证明 （ZKP 编程）

要实现一个零知识证明通常要进行以下几步：

1. **问题转化**：证明者需要把待证明的问题转化为一个标准化的形式，如布尔电路或算术电路或R1CS，即电路可满足性问题（Circuit-SAT）。

   > 电路(Circuit) 是零知识证明的逻辑实现代码，是多项式的形象化表达，而不是硬件电路。

2. **生产证明**：证明者使用这个电路生成一个证明。通常包括把电路变成多项式，转换成多项式可满足性问题（Polynomial-SAT）。

3. **承诺**: 证明者将生成的证明（多项式）进行承诺。这是一个加密步骤，旨在确保证明的完整性和防止篡改。

4. **发送承诺**: 证明者将这个承诺的证明发送给验证者。



证明系统面临的主要挑战之一是将抽象的高级概念转化为实际电路，初学者可以从 zk DSL （特定领域语言） 开始， 例如Circom、Halo2 或 Cairo ，DSL 简化了 ZKP 电路的开发和验证。另外还有一些开发库实现了基础电路和不同程度的抽象，例如：[libsnark](https://github.com/scipr-lab/libsnark)、[gnark](https://github.com/consensys/gnark)、[snarkjs](https://github.com/iden3/snarkjs) 。



## ZK 技术栈

![img](https://img.learnblockchain.cn/pics/20240614154507.png)



## 参考引用：

1. 安比实验室：[零知识证明学习资料汇总](https://learnblockchain.cn/2019/11/08/zkp-info)

2. [Awesome zero knowledge proofs (zkp)](https://github.com/matter-labs/awesome-zero-knowledge-proofs)

