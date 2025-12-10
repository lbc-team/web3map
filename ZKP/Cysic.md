# Cysic

Cysic (Crypto-Systemic Identity & Computation) 是一个专注于[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)（ZKP）硬件加速的领先项目。它致力于通过专用的硬件设计（FPGA 和 ASIC）和软硬件协同优化，大幅提升 [ZKP](https://learnblockchain.cn/tags/zkp) 生成的速度和效率，旨在成为 ZK 生态系统的底层算力基础设施。

## 要解决的问题

随着 ZK-[Rollup](https://learnblockchain.cn/tags/Rollup) 和 [zkEVM](https://learnblockchain.cn/tags/zkEVM?map=EVM) 的兴起，[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)的生成（Proving）过程成为了整个系统的性能瓶颈。

1.  **计算密集型**：生成 [ZKP](https://learnblockchain.cn/tags/zkp) 涉及大量的密码学运算，如多标量乘法（MSM）和快速傅里叶变换（NTT），这对通用 CPU 来说极其繁重。
2.  **高延迟与高成本**：在普通硬件上生成复杂的 [zkEVM](https://learnblockchain.cn/tags/zkEVM?map=EVM) 证明可能需要数十分钟甚至数小时，且不仅消耗大量电力，还导致 Layer 2 的最终确认时间变长。
3.  **去中心化障碍**：如果证明生成只能依赖昂贵的数据中心级服务器，那么普通用户将无法参与证明过程，导致证明者（Prover）角色的中心化。

Cysic 旨在通过硬件加速解决上述问题，将证明生成时间缩短几个数量级。

## 实现机制与原理

Cysic 采取了软硬结合的优化策略，主要分为 FPGA 原型验证和 ASIC 芯片量产两个阶段。

### 硬件架构
*   **多标量乘法 (MSM) 加速**：MSM 占据了 ZK 证明生成约 60%-70% 的计算量。Cysic 设计了高度并行的流水线架构来处理椭圆曲线点运算。
*   **数论变换 (NTT) 加速**：针对大规模多项式运算，Cysic 优化了内存访问模式和带宽管理，以加速 NTT 计算。

### 产品形态
1.  **SolarMSM**：Cysic 早期基于 FPGA 开发的 MSM 加速方案，在基准测试中展现了超越同类竞品的性能。
2.  **专用 ASIC 芯片**：相比于 FPGA，ASIC 芯片在功耗和性能上具有更大的优势。Cysic 正在研发专用的 ZK 挖矿芯片，旨在像[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)矿机一样，通过特定的硬件高效产出证明。

### 证明即服务 (Proving-as-a-Service)
Cysic 不仅提供硬件，还构建了一个算力网络（Cysic Network）。在这个网络中：
*   **验证者/开发者**：提交证明任务。
*   **证明者 (Provers)**：利用 Cysic 的硬件算力完成任务并获得奖励。
这种模式形成了一个去中心化的 ZK 算力市场，降低了 ZK 项目方自建基础设施的门槛。

## 主要特点

*   **极致性能**：Cysic 的硬件方案旨在提供业界最快的证明生成速度，支持实时的 ZK 应用场景。
*   **广泛兼容性**：支持主流的证明系统（如 Plonk, [Groth16](https://learnblockchain.cn/tags/Groth16), [Halo2](https://learnblockchain.cn/tags/Halo2)）和椭圆曲线（如 BN254, BLS12-381），可服务于 Scroll, zkSync, Aztec 等多个 ZK-[Rollup](https://learnblockchain.cn/tags/Rollup) 项目。
*   **生态赋能**：作为“卖铲子”的角色，Cysic 通过提供廉价且快速的算力，间接推动了更复杂的 ZK 应用（如 ZK 机器学习 - ZKML）的落地。

## 推荐阅读

*   [Cysic Official Website](https://cysic.xyz/)
*   [Cysic Medium Blog](https://medium.com/@cysic)
*   [ZPrize Competition Results](https://www.zprize.io/) (Cysic 在 ZK 算法竞赛中的表现)

## 相关概念

*   **硬件加速 (Hardware Acceleration)**
*   **FPGA / ASIC**
*   **MSM (Multi-Scalar Multiplication)**
*   **NTT (Number Theoretic Transform)**
