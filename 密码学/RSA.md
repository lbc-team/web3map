# RSA

## 概念简介

RSA 加密算法是一种非对称加密算法，在公开密钥加密和电子商业中被广泛使用。RSA 是由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）在 1977 年于麻省理工学院（MIT）一起提出的，RSA 就是他们三人姓氏开头字母的组合。

RSA 算法的安全性基于大整数分解的数学难题：将两个大质数相乘很容易，但将其乘积分解回原来的质数在计算上极其困难。这种单向陷门函数的特性使得 RSA 成为最早的实用公钥加密系统之一，也是迄今为止应用最广泛的非对称加密算法。

## 核心原理

**大整数分解困难性**

对极大整数做因数分解的难度决定了 RSA 算法的可靠性。换言之，对一极大整数做因数分解愈困难，RSA 算法愈可靠。大整数的因数分解，是一件非常困难的事情。目前，除了暴力破解，还没有发现别的有效方法。

**数学基础**

RSA 算法基于以下数学事实：
1. 选择两个大质数 p 和 q 很容易
2. 计算它们的乘积 N = p × q 很容易
3. 但从 N 分解出 p 和 q 极其困难
4. 欧拉函数 φ(N) = (p-1)(q-1) 是密钥生成的关键

## 密钥生成

**生成步骤：**

1. **选择质数**：准备两个互质数 p，q。这两个数不能太小，太小则会容易破解
2. **计算模数**：将 p 乘以 q 就是 N。如果互质数 p 和 q 足够大，那么根据目前的计算机技术和其他工具，至今也没能从 N 分解出 p 和 q
3. **计算欧拉函数**：φ(N) = (p-1)(q-1)
4. **选择公钥指数**：选择一个小于 φ(N) 且与 φ(N) 互质的整数 e，通常选择 65537（0x10001）
5. **计算私钥指数**：计算 e 的模反元素 d，使得 (e × d) mod φ(N) = 1
6. **密钥对**：
   - 公钥：(N, e)
   - 私钥：(N, d)

**安全考虑**：质数 p 和 q 在密钥生成后必须销毁，泄露它们将导致私钥可以被计算出来。

## 加密与解密

**加密过程**

RSA 加密是对明文的 e 次方后除以 N 后求余数的过程：
```
密文 C = M^e mod N
```
其中 M 是明文，e 和 N 是公钥

**解密过程**

对密文进行 d 次方后除以 N 的余数就是明文，这就是 RSA 解密过程：
```
明文 M = C^d mod N
```
其中 C 是密文，d 和 N 是私钥

**数学正确性**

根据欧拉定理和费马小定理，可以证明：
```
(M^e)^d mod N = M^(ed) mod N = M
```

**密文长度**：生成密文的长度等于密钥长度。密钥长度越大，生成密文的长度也就越大，加密的速度也就越慢，而密文也就越难被破解掉。

## 数字签名

RSA 不仅可以用于加密，还可以用于数字签名。

**签名过程（私钥签名）**

1. 对消息 M 计算哈希值 H = Hash(M)
2. 使用私钥对哈希值签名：S = H^d mod N
3. 将签名 S 和消息 M 一起发送

**验证过程（公钥验证）**

1. 接收者计算消息的哈希值 H' = Hash(M)
2. 使用公钥解密签名：H'' = S^e mod N
3. 验证 H' = H''，相等则签名有效

**应用场景**：
- 软件发布验证（确保软件未被篡改）
- SSL/TLS 证书
- 代码签名
- 电子文档签署

## 填充方案

为了安全性，RSA 加密和签名都需要使用适当的填充方案，不能直接对原始数据进行运算。

**PKCS#1 v1.5**

最早的填充方案，简单但存在安全漏洞：
- 1998 年发现 Bleichenbacher 攻击
- 仅应用于支持遗留协议
- 不推荐用于新系统

**OAEP（Optimal Asymmetric Encryption Padding）**

现代推荐的加密填充方案：
- 由 Bellare 和 Rogaway 提出
- 在 PKCS#1 v2 和 RFC 3447 中标准化
- 提供概率性加密
- 经过安全性证明，可抵御多种攻击
- 使用 MGF1（掩码生成函数）和哈希算法（如 SHA-256）
- 是新协议和应用的推荐选择

**PSS（Probabilistic Signature Scheme）**

推荐的签名填充方案：
- 在 RFC 3447 中定义
- 比 PKCS#1 v1.5 更复杂但具有安全性证明
- 是新协议 RSA 签名的推荐选择
- 注意：OAEP 不能用于签名，仅用于加密

## 密钥长度建议

**历史和当前建议：**

- **512 位**：已被破解（1999 年）
- **768 位**：已被破解（2009 年），这是目前被破解的最长 RSA 密钥
- **1024 位**：基本安全，但不再推荐使用
- **2048 位**：NIST 建议的最低长度，极其安全，当前标准
- **3072 位**：更高安全级别，推荐用于长期保护
- **4096 位**：最高常用级别，适用于极高安全需求

**安全级别对比：**

| RSA 密钥长度 | 对称加密等效 | [椭圆曲线](https://learnblockchain.cn/tags/%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF)等效 | 适用场景 |
|-------------|-------------|-------------|---------|
| 1024 位     | 80 位       | 160 位      | 已淘汰 |
| 2048 位     | 112 位      | 224 位      | 当前标准 |
| 3072 位     | 128 位      | 256 位      | 推荐使用 |
| 7680 位     | 192 位      | 384 位      | 高安全性 |
| 15360 位    | 256 位      | 521 位      | 极高安全性 |

**未来趋势**：预计 RSA 2048 位的安全性只能持续到 2030 年。

## RSA vs ECC 对比

**密钥长度**

在相同安全级别下，ECC 的密钥长度远小于 RSA：
- 达到 112 位对称密钥的等效加密强度，需要 RSA 2048 位密钥，但只需要 ECC 224 位密钥
- 128 位安全加密需要 3072 位 RSA 密钥，但只需要 256 位 ECC 密钥
- 256 位安全级别需要 15360 位 RSA 密钥，但只需 512 位 ECC 密钥

**性能对比**

ECC 被认为是 RSA 的继任者，因为在相同的安全级别上使用比 RSA 更小的密钥和签名，并提供非常快速的密钥生成、快速的密钥协商和快速的签名。

- RSA 的主要缺点是速度：比对称加密算法慢约 1000 倍
- 在 Apache 和 IIS 服务器采用 ECC 算法，Web 服务器响应时间比 RSA 快十几倍
- 更短的密钥长度意味着设备需要更少的处理能力来加密和解密数据
- ECC 非常适合移动设备、物联网和其他计算能力更有限的用例

**量子计算威胁**

RSA 和 ECC 都是量子不安全的：
- Shor 量子算法可以在多项式时间内分解大整数和解决离散对数问题
- 两者都需要向后量子密码算法过渡
- ECC 基于超奇异的[椭圆曲线](https://learnblockchain.cn/tags/%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF)同源密码术，破解难度更大，相对不太容易受到量子计算的影响
- 对称加密如 AES-256 是抗量子安全的

## 应用场景

**SSL/TLS 证书**

HTTPS 网站使用 RSA 证书进行身份验证和密钥交换：
- 服务器使用 RSA 私钥证明身份
- 通常 RSA 用于身份验证，对称加密用于实际数据传输
- 现代 TLS 1.3 倾向于使用 ECC

**SSH 密钥**

安全外壳协议支持 RSA 密钥认证：
- `ssh-keygen -t rsa -b 4096` 生成 RSA 密钥对
- 公钥部署到服务器，私钥保留在客户端
- 现代实践推荐使用 Ed25519 替代 RSA

**PGP/GPG 加密**

电子邮件加密和文件加密：
- 使用 RSA 加密对称密钥
- 对称密钥用于加密实际内容
- 混合加密方案结合两者优势

**代码签名**

软件开发者签名应用程序和更新：
- Apple、Microsoft、Android 都使用 RSA 签名
- 防止恶意软件和篡改
- 建立软件来源的可信性

**数字证书**

PKI（公钥基础设施）体系：
- X.509 证书使用 RSA 公钥
- CA（证书颁发机构）使用 RSA 签名证书
- 浏览器验证网站证书链

## 安全性分析

**已知攻击**

1. **小指数攻击**：如果公钥指数 e 太小（如 3），可能存在风险
2. **时间攻击**：通过测量解密时间推断私钥信息
3. **填充攻击**：如 Bleichenbacher 攻击针对 PKCS#1 v1.5
4. **侧信道攻击**：通过功耗分析、电磁泄漏等获取信息

**防护措施**

- 使用推荐的密钥长度（至少 2048 位）
- 使用安全的填充方案（OAEP、PSS）
- 正确实现常数时间算法
- 使用硬件安全模块（HSM）保护私钥
- 定期轮换密钥

**破解难度**

目前被破解的最长 RSA 密钥是 768 位，这也说明了更长密钥的安全性。破解 RSA-2048 需要的计算资源在当前技术下是不可行的，但量子计算的出现可能改变这一局面。

## 实现和标准

**标准规范**

- **PKCS#1**：RSA Laboratories 发布，定义 RSA 密钥格式和操作
- **RFC 8017**：PKCS #1 v2.2 的最新标准
- **FIPS 186-4**：美国联邦标准，定义 [RSA](https://learnblockchain.cn/tags/RSA) 签名
- **X.509**：数字证书标准

**常用库**

- **OpenSSL**：C 语言，最广泛使用的加密库
- **Bouncy Castle**：Java/C# 实现
- **PyCrypto / Cryptography**：Python 实现
- **Crypto++**：C++ 实现
- **WebCrypto API**：浏览器内置加密 API

## 优势与局限

**优势：**
- 成熟可靠，经过 40 多年验证
- 广泛支持，几乎所有系统都支持
- 实现简单，数学原理易于理解
- 同时支持加密和签名

**局限：**
- 速度慢，比对称加密慢约 1000 倍
- 密钥长度大，占用更多存储和带宽
- 量子不安全，需要向 PQC 迁移
- 被 ECC 逐渐取代

## 未来展望

**迁移到 ECC**

专家预测 [RSA](https://learnblockchain.cn/tags/RSA) 将被 ECC 取代为当前标准，因为 ECC 提供更好的性能和更短的密钥。

**后量子密码学**

量子计算的出现将对现有的加密算法提出巨大挑战，许多现有的加密算法，如 [RSA](https://learnblockchain.cn/tags/RSA) 和 [ECC](https://learnblockchain.cn/tags/ECC)，可能无法抵御量子计算的攻击。需要过渡到格密码、基于哈希的签名等后量子算法。

**混合方案**

在过渡期间，使用 [RSA](https://learnblockchain.cn/tags/RSA)/[ECC](https://learnblockchain.cn/tags/ECC) 与后量子算法的混合方案，确保至少一个算法安全即可。

## 推荐阅读

**中文资源：**
- [RSA算法原理（一）- 阮一峰](https://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)
- [RSA算法原理（二）- 阮一峰](https://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html)
- [密码学基础 | RSA算法详解及证明 - 知乎](https://zhuanlan.zhihu.com/p/561733119)
- [RSA算法公钥、私钥及数字签名加密流程分步解析 - 知乎](https://zhuanlan.zhihu.com/p/462157596)
- [RSA加密及数字签名详解 - 知乎](https://zhuanlan.zhihu.com/p/299786289)
- [公钥，私钥和数字签名这样最好理解 - CSDN](https://blog.csdn.net/21aspnet/article/details/7249401)
- [浅谈RSA算法与大整数分解 - CSDN](https://blog.csdn.net/xbb224007/article/details/81122544)
- [RSA加密演算法 - 维基百科](https://zh.wikipedia.org/zh-hans/RSA加密演算法)

**性能对比：**
- [AES vs RSA vs ECC - 阿萍的博客](https://aping-dev.com/index.php/archives/596/)
- [RSA与ECDSA：选择指南 - CSDN](https://blog.csdn.net/seccloud/article/details/8189147)
- [加密算法RSA与ECC的对比 - 数安时代](https://www.trustauth.cn/news/security-news/30260.html)
- [RSA和ECC区别 - 阿里云](https://help.aliyun.com/zh/ssl-certificate/what-are-the-differences-between-the-rsa-and-ecc-algorithms)

**英文资源：**
- [RSA Cryptography Specifications - RFC 8017](https://datatracker.ietf.org/doc/html/rfc8017)
- [So How Does Padding Work in RSA? - Medium](https://medium.com/asecuritysite-when-bob-met-alice/so-how-does-padding-work-in-rsa-6b34a123ca1f)
- [The Cryptography Handbook: RSA PKCSv1.5, OAEP, and PSS - FreeCodeCamp](https://www.freecodecamp.org/news/the-cryptography-handbook-rsa-algorithm/)
- [RSA Signature and Encryption Schemes](https://cryptosys.net/pki/manpki/pki_rsaschemes.html)

## 相关概念

- **公钥密码学**
- **[椭圆曲线密码学](https://learnblockchain.cn/tags/椭圆曲线密码学)**
- **数字签名**
- **PKCS#1**
- **OAEP**
- **PSS**
- **SSL/TLS**
- **后量子密码学**
- **大整数分解**
- **欧拉函数**
