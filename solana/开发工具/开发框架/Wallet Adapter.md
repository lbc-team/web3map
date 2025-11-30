## Wallet Adapter

Wallet Adapter 是 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 钱包连接的标准库，让 DApp 能够轻松支持多种钱包。

### 核心功能

**统一接口**
一套代码支持所有钱包：
- [Phantom](https://learnblockchain.cn/tags/Phantom?map=Solana)
- Solflare
- Backpack
- Ledger
- 等 20+ 种钱包

**React 集成**
```javascript
import { useWallet } from '@solana/wallet-adapter-react';

function MyComponent() {
  const { publicKey, signTransaction } = useWallet();
  
  return (
    <div>
      {publicKey ? `Connected: ${publicKey}` : 'Not connected'}
    </div>
  );
}
```

**UI 组件**
```javascript
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';

<WalletMultiButton />
```

### 安装使用

```bash
npm install @solana/wallet-adapter-react   @solana/wallet-adapter-react-ui   @solana/wallet-adapter-wallets
```

### 配置钱包

```javascript
import { PhantomWalletAdapter, SolflareWalletAdapter } from '@solana/wallet-adapter-wallets';

const wallets = [
  new PhantomWalletAdapter(),
  new SolflareWalletAdapter(),
];
```

### 功能

- 连接/断开钱包
- 获取公钥
- 签名交易
- 签名消息
- 发送交易

### 最佳实践

**错误处理**
捕获钱包拒绝、网络错误等。

**自动重连**
记住用户选择的钱包。

**移动端适配**
支持 WalletConnect 协议。

### 相关概念

- **WalletConnect**：移动端连接协议
- **DApp**：去中心化应用
- **React**：前端框架
- **[Solana Web3.js](https://solana-labs.github.io/solana-web3.js/)**: [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 的 JavaScript SDK
- **[Anchor](https://www.anchor-lang.com/)**: [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 智能合约框架
- **[Phantom](https://phantom.app/)**: 最流行的 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 钱包
- **[Solflare](https://solflare.com/)**: [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 多链钱包
- **[WalletConnect](https://walletconnect.com/)**: 移动端钱包连接协议


[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) Wallet Adapter 通过提供标准化的钱包集成方案,极大地简化了 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) DApp 的开发。它的模块化设计、多框架支持和丰富的钱包生态,使其成为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 开发者的首选工具。