## HE

HE (Homomorphic Encryption  同态加密，简称 HE) , 同态加密是一种特殊的加密方法，允许对密文进行处理得到仍然是加密的结果。即对密文直接进行处理，跟对明文进行处理后再对处理结果加密，得到的结果相同。



如果定义一个运算符 `△`，对加密算法 `E` 和 解密算法 `D`，满足：

$$ E(X△Y)=E(X)△E(Y) $$

则意味着对于该运算满足同态性。



同态加密体系大致上被分为四类：部分同态、近似同态、有限级数全同态与完全同态。



### 部分同态加密

部分同态加密（Partially Homomorphic encryption）也叫半同态加密， 它允许人们对密文进行某种特定形式的代数运算（如加法或乘法）得到仍然是加密的结果，将其解密所得到的结果与对明文进行同样的运算结果一样。



- 加法同态：满足 $E(x)E(y) = E(x + y)$  ， 例如椭圆曲线加密算法中，$ E(x)=gx$  具有加法同态性，Pedersen Commit也具有加法同态性。
- 乘法同态：满足 $E(X)E(Y)=E(X*Y)$。典型的例子为：RSA加密算法中，$E(x)=x^e$（其中e为公钥），则$E(x)E(y)=x^ey^e=(xy)^e=E(xy)$，具有乘法同态性。

在加密计算中，加法同态可以完成任何加法运算。乘法同态亦然。



## 近似同态加密

如果我们又想让私密输入相乘，又想得到它们之间的线性组合的话，单纯的部分同态加密算法（RSA，ElGamal）是无法完成的。就可能需要近似同态加密。

近似同态加密可以在密文上同时计算加法与乘法了。但是需要注意的是，近似同态（Somewhat Homomorphic）可以做的加法和乘法次数非常有限，可以计算的函数也在一个有限的范围内。**因为我们不能计算任意逻辑和深度的函数。**

## 有限级数全同态加密

有限级数全同态加密可以对密文进行任意的加法乘法组合了，没有次数的局限性。

但有限级数全同态会引入一个新的复杂度上限 $L$ 的概念，这一复杂度上限约束了函数 $F$ 的复杂度。 

## 全同态加密

全同态加密的系统**没有任何计算方法的限制**，我们可以允许第三方对加密数据执行计算，并获得加密结果，他们可以将其交还给拥有原始数据解密密钥的任何人，而第三方无法自行解密数据或结果。
