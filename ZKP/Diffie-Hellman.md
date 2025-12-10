# Diffie-Hellman 密钥交换

## 概念简介

Diffie-Hellman 密钥交换协议是由 Whitfield Diffie 和 Martin Hellman 在 1976 年发表的开创性论文《New Directions in Cryptography》中提出的。这是第一个公开发表的公钥加密算法，允许两方在不安全的信道上建立共享密钥。

该协议的安全性基于离散对数问题（Discrete Logarithm Problem, DLP）的困难性，即在已知 g^x mod p 的情况下，求解 x 是计算上困难的。

## 核心原理

**基本思想**：两方各自生成私钥，通过公开信道交换基于私钥计算的公开值，最后各自独立计算出相同的共享密钥。

**数学基础：**
1. 选择大素数 p 和生成元 g（公开参数）
2. Alice 选择私钥 a，计算 A = g^a mod p
3. Bob 选择私钥 b，计算 B = g^b mod p
4. Alice 和 Bob 交换 A 和 B
5. Alice 计算共享密钥 K = B^a mod p
6. Bob 计算共享密钥 K = A^b mod p
7. 由于 B^a = (g^b)^a = g^(ab) = (g^a)^b = A^b，双方得到相同的密钥

## 椭圆曲线变体（ECDH）

**椭圆曲线 Diffie-Hellman (ECDH)**：在椭圆曲线上实现 Diffie-Hellman，使用点加法代替模幂运算。

**优势：**
- 更短的密钥长度（256 位 ECDH ≈ 3072 位 DH）
- 更快的计算速度
- 更少的带宽需求
- 相同安全级别下更高效

**广泛应用**：ECDH 在现代加密协议中广泛使用，如 TLS 1.3、Signal 协议、WhatsApp 加密等。

## 安全性

**离散对数困难性**：攻击者即使知道 g、p、A 和 B，在计算上也难以求出 a 或 b，因此无法计算共享密钥 K。

**中间人攻击（MITM）**：DH 协议本身不提供身份认证，容易受到中间人攻击。攻击者可以分别与 Alice 和 Bob 建立密钥交换。

**防御措施**：
- 使用数字证书进行身份认证
- 结合数字签名验证公钥
- 使用认证的 DH 变体（如 Station-to-Station 协议）

**量子威胁**：Shor 算法可以在多项式时间内解决离散对数问题，因此 DH 在量子计算机面前是脆弱的。

## 应用场景

1. **TLS/SSL**：在建立 HTTPS 连接时协商会话密钥
2. **SSH**：安全远程登录中的密钥交换
3. **VPN**：IPsec 中使用 DH 建立隧道密钥
4. **即时通讯**：Signal、WhatsApp 等使用 ECDH
5. **区块链**：节点间安全通信

## 变体和扩展

**临时 Diffie-Hellman (DHE/ECDHE)**：每次会话使用新的临时密钥对，提供前向保密性（Forward Secrecy）。即使长期私钥泄露，过去的会话仍然安全。

**三方 Diffie-Hellman**：扩展到三方或多方的密钥协商。

**MQV 协议**：结合了密钥协商和隐式认证。

## 历史意义

Diffie-Hellman 的提出标志着现代密码学的开始，开创了公钥密码学的新时代，影响深远：
- 启发了 RSA 等其他公钥加密算法
- 奠定了现代安全通信的基础
- Whitfield Diffie 和 Martin Hellman 因此获得 2015 年图灵奖

## 推荐阅读

- [Diffie–Hellman key exchange - Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [Diffie-Hellman密钥交换协议详解 - CSDN](https://blog.csdn.net/mrpre/article/details/72850769)
- [理解椭圆曲线Diffie-Hellman(ECDH) - 知乎](https://zhuanlan.zhihu.com/p/31153318)

## 相关概念

- **离散对数问题**
- **ECDH**
- **中间人攻击**
- **前向保密**
- **ElGamal加密**
