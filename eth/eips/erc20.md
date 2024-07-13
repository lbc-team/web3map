## ERC20

[ERC20](https://learnblockchain.cn/tags/ERC20?map=EVM) 是 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 区块链上最常用的同质化代币（Token）标准之一。它定义了一组通用接口，使得在 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 区块链上创建和管理代币变得非常简单和标准化。标准的通用接口，让生态应用：包括钱包、交易所和dapp 之前具备了互操作性。使得Token可以轻松地在各种平台上进行交易和使用。

### ERC20 主要接口和事件

```solidity
pragma solidity ^0.8.0;

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}
```



1. **totalSupply**：返回代币的总供给量。
2. **balanceOf**：返回指定地址的代币余额。
3. **transfer**：将指定数量的代币从调用者账户转移到另一个账户。
4. **approve**：允许另一个账户支配指定数量的代币。
5. **transferFrom**：从一个账户转移指定数量的代币到另一个账户（需事先授权 approve）。
6. **allowance**：返回授权账户允许支配的代币数量。



### ERC20 代币合约示例

以下是一个基于 [OpenZeppelin](https://learnblockchain.cn/tags/OpenZeppelin?map=EVM) 代码实现的简单的 [ERC20](https://learnblockchain.cn/tags/ERC20?map=EVM) 代币合约示例：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    constructor() ERC20("MyToken", "MTK") {
        // Initial mint: mint 1000 tokens to the contract deployer
        _mint(msg.sender, 1000 * 10 ** decimals());
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```



上述合约示例展示了如何实现这些接口，开发者可以根据具体需求扩展和修改该合约，构建自己的代币。通过遵循 [ERC20标准](https://eips.ethereum.org/EIPS/eip-20)，可以确保代币在以太坊生态系统中的广泛互操作性和兼容性。

## 知名的 Token

以下是在 [以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM) 区块链上使用 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 标准的一些知名代币：

1. **Tether（[USDT](https://learnblockchain.cn/tags/USDT)）**：Tether 是与美元挂钩的稳定币，在加密货币市场中被广泛用于交易和作为稳定的价值储存。网址：[tether.to](https://tether.to/)
2. **USD Coin（[USDC](https://learnblockchain.cn/tags/USDC)）**：USDC 是另一种与美元挂钩的稳定币，由包括 Circle 和 Coinbase 在内的 Centre 财团管理。**网站**：[centre.io/usdc](https://www.centre.io/usdc)
3. **Chainlink（LINK）**：是一个去中心化的预言机网络，为区块链上的智能合约提供现实世界数据。**网站**：[chain.link](https://chain.link/)
4. **Uniswap（UNI）**：Uniswap 是建立在 [Ethereum](https://learnblockchain.cn/tags/以太坊?map=EVM) 上的去中心化交易（DEX）协议。UNI 代币用于治理和流动性激励。**网站**：[uniswap.org](https://uniswap.org/)
5. **Wrapped Bitcoin（WBTC）**：WBTC 是在 [Ethereum](https://learnblockchain.cn/tags/以太坊?map=EVM) 区块链上代表比特币（BTC）的 ERC-20 代币。每个 WBTC 都以 1:1 的比特币作为支撑。**网站**：[wbtc.network](https://wbtc.network/)
6. **Dai（DAI）**：是一种去中心化的稳定币，与美元软挂钩，并由 MakerDAO 平台上的其他加密货币抵押支持。**网站**：[makerdao.com](https://makerdao.com/)
7. **Aave（[AAVE](https://learnblockchain.cn/tags/AAVE)）**：AAVE 是 Aave 协议的原生代币，是一个去中心化的借贷平台。**网站**：[aave.com](https://aave.com/)
8. **COMP**：COMP 是 [Compound ](https://learnblockchain.cn/tags/Compound)协议的治理代币，是一个允许用户借贷加密货币的去中心化货币市场平台。**网站**：[compound.finance](https://compound.finance/)

