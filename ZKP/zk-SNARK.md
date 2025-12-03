# zk-SNARK

## 概念简介

zk-SNARK（Zero-Knowledge Succinct Non-Interactive Argument of Knowledge，零知识简洁非交互式知识论证）是一种零知识证明技术，允许证明者向验证者证明某个陈述为真，而无需透露任何额外信息。该技术由 Nir Bitansky、Alessandro Chiesa 等密码学家于 2010 年代初期提出并逐步完善，是现代密码学和区块链隐私保护领域的重要突破。

zk-SNARK 的核心特性体现在其名称中：零知识（Zero-Knowledge）意味着除了陈述本身的真实性外不泄露其他信息；简洁（Succinct）指证明数据量小且验证速度快；非交互式（Non-Interactive）表示证明者和验证者无需多轮交互；知识论证（Argument of Knowledge）说明证明者确实拥有相关知识。这些特性使 zk-SNARK 成为区块链扩容、隐私保护和可验证计算的关键技术。

## 核心特性

**简洁性**

zk-SNARK 生成的证明数据量极小，通常只有几百字节，验证时间在毫秒级别。无论被证明的计算有多复杂，证明大小几乎保持恒定。这种简洁性使得资源受限的节点也能快速验证复杂计算的正确性，为区块链扩容提供了可能。

**非交互性**

与传统需要多轮交互的零知识证明协议不同，zk-SNARK 采用非交互式设计。证明者生成一次证明后，验证者可以独立验证，无需与证明者通信。这种特性通过 Fiat-Shamir 启发式转换实现，将交互式协议转换为非交互式，大幅简化了协议流程和应用场景。

**可信设置**

大多数 zk-SNARK 方案（如 Groth16）需要进行可信设置（Trusted Setup）阶段，生成公共参考字符串（CRS）。这个过程产生的"有毒废料"（toxic waste）必须被销毁，否则知道该信息的人可以伪造证明。为确保安全性，通常采用多方计算（MPC）仪式，只要有一个参与者诚实删除了秘密，系统就是安全的。

**通用可组合性**

较新的 zk-SNARK 方案（如 PLONK、Marlin）实现了通用可信设置，一次设置可用于多个不同电路。这种特性降低了部署新应用的成本，提高了系统的灵活性。目前研究方向还包括完全消除可信设置的 zk-SNARK 变体。

## 技术优势

**极高的验证效率**：验证者只需处理几百字节的证明数据和执行少量椭圆曲线运算，即使在移动设备上也能快速完成验证。这使得轻客户端和资源受限环境能够参与区块链验证。

**隐私保护能力**：zk-SNARK 能够在不泄露交易细节（金额、地址等）的情况下证明交易合法性，为金融隐私提供了强有力的保障。

**计算压缩**：可以将复杂计算压缩为简短证明，实现链下计算、链上验证的扩容方案。以太坊 Layer2 方案 zkRollup 利用这一特性实现了数千倍的吞吐量提升。

**可组合性**：zk-SNARK 证明可以递归组合，一个证明可以验证另一个证明的正确性，支持构建复杂的证明系统。

## 技术原理

zk-SNARK 的技术原理涉及算术电路、多项式承诺和配对密码学。计算过程首先被转换为 R1CS（Rank-1 Constraint System）约束系统，再编码为多项式方程。证明者和验证者之间的交互通过椭圆曲线配对实现，保证了零知识特性和简洁性。

典型的 zk-SNARK 协议包含三个阶段：Setup（生成公共参数）、Prove（证明者生成证明）、Verify（验证者验证证明）。Setup 阶段产生 proving key 和 verification key；Prove 阶段证明者使用 witness（私密输入）和 proving key 生成证明；Verify 阶段验证者使用 verification key 快速验证证明有效性。

## 应用场景

**隐私加密货币**

Zcash 是首个大规模应用 zk-SNARK 的加密货币项目，通过屏蔽交易（Shielded Transaction）实现完全的交易隐私。用户可以隐藏发送方、接收方和交易金额，同时证明交易的合法性（如未双花、余额充足等）。

**Layer2 扩容方案**

zkRollup 利用 zk-SNARK 实现以太坊扩容。Layer2 在链下批量处理数千笔交易，生成一个简洁的有效性证明提交到主链。主链只需验证证明即可确认所有交易有效，大幅降低了链上负担。StarkWare、zkSync、Scroll 等项目采用此技术。

**可验证计算**

zk-SNARK 可用于外包计算场景。客户端将计算任务外包给服务器，服务器返回计算结果和 zk-SNARK 证明。客户端验证证明即可确信结果正确，无需重新执行计算。这在云计算、AI 推理等领域有重要应用。

**身份认证**

用户可以证明自己满足某些条件（如年满 18 岁、拥有特定资格）而不泄露具体信息。这种选择性披露在 KYC、投票、访问控制等场景中保护了用户隐私。

## 发展历程

2010 年代初期，Gennaro、Gentry、Parno 等人提出了早期的 zk-SNARK 构造（如 GGPR）。2013 年，Parno 等人发布 Pinocchio 协议，实现了首个实用的 zk-SNARK 系统。

2014 年，Zcash 团队开始将 zk-SNARK 应用于加密货币，为隐私交易奠定基础。2016 年，Jens Groth 提出 Groth16 协议，成为最高效的 zk-SNARK 方案之一，被 Zcash 和众多项目采用。

2019-2020 年，PLONK、Marlin 等通用可信设置的 zk-SNARK 方案问世，降低了部署难度。同期，zkRollup 技术开始在以太坊生态中应用，推动了 Layer2 扩容的发展。

2021 年后，zk-SNARK 在 Layer2、跨链桥、隐私协议等领域得到广泛应用。递归证明、硬件加速、新型证明系统等技术持续演进，推动零知识证明技术走向成熟。

## 相关链接

- [Zcash 的 zk-SNARK 技术](https://z.cash/technology/zksnarks/)
- [zk-SNARK 学习资源](https://zkp.science/)
- [Groth16 论文](https://eprint.iacr.org/2016/260.pdf)
- [PLONK 论文](https://eprint.iacr.org/2019/953)
- [libsnark 代码库](https://github.com/scipr-lab/libsnark)

## 相关协议

- **zk-STARK**：不需要可信设置的零知识证明方案
- **Bulletproofs**：另一种简洁零知识证明协议
- **PLONK**：通用可信设置的 zk-SNARK 变体
- **Groth16**：最常用的 zk-SNARK 实现方案
- **Zcash**：采用 zk-SNARK 的隐私加密货币
- **zkRollup**：基于 zk-SNARK 的以太坊 Layer2 扩容方案
