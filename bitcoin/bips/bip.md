## BIP

BIP: Bitcoin Improvement Proposal, 即比特币改进提案， 是为比特币协议提出的新功能、改进、或信息提交的标准化文档。
BIP 的目的是为比特币社区提供一个透明、结构化和协作的方式来讨论和实现比特币协议的改进和变更。改进提案通过 [GitHub 库管理](https://github.com/bitcoin/bips) 。

### BIP 分类

BIP 主要分为以下几类：

* 标准跟踪 BIP（Standards Track BIP）： 对比特币核心协议、共识规则和网络协议的改进，如涉及比特币标准的定义，如交易格式和数据结构。
* 信息性 BIP（Informational BIP）： 提供比特币开发和设计方面的建议，不强制实施，帮助社区理解和讨论比特币相关主题。
* 流程 BIP（Process BIP）： 描述比特币开发和决策流程的改进，如 BIP 的流程本身， 对非技术性改进和操作流程的规范。

### BIP 生命周期

BIP 从提出到实施，一般经历以下几个阶段：草案阶段（Draft）、候选阶段（Proposed）、最终阶段（Final）

如下是一个生命周期图：

![alt text](https://img.learnblockchain.cn/pics/20240623210600.png)



### 所有有效 BIP 

BIP1: [ BIP 目的和指南](https://bips.dev/1/)

BIP2: [ BIP 流程，修订版](https://bips.dev/2/)

BIP8: [通过高度锁定的版本位](https://bips.dev/8/)

BIP9: [带有超时和延迟的版本位](https://bips.dev/9/)

BIP10: [多重签名交易分发](https://bips.dev/10/)

BIP11: [M-of-N 标准交易](https://bips.dev/11/)

BIP12: [OP_EVAL](https://bips.dev/12/)

BIP13: [支付到脚本哈希的地址格式](https://bips.dev/13/)

BIP14: [协议版本和用户代理](https://bips.dev/14/)

BIP15: [别名](https://bips.dev/15/)

BIP16: [支付到脚本哈希](https://bips.dev/16/)

BIP17: [OP_CHECKHASHVERIFY (CHV)](https://bips.dev/17/)

BIP18: [hashScriptCheck](https://bips.dev/18/)

BIP19: [M-of-N 标准交易（低 SigOp）](https://bips.dev/19/)

BIP20: [URI 方案](https://bips.dev/20/)

BIP21: [URI 方案](https://bips.dev/21/)

BIP22: [getblocktemplate - 基础](https://bips.dev/22/)

BIP23: [getblocktemplate - 联合挖矿](https://bips.dev/23/)

BIP30: [重复交易](https://bips.dev/30/)

BIP31: [Pong 消息](https://bips.dev/31/)

BIP32: [分层确定性钱包](https://bips.dev/32/)

BIP33: [分层节点](https://bips.dev/33/)

BIP34: [区块 v2，Coinbase 中的高度](https://bips.dev/34/)

BIP35: [mempool 消息](https://bips.dev/35/)

BIP36: [自定义服务](https://bips.dev/36/)

BIP37: [连接 Bloom 过滤](https://bips.dev/37/)

BIP38: [密码保护的私钥](https://bips.dev/38/)

BIP39: [用于生成确定性密钥的助记词](https://bips.dev/39/)

BIP42: [比特币的有限货币供应](https://bips.dev/42/)

BIP43: [确定性钱包的用途字段](https://bips.dev/43/)

BIP44: [确定性钱包的多账户层次结构](https://bips.dev/44/)

BIP45: [确定性 P2SH 多重签名钱包的结构](https://bips.dev/45/)

BIP47: [分层确定性钱包的可重用支付代码](https://bips.dev/47/)

BIP48: [多重签名钱包的多脚本层次结构](https://bips.dev/48/)

BIP49: [基于 P2WPKH 嵌套在 P2SH 中的账户派生方案](https://bips.dev/49/)

BIP50: [2013 年 3 月链分叉事后分析](https://bips.dev/50/)

BIP52: [耐用、低能耗的比特币 PoW](https://bips.dev/52/)

BIP60: [固定长度的“版本”消息（中继交易字段）](https://bips.dev/60/)

BIP61: [拒绝 P2P 消息](https://bips.dev/61/)

BIP62: [处理可塑性](https://bips.dev/62/)

BIP64: [getutxo 消息](https://bips.dev/64/)

BIP65: [OP_CHECKLOCKTIMEVERIFY](https://bips.dev/65/)

BIP66: [严格的 DER 签名](https://bips.dev/66/)

BIP67: [通过公钥排序的确定性支付到脚本哈希多重签名地址](https://bips.dev/67/)

BIP68: [使用共识强制的序列号的相对锁定时间](https://bips.dev/68/)

BIP69: [交易输入和输出的字典索引](https://bips.dev/69/)

BIP70: [支付协议](https://bips.dev/70/)

BIP71: [支付协议 MIME 类型](https://bips.dev/71/)

BIP72: [比特币：支付协议的 URI 扩展](https://bips.dev/72/)

BIP73: [使用“Accept”头进行支付请求 URL 的响应类型协商](https://bips.dev/73/)

BIP74: [在支付协议中允许零值 OP_RETURN](https://bips.dev/74/)

BIP75: [使用支付协议加密的带外地址交换](https://bips.dev/75/)

BIP78: [一个简单的 Payjoin 提案](https://bips.dev/78/)

BIP79: [Bustapay :: 一个实用的 coinjoin 协议](https://bips.dev/79/)

BIP80: [非染色投票池确定性多重签名钱包的层次结构](https://bips.dev/80/)

BIP81: [染色投票池确定性多重签名钱包的层次结构](https://bips.dev/81/)

BIP83: [动态分层确定性密钥树](https://bips.dev/83/)

BIP84: [基于 P2WPKH 账户的派生方案](https://bips.dev/84/)

BIP85: [从 BIP32 密钥链生成确定性熵](https://bips.dev/85/)

BIP86: [单密钥 P2TR 输出的密钥派生](https://bips.dev/86/)

BIP87: [确定性多重签名钱包的层次结构](https://bips.dev/87/)

BIP88: [分层确定性路径模板](https://bips.dev/88/)

BIP90: [埋藏部署](https://bips.dev/90/)

BIP91: [降低阈值的 Segwit MASF](https://bips.dev/91/)

BIP93: [codex32：带校验和的 SSSS 感知 BIP32 种子](https://bips.dev/93/)

BIP98: [快速默克尔树](https://bips.dev/98/)

BIP99: [共识规则更改的动机和部署（软/硬分叉）](https://bips.dev/99/)

BIP100: [通过矿工投票动态最大区块大小](https://bips.dev/100/)

BIP101: [增加最大区块大小](https://bips.dev/101/)

BIP102: [区块大小增加到 2MB](https://bips.dev/102/)

BIP103: [区块大小随技术增长](https://bips.dev/103/)

BIP104: ['Block75' - 类似难度的最大区块大小](https://bips.dev/104/)

BIP105: [基于共识的区块大小重新定位算法](https://bips.dev/105/)

BIP106: [动态控制的比特币区块大小最大上限](https://bips.dev/106/)

BIP107: [区块大小的动态限制](https://bips.dev/107/)

BIP109: [两百万字节大小限制，带 sigop 和 sighash 限制](https://bips.dev/109/)

BIP111: [NODE_BLOOM 服务位](https://bips.dev/111/)

BIP112: [CHECKSEQUENCEVERIFY](https://bips.dev/112/)

BIP113: [锁定时间计算的中值时间过去](https://bips.dev/113/)

BIP114: [默克尔化抽象语法树](https://bips.dev/114/)

BIP115: [使用脚本的通用反重播保护](https://bips.dev/115/)

BIP116: [MERKLEBRANCHVERIFY](https://bips.dev/116/)

BIP117: [尾调用执行语义](https://bips.dev/117/)

BIP118: [Taproot 脚本的 SIGHASH_ANYPREVOUT](https://bips.dev/118/)

BIP119: [CHECKTEMPLATEVERIFY](https://bips.dev/119/)

BIP120: [支付证明](https://bips.dev/120/)

BIP121: [支付证明 URI 方案](https://bips.dev/121/)

BIP122: [区块链引用/探索的 URI 方案](https://bips.dev/122/)

BIP123: [ BIP 分类](https://bips.dev/123/)

BIP124: [分层确定性脚本模板](https://bips.dev/124/)

BIP125: [选择性完全替换费用信号](https://bips.dev/125/)

BIP126: [异构输入脚本交易的最佳实践](https://bips.dev/126/)

BIP127: [简单的储备证明交易](https://bips.dev/127/)

BIP129: [比特币安全多重签名设置 (BSMS)](https://bips.dev/129/)

BIP130: [sendheaders 消息](https://bips.dev/130/)

BIP131: [“合并交易”规范（通配符输入）](https://bips.dev/131/)

BIP132: [基于委员会的  接受过程](https://bips.dev/132/)

BIP133: [feefilter 消息](https://bips.dev/133/)

BIP134: [灵活交易](https://bips.dev/134/)

BIP135: [广义版本位投票](https://bips.dev/135/)

BIP136: [Bech32 编码的交易位置引用](https://bips.dev/136/)

BIP137: [使用私钥签名消息](https://bips.dev/137/)

BIP140: [规范化 TXID](https://bips.dev/140/)

BIP141: [隔离见证（共识层）](https://bips.dev/141/)

BIP142: [隔离见证的地址格式](https://bips.dev/142/)

BIP143: [版本 0 见证程序的交易签名验证](https://bips.dev/143/)

BIP144: [隔离见证（对等服务）](https://bips.dev/144/)

BIP145: [隔离见证的 getblocktemplate 更新](https://bips.dev/145/)

BIP146: [处理签名编码的可塑性](https://bips.dev/146/)

BIP147: [处理虚拟堆栈元素的可塑性](https://bips.dev/147/)

BIP148: [强制激活 segwit 部署](https://bips.dev/148/)

BIP149: [隔离见证（第二次部署）](https://bips.dev/149/)

BIP150: [对等身份验证](https://bips.dev/150/)

BIP151: [点对点通信加密](https://bips.dev/151/)152: [紧凑区块中继](https://bips.dev/152/)

BIP154: [通过对等指定挑战进行速率限制](https://bips.dev/154/)

BIP155: [addrv2 消息](https://bips.dev/155/)

BIP156: [蒲公英 - 隐私增强路由](https://bips.dev/156/)

BIP157: [客户端区块过滤](https://bips.dev/157/)

BIP158: [轻客户端的紧凑区块过滤器](https://bips.dev/158/)

BIP159: [NODE_NETWORK_LIMITED 服务位](https://bips.dev/159/)

BIP171: [货币/汇率信息 API](https://bips.dev/171/)

BIP173: [原生 v0-16 见证输出的 Base32 地址格式](https://bips.dev/173/)

BIP174: [部分签名的比特币交易格式](https://bips.dev/174/)

BIP175: [支付合约协议](https://bips.dev/175/)

BIP176: [比特单位](https://bips.dev/176/)

BIP178: [版本扩展 WIF](https://bips.dev/178/)

BIP179: [支付接收者标识符的名称](https://bips.dev/179/)

BIP180: [区块大小/重量欺诈证明](https://bips.dev/180/)

BIP197: [哈希时间锁定抵押合约](https://bips.dev/197/)

BIP199: [哈希时间锁定合约交易](https://bips.dev/199/)

BIP300: [算力托管（共识层）](https://bips.dev/300/)

BIP301: [盲合并挖矿（共识层）](https://bips.dev/301/)

BIP310: [Stratum 协议扩展](https://bips.dev/310/)

BIP320: [通用用途的 nVersion 位](https://bips.dev/320/)

BIP322: [通用签名消息格式](https://bips.dev/322/)

BIP324: [版本2 P2P 加密传输协议](https://bips.dev/324/)

BIP325: [Signet](https://bips.dev/325/)

BIP326: [taproot 交易中的反费用狙击](https://bips.dev/326/)

BIP327: [BIP340 兼容的多重签名的 MuSig2](https://bips.dev/327/)

BIP329: [钱包标签导出格式](https://bips.dev/329/)

BIP330: [交易公告对账](https://bips.dev/330/)

BIP331: [祖先包中继](https://bips.dev/331/)

BIP337: [压缩交易](https://bips.dev/337/)

BIP338: [禁用交易中继消息](https://bips.dev/338/)

BIP339: [基于 WTXID 的交易中继](https://bips.dev/339/)

BIP340: [secp256k1 的 Schnorr 签名](https://bips.dev/340/)

BIP341: [Taproot：SegWit 版本 1 支出规则](https://bips.dev/341/)

BIP342: [Taproot 脚本的验证](https://bips.dev/342/)

BIP343: [Taproot 部署的强制激活](https://bips.dev/343/)

BIP345: [OP_VAULT](https://bips.dev/345/)

BIP347: [Tapscript 中的 OP_CAT](https://bips.dev/347/)

BIP350: [v1+ 见证地址的 Bech32m 格式](https://bips.dev/350/)

BIP351: [私人支付](https://bips.dev/351/)

BIP352: [静默支付](https://bips.dev/352/)

BIP353: [DNS 支付指令](https://bips.dev/353/)

BIP370: [PSBT 版本2](https://bips.dev/370/)

BIP371: [PSBT 的 Taproot 字段](https://bips.dev/371/)

BIP372: [PSBT 的支付合约调整字段](https://bips.dev/372/)

BIP380: [输出脚本描述符的一般操作](https://bips.dev/380/)

BIP381: [非 Segwit 输出脚本描述符](https://bips.dev/381/)

BIP382: [Segwit 输出脚本描述符](https://bips.dev/382/)

BIP383: [多重签名输出脚本描述符](https://bips.dev/383/)

BIP384: [combo() 输出脚本描述符](https://bips.dev/384/)

BIP385: [raw() 和 addr() 输出脚本描述符](https://bips.dev/385/)

BIP386: [tr() 输出脚本描述符](https://bips.dev/386/)

BIP387: [Tapscript 多重签名输出脚本描述符](https://bips.dev/387/)

BIP388: [描述符钱包的钱包策略](https://bips.dev/388/)

BIP389: [多路径描述符密钥表达式](https://bips.dev/389/)

BIP431: [固定的拓扑限制](https://bips.dev/431/)