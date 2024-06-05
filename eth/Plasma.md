# Plasma

## 什么是Plasma？

Plasma是一个用于改善以太坊这类公共区块链可扩展性的框架。Plasma链是一个锚定到以太坊主网的独立区块链，但却在链下执行交易，有自己的区块验证机制。Plasma有时被称作“子”链，其本质是以太坊主网的较小副本。Plasma链使用欺诈证明来仲裁争议。

Plasma合约有一项功能是作为链梁，让用户可以在以太坊主网和Plasma链之间转移资产。虽然这使它们类似于侧链，但Plasma链至少在某种程度上受益于以太坊主网的安全性。 这一点不同于单独负责其安全性的侧链。

## Plasma基本框架

Plasma框架的基本组成部分包括：链下计算、状态承诺、入口和出口和争议仲裁。

### <u>链下计算</u>

以太坊的当前处理速度限制为每秒15～20个交易，降低了短期内处理更多用户的扩容可能性。这个问题之所以存在，主要是因为以太坊的共识机制需要许多对等节点来验证对区块链状态的每次更新。

尽管以太坊的共识机制对于安全性来说是必要的，但它可能并不适用于所有用例。 例如，由于双方之间存在某种信任，Alice 可能不需要每天向 Bob 支付一杯由整个以太坊网络验证的咖啡。

Plasma 假设以太坊主网不需要验证所有交易。 相反，我们可以在主网外处理交易，使节点不必验证每笔交易。

链下计算是必要的，因为 Plasma 链可以优化速度和成本。 例如，一个 Plasma 链可能，而且大多数情况下都使用单个“运营商”来管理交易的排序和执行。 由于只有一个实体验证交易，Plasma 链上的处理速度比以太坊主网更快。

### <u>状态承诺</u>

虽然 Plasma 在链下执行交易，但它们是在以太坊主执行层上结算的，否则，Plasma 链无法从以太坊的安全保证中受益。 但是在不知道 Plasma 链状态的情况下完成链下交易会破坏安全模型并让无效交易扩散。 这就是为什么运营商，即负责在 Plasma 链上生产区块的实体，需要定期在以太坊上发布“状态承诺”。

承诺方案(opens in a new tab)是一种加密技术，用于承诺价值或声明而不向另一方透露。 承诺是“有约束力的”，因为一旦你承诺了，就不能改变价值或声明。Plasma 中的状态承诺采用“Merkle 根”的形式（源自Merkle树），运营商每隔一段时间将其发送到以太坊链上的Plasma合约。

Merkle 根是能够压缩大量信息的密码原语。Merkle根（在此情况下也称为“区块根”）可以代表区块中的所有交易。 Merkle根还可以更容易地验证一小部分数据是否是较大数据集的一部分。 例如，用户可以生成Merkle证明来证明交易包含在特定的区块中。

Merkle 根对于向以太坊提供有关链下状态的信息非常重要。 你可以将 Merkle 根视为“保存点”：运营商表示，“这是 Plasma 链在 x 时间点的状态，这是 Merkle 根作为证明。” 运营商使用 Merkle 根对 Plasma 链的当前状态进行承诺，这就是为什么它被称为“状态承诺”。

### <u>入口和出口</u>

为了让以太坊用户使用Plasma，需要有一种机制在主网和Plasma链之间转移资金。但是，我们不能随意将以太币发送到Plasma链上的地址，因为这些链是不兼容的，因此要么交易失败，要么会导致资金损失。

Plasma使用在以太坊上运行的主合约来处理用户的入口和出口。该主合约还负责跟踪状态承诺并通过欺诈证明惩罚不诚实行为。

#### 进入Plasma链

要进入Plasma链，用户必须在Plasma合约中存入以太币或任何ERC-20代币。监视合约存款的Plasma运营商重新创建与用户的初始存款相等的金额，并将其释放到她在Plasma链上的地址。用户需要证明在子链上收到资金，然后才能使用这些资金进行交易。

#### 退出Plasma链

虽然以太坊有关于Plasma链状态的信息，但它无法验证信息是否真实。恶意用户可能会做出不正确的断言，并提供虚假证据来支持该声明而侥幸逃脱。

为防止恶意取款，人们引入了“挑战期”的概念。 在挑战期内（通常为一周），任何人都可以使用欺诈证明来挑战取款请求。 如果挑战成功，则取款请求被拒绝。

但是，通常情况下，用户是诚实的，并对他们拥有的资金做出正确的声明。 在这种情况下，用户将通过向 Plasma 合约提交交易，在根链（以太坊）上发起取款请求。

用户还必须提供 Merkle 证明，验证在 Plasma 链上创建的资金的交易是否包含在区块中。 这对于 Plasma 的迭代是必要的，例如最小可行 Plasma(opens in a new tab) 使用未花费的交易输出 (UTXO)模型。

其他的，如 Plasma Cash(opens in a new tab)，将资金表示为非同质化代币，而不是未花费的交易输出。 在这种情况下，取款需要证明 Plasma 链上代币的所有权。 这是通过提交涉及代币的两个最新交易并提供 Merkle 证明来验证这些交易是否包含在区块中来完成的。

用户还必须在取款请求中添加保证金，作为诚实行为的保证。 如果挑战者证明用户的取款请求无效，那么用户的保证金将被罚没，其中一部分作为奖励交给挑战者。

如果在没有任何人提供欺诈证明的情况下经过挑战期，用户的取款请求被认为是有效的，允许从以太坊上的 Plasma 合约中取回存款。

### <u>争议仲裁</u>

与任何区块链一样，Plasma 链需要一种机制确保交易的完整性，防止参与者的恶意行为（例如，资金双重支付）。 为此，Plasma 链使用欺诈证明来仲裁有关状态转换有效性的争议并惩罚不良行为。 欺诈证明可作为一种机制，Plasma 子链通过它向父链或根链提出申诉。

欺诈证明只是声称特定状态转换无效。 例如，如果用户 Alice 尝试两次花费相同的资金。 也许她在与 Bob 的交易中花费了未花费的交易输出，并希望在另一笔交易中花费相同的未花费的交易输出（现在是 Bob 的）。

为了防止取款，Bob 将通过提供 Alice 在之前的交易中花费上述未花费的交易输出的证据以及交易包含在区块中的 Merkle 证明来构建欺诈证明。 在 Plasma Cash 中使用同样的流程：Bob 需要提供证据，证明 Alice 先前已经转让她尝试提取的代币。

如果 Bob 挑战成功，Alice 的取款请求将被取消。 但是，这种方法依赖于 Bob 监视链中取款请求的能力。 如果 Bob 离线，那么一旦挑战期过去，Alice 就可以处理恶意取款。

## Plasma的优缺点

**优点**：

* Plasma链提供了高吞吐量和较低的交易成本
* 适合任意用户之间的交易（如果双方的交易都建立在 Plasma 链上，则这个交易几乎没有成本）
* Plasma链可以适应与主链无关的特定用例，包括企业在内的任何人都可以定制 Plasma 智能合约，以提供可在不同环境中工作的可扩展基础设施
* 通过将计算和存储转移到链下来减少以太坊主网的负载

**缺点**：

* 不支持通用计算（无法运行智能合约），只支持特定逻辑的基本通证转账、兑换和几种其他交易类型
* 需要定期监视网络（活性要求）或委托其他人监视网络，以确保你的资金安全
* 依靠一个或多个运营者来存储数据，并根据其需求提供数据
* 为了等待挑战期，提款会延迟几天。 对于同质化资产，流动性提供者可以缓解这种情况，但存在相关的资本成本
* 如果太多用户同时尝试退出，可能会导致以太坊主网堵塞

## Plasma与侧链、分片技术的区别

Plasma、侧链、分片技术有一定的相似度，因为它们都以某种方式连接到以太坊主网。 然而，连接到以太坊主网的级别和强度有所不同，这影响了这些扩容方案的安全属性。

### Plasma与侧链

侧链是一条独立运行的区块链，通过双向桥梁连接到以太坊主网。 桥梁允许用户在两条区块链之间兑换代币以便在侧链进行交易，这缓解了以太坊主网上的拥塞并提升了可扩展性。 侧链采用独立的共识机制，它们通常比以太坊主网小得多。 因此，将资产桥接到这些区块链会增加风险；由于侧链模型中缺少从以太坊主网继承的安全保障，在侧链受到攻击时用户会面临资金损失的风险。

相反，Plasma 链的安全性源自以太坊主网。 这让它们明显比侧链更安全。 侧链和 Plasma 链都可以采用不同的共识协议。但区别是 Plasma 链在以太坊主网上发布每个区块的默克尔根。 区块根是小段信息，可用来验证在 Plasma 链上进行的交易相关信息。 如果 Plasma 链遭到攻击，用户可以用适当的证据安全地将资金撤回到主网。

### Plasma与分片

Plasma 链和分片链都定期向以太坊主网发布加密证明。 但是两者具有不同的安全属性。

分片链向主网提交“汇总头”，其中包含有关每个数据分片的详细信息。 主网上的节点验证和执行数据分片的有效性，减少无效分片转换的可能性并防止网络上出现恶意活动。

Plasma 不同于此，因为主网只接收最少量的子链状态信息。 这意味着主网无法有效验证子链上进行的交易，降低了交易的安全性。

***

节选文章：

https://ethereum.org/zh/developers/docs/scaling/plasma/