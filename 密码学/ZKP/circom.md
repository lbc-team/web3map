# Circom

## 概念简介

Circom 是一种用于定义算术电路的领域特定语言（DSL），专门用于生成零知识证明。它由 iden3 团队开发，是构建 zkSNARK 应用的核心工具。

Circom 允许程序员设计具有自定义约束的电路，编译器会输出 R1CS（Rank-1 Constraint System，秩-1 约束系统）表示，这是生成零知识证明所需的关键格式。

## 核心特性

**模块化设计**：Circom 的主要特点是其模块化，允许程序员定义可参数化的电路模板（templates），这些模板可以被实例化以形成更大的电路。

**编译输出**：Circom 编译器使用 [Rust](https://learnblockchain.cn/tags/Rust) 编写，可以生成：
- R1CS 文件及相关约束集
- 用 C++ 或 WebAssembly 编写的程序，用于高效计算电路所有线路的有效赋值

**灵活编译目标**：支持编译到多种格式，包括 R1CS、C++、WASM（WebAssembly）和 WAT。

## 技术原理

**约束系统**：使用 Circom 编写的电路定义了一组约束条件，这些约束必须被满足才能生成有效的零知识证明。

**核心概念：**

1. **Witness（见证）**：需要保密的信息。如果电路的某些输入需要保密，它们就是 witness 集的一部分。零知识证明可以证明你知道一组满足所有约束的信号（witness），而不泄露除公共输入和输出之外的任何信号。

2. **R1CS（Rank-1 Constraint System）**：电路被编译成 R1CS 格式，用于表示电路中的所有线路，使它们可以被检查以生成证明。R1CS 协议使代数电路能够表示为一组向量和矩阵。

3. **QAP（Quadratic Arithmetic [Program](https://learnblockchain.cn/tags/Program?map=Solana)）**：R1CS 进一步转换为多项式集合，用于 QAP 协议，然后输入到 zkSNARK 流水线的其余部分。

## 生态系统工具

**SnarkJS**：一个 JavaScript 库，用于从 R1CS 生成和验证 ZK 证明。用纯 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 和 Pure WebAssembly 编写。

**Circomlib**：一个公开可用的库，包含数百个电路模板，包括：
- 比较器（Comparators）
- 哈希函数（Hash Functions）
- 数字签名（Digital Signatures）
- 二进制和十进制转换器
- 更多实用电路

**安全分析工具：**
- **Circomspect**：静态分析器和 linter，用于检测 Circom 电路中的常见漏洞，扩展了 [circom](https://learnblockchain.cn/tags/circom) `--inspect` 标志执行的检查
- **CIVER**：安全验证工具
- **Ecne**：静态分析器
- **PICUS**：安全性验证静态分析器
- **ZKAP**：漏洞检测工具

**开发工具：**
- **Hardhat-zkit**：用于 [circom](https://learnblockchain.cn/tags/circom) 开发的 TypeScript 环境
- **Circomkit**：测试和开发环境

## 工作流程

**完整的开发流程：**

1. **编写电路**：使用 Circom 语言定义约束和电路逻辑
2. **编译电路**：使用 Circom 编译器将电路编译为 R1CS 和 witness 生成程序
3. **生成 Witness**：运行 witness 生成程序，输入私有和公共输入
4. **生成证明**：使用 SnarkJS 和 witness 生成 [zkSNARK](https://learnblockchain.cn/tags/zkSNARK) 证明
5. **验证证明**：使用验证密钥验证证明的有效性
6. **链上验证**（可选）：部署 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 验证合约到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)进行链上验证

## 版本更新

**Circom 2.0**（2022）：重大更新，提供了更好的性能和新功能。

**Circom 2.2.0**（2024年10月）：引入新特性，包括 Buses（总线）功能。

**Circom 2.2.2**（2025年3月）：最新版本，添加了新的素数 bls12377 和 r1cs 读取器。

## 知名应用案例

Circom 已被多个知名项目采用，证明了其有效性和可靠性：

1. **Polygon Hermez**：使用 Circom 构建 [zkEVM](https://learnblockchain.cn/tags/zkEVM?map=EVM) 电路
2. **Tornado Cash**：隐私交易协议使用 Circom 实现混币功能
3. **Dark Forest**：链上游戏使用零知识证明隐藏玩家位置
4. **Zkopru**：[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)上的隐私 [Rollup](https://learnblockchain.cn/tags/Rollup) 解决方案
5. **Polygon ID**：使用 iden3 协议和 Circom 2.0 实现的主权身份系统

## Polygon ID 集成

Polygon ID 实现了 zk-SNARKs，利用了 iden3 主权身份协议的创新和 Circom 2.0 算术电路框架。该协议使用 iden3 协议和 Circom ZK 工具包，为 Web3 创建可信交互提供私有身份解决方案。

## 安全性考虑

**2024年5月安全审计**：Trail of Bits 对 iden3 电路进行了安全审计并发布了报告。

**常见漏洞**：Circomspect 可以检测多种潜在问题，包括：
- 使用 Circomlib 的 Num2Bits 和 Bits2Num 转换域元素时的安全问题
- 只有当输入大小小于素数大小时才安全
- 约束不足导致的欠约束问题
- 整数溢出风险

## 学习资源

**中文教程：**
- [零知识证明编程 - 使用 Circom、Groth16 构建证明及验证 - 登链社区](https://learnblockchain.cn/article/9178)
- [零知识证明 circom 及 snarkjs 入门教程 - 腾讯云](https://cloud.tencent.com/developer/article/1638822)
- [构建你的第一个零知识 snark 电路（Circom2）- 登链社区](https://learnblockchain.cn/article/4256)
- [使用 SnarkJS 和 Circom 进行零知识证明 - 登链社区](https://learnblockchain.cn/article/7403)

**英文教程：**
- [Circom 2 Documentation](https://docs.circom.io/)
- [zkSNARK Crashcourse with Circom and SnarkJS](https://zksnark.toddchapman.io/)
- [Circom language tutorial with circomlib walkthrough - RareSkills](https://rareskills.io/post/circom-tutorial)
- [R1CS Explainer - 0xPARC](https://learn.0xparc.org/materials/circom/additional-learning-resources/r1cs%20explainer/)

**官方资源：**
- [GitHub - iden3/circom](https://github.com/iden3/circom)
- [GitHub - iden3/circuits](https://github.com/iden3/circuits)
- [iden3 Official Website](https://iden3.io/)
- [Iden3 Blog - Circom 2.0 Release](https://blog.iden3.io/circom-2-is-released.html)

## 优势与挑战

**优势：**
- 模块化设计，代码可重用
- 丰富的库和模板（Circomlib）
- 强大的工具链生态
- 被多个生产项目验证
- 活跃的社区和持续更新
- 完善的安全分析工具

**挑战：**
- 学习曲线较陡峭
- 需要理解约束系统和[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)原理
- 电路优化需要经验
- 安全性要求高，需要仔细审计

## 未来发展

Circom 持续演进，2024-2025 年的更新显示该项目仍在积极开发中。随着[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)应用的增长，Circom 作为开发者首选工具的地位将继续巩固。

## 推荐阅读

**学术论文：**
- [Circom: A Circuit Description Language for Building Zero-Knowledge Applications - ResearchGate](https://www.researchgate.net/publication/366676429_Circom_A_Circuit_Description_Language_for_Building_Zero-knowledge_Applications)
- [Practical Security Analysis of Zero-Knowledge Proof Circuits - IACR](https://eprint.iacr.org/2023/190.pdf)

**视频教程：**
- [Introduction to Circom 2.0 - Devcon Archive](https://archive.devcon.org/archive/watch/6/introduction-to-circom20/?tab=YouTube)

## 相关概念

- **[zkSNARK](https://learnblockchain.cn/tags/zkSNARK)**
- **SnarkJS**
- **R1CS**
- **QAP**
- **Witness**
- **[Groth16](https://learnblockchain.cn/tags/Groth16)**
- **iden3**
- **Polygon Hermez**
