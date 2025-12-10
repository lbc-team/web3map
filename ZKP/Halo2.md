# Halo2

## 概念简介

Halo 是 Zcash 的新型零知识证明机制，无需 Trusted Setup 过程，具体可参见论文《Halo: Recursive Proof Composition without a Trusted Setup》。

Halo2 由 ECC 公司在 Halo 的基础上，使用 PLONK 算法进行升级改造，充分利用了 PLONK 的特性，如 custom gate、PLONKup 等，使得开发零知识证明电路更加高效和方便。

## 核心技术

**递归证明组合**：Halo 论文中描述了递归证明组合（recursive proof composition）的一种具体表现形式，它将 Sonic 论文中描述的 Polynomial IOP 剥离出来，用基于 inner product argument 的 polynomial commitment scheme 代替了基于 pairing 的 polynomial commitment。

**Pasta Curves**：Halo2 采用 Pasta curves（Pallas 和 Vesta）实现 recursive zk-SNARKs 证明系统，提供了一种新的[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)方案，它可以实现无需信任设置的递归证明。

**PLONK 集成**：Halo2 进行了进一步的优化，主要是 Polynomial IOP 方向。相比之下，由于 PLONK 支持更灵活的电路设计，而最终被选中。

## 主要特性

**无需 Trusted Setup**：这是 Halo/Halo2 最重要的特性之一，消除了 trusted setup 的安全风险和复杂性。

**递归证明**：Halo 支持递归证据组织，可以将多个证明组合成一个证明，实现证明的聚合。

**线性验证时间**：与其他新的 [zk-SNARK](https://learnblockchain.cn/tags/zkSNARK) 构建不同，Halo 的验证时间是线性的（虽然后来的优化降低了这个复杂度）。

## Halo2 的改进

**灵活的电路设计**：通过 PLONK，Halo2 支持：
- Custom gates（自定义门）
- Lookups（查找表，PLONKup）
- 更灵活的约束系统

**优化的性能**：相比原始的 Halo，[Halo2](https://learnblockchain.cn/tags/Halo2) 在证明生成速度和验证效率上都有显著提升。

## 在 Zcash Orchard 中的应用

**Orchard 升级**：Zcash Orchard 采用了 halo2 ZK（[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)）框架，电路部分基于 halo2 gadgets 里面的 sinsemilla、ecc、merkle、poseidon 等部分，并集成了多种 chips。

**组件集成**：
- **Sinsemilla**：哈希函数
- **ECC**：椭圆曲线运算
- **Merkle**：Merkle 树证明
- **Poseidon**：另一种哈希函数

## 技术优势

1. **无需 Trusted Setup**：消除了最大的安全隐患
2. **递归友好**：可以高效地证明证明
3. **通用性**：一次 setup 可用于所有电路
4. **渐进式改进**：支持持续的协议升级

## 与其他方案对比

| 特性 | [Halo2](https://learnblockchain.cn/tags/Halo2) | [Groth16](https://learnblockchain.cn/tags/Groth16) | [PLONK](https://learnblockchain.cn/tags/PLONK) |
|------|-------|---------|-------|
| Trusted Setup | 不需要 | 电路特定 | 通用（一次）|
| 证明大小 | 中等 | 极小 | 小 |
| 递归 | 原生支持 | 困难 | 可能 |
| 电路灵活性 | 高 | 低 | 高 |

## 推荐阅读

- [Halo——zcash新的零知识证明机制 - CSDN](https://blog.csdn.net/mutourend/article/details/100764027)
- [Zcash halo2 背后技术衍化介绍 - CSDN](https://blog.csdn.net/mutourend/article/details/114059130)
- [Halo2：原理剖析 - 知乎](https://zhuanlan.zhihu.com/p/385134321)
- [探秘HALO2：构建隐私保护的未来 - CSDN](https://blog.csdn.net/gitblog_00028/article/details/139385741)

## 相关概念

- **Zcash**
- **递归证明**
- **[PLONK](https://learnblockchain.cn/tags/PLONK)**
- **Pasta Curves**
- **Inner Product Argument**
