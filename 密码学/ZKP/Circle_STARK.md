# Circle STARK

## 概念简介

Circle STARK 是由 StarkWare 和 Polygon Labs 团队联合开发的协议，使用 Mersenne 素数域 M31。根据 Polygon Labs 和 StarkWare 发布的白皮书，Circle STARK 预计将加速零知识 [Rollup](https://learnblockchain.cn/tags/Rollup) 的证明过程。

Circle STARK 结合 M31 素数域大大提高了 STARK 证明效率，新的 Circle STARK 证明应该比当前的 STARK 证明更快完成。这项研究的数学原理很复杂，但经典圆的使用将 STARK 的证明能力提高了 100 倍。

## 技术创新

**Mersenne 素数域（M31）**：Circle STARK 采用 M31 = 2^31 - 1 这个特殊的 Mersenne 素数作为有限域，这使得算术运算更加高效。

**圆曲线几何**：利用圆曲线的数学特性优化证明生成过程，相比传统方法有显著性能提升。

## Stwo 证明系统

基于 Circle STARK 协议，StarkWare 开发了超快证明系统 Stwo，显著改进了现有的 Stone prover。Polygon 预计该技术将带来 7 到 10 倍的性能提升。

## 行业影响

StarkWare 和 Polygon Labs 的合作可能令人惊讶，因为这两个团队在更广泛的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)扩展领域经常相互竞争。该白皮书于周三发布，由 Polygon Labs 的 Ulrich Haböck 以及 StarkWare 的 David Levit 和 Shahar Papini 共同撰写，目前可在线获取。

这一发展代表了区块链可扩展性[零知识证明](https://learnblockchain.cn/tags/%E9%9B%B6%E7%9F%A5%E8%AF%86%E8%AF%81%E6%98%8E)技术的重大进步。

## 推荐阅读

- [Circle STARK和Stwo令人着迷之处 - CSDN](https://blog.csdn.net/mutourend/article/details/136857977)
- [Polygon and StarkWare launch new cryptographic proof "Circle STARK"](https://www.coinlive.com/news/polygon-and-starkware-launch-new-cryptographic-proof-circle-stark)
- [Polygon, StarkWare Tout New 'Circle STARKs' as Breakthrough](https://www.coindesk.com/tech/2024/02/21/polygon-starkware-tout-new-circle-starks-as-breakthrough-for-zero-knowledge-proofs)

## 相关概念

- **[zkSTARK](https://learnblockchain.cn/tags/zkSTARK)**
- **StarkWare**
- **Polygon**
- **Mersenne素数**
- **Stwo证明系统**
