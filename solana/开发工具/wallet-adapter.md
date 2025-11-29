## Solana Wallet Adapter 概述

[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) Wallet Adapter 是 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 生态系统的官方钱包连接解决方案,为 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) [DApp](https://learnblockchain.cn/tags/DApp) 提供了标准化的钱包集成接口。它支持超过 50 个 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) [钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85),包括 Phantom、Solflare、Ledger 等,通过模块化设计和统一 API,让开发者无需为每个钱包编写特定代码。Wallet Adapter 不仅简化了钱包集成,还提供了自动钱包检测、连接状态管理和错误处理等企业级功能。

**GitHub**: https://github.com/anza-xyz/wallet-adapter

## 核心特性

### 1. 多钱包支持

广泛的钱包生态:

- **浏览器钱包**: Phantom、Solflare、Backpack、Glow
- **移动钱包**: 通过 WalletConnect 支持移动端钱包
- **硬件钱包**: Ledger、Trezor(通过适配器)
- **MPC 钱包**: Coinbase Wallet、Slope
- **自动检测**: 自动检测用户已安装的钱包

### 2. 框架集成

支持主流前端框架:

- **React**: @solana/wallet-adapter-react
- **Vue**: @solana/wallet-adapter-vue
- **Angular**: @solana/wallet-adapter-angular
- **Svelte**: @solana/wallet-adapter-svelte
- **Vanilla JS**: @solana/wallet-adapter-base

### 3. 标准化接口

统一的钱包操作:

- **连接/断开**: connect()、disconnect()
- **签名消息**: signMessage()
- **签名交易**: signTransaction()、signAllTransactions()
- **发送交易**: sendTransaction()
- **公钥获取**: publicKey
- **连接状态**: connected、connecting、disconnecting

### 4. UI 组件

开箱即用的 UI:

- **WalletMultiButton**: 连接按钮和钱包选择器
- **WalletDisconnectButton**: 断开连接按钮
- **WalletIcon**: 钱包图标组件
- **WalletModal**: 钱包选择模态框
- **自定义样式**: 完全可定制的外观

## 快速开始

### 安装

```bash
npm install @solana/wallet-adapter-react \
            @solana/wallet-adapter-react-ui \
            @solana/wallet-adapter-wallets \
            @solana/wallet-adapter-base \
            @solana/web3.js
```

### React 集成

```tsx
import { useMemo } from 'react'
import { ConnectionProvider, WalletProvider } from '@solana/wallet-adapter-react'
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base'
import { PhantomWalletAdapter, SolflareWalletAdapter } from '@solana/wallet-adapter-wallets'
import { WalletModalProvider, WalletMultiButton } from '@solana/wallet-adapter-react-ui'
import { clusterApiUrl } from '@solana/web3.js'

// 默认样式
import '@solana/wallet-adapter-react-ui/styles.css'

function App() {
  const network = WalletAdapterNetwork.Devnet
  const endpoint = useMemo(() => clusterApiUrl(network), [network])

  const wallets = useMemo(
    () => [
      new PhantomWalletAdapter(),
      new SolflareWalletAdapter({ network })
    ],
    [network]
  )

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletModalProvider>
          <WalletMultiButton />
          {/* Your App */}
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  )
}
```

## 核心 Hooks

### 1. useWallet

访问钱包状态和方法:

```tsx
import { useWallet } from '@solana/wallet-adapter-react'

function MyComponent() {
  const {
    publicKey,
    connected,
    connecting,
    disconnecting,
    wallet,
    connect,
    disconnect,
    select,
    signMessage,
    signTransaction,
    sendTransaction
  } = useWallet()

  if (!connected) {
    return <button onClick={connect}>连接钱包</button>
  }

  return (
    <div>
      <p>钱包: {wallet?.adapter.name}</p>
      <p>地址: {publicKey?.toBase58()}</p>
      <button onClick={disconnect}>断开</button>
    </div>
  )
}
```

### 2. useConnection

访问 Solana 连接:

```tsx
import { useConnection, useWallet } from '@solana/wallet-adapter-react'

function Balance() {
  const { connection } = useConnection()
  const { publicKey } = useWallet()
  const [balance, setBalance] = useState(0)

  useEffect(() => {
    if (!publicKey) return

    connection.getBalance(publicKey).then(bal => {
      setBalance(bal / 1e9) // 转换为 SOL
    })
  }, [publicKey, connection])

  return <p>余额: {balance} SOL</p>
}
```

## 交易操作

### 1. 发送交易

使用 sendTransaction:

```tsx
import { useConnection, useWallet } from '@solana/wallet-adapter-react'
import { Transaction, SystemProgram, LAMPORTS_PER_SOL } from '@solana/web3.js'

function SendSOL() {
  const { connection } = useConnection()
  const { publicKey, sendTransaction } = useWallet()

  const handleSend = async () => {
    if (!publicKey) return

    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: publicKey,
        toPubkey: new PublicKey('目标地址'),
        lamports: 0.1 * LAMPORTS_PER_SOL
      })
    )

    const signature = await sendTransaction(transaction, connection)
    await connection.confirmTransaction(signature, 'confirmed')
    console.log('交易成功:', signature)
  }

  return <button onClick={handleSend}>发送 0.1 SOL</button>
}
```

### 2. 签名交易

离线签名后发送:

```tsx
import { useWallet } from '@solana/wallet-adapter-react'

function SignTransaction() {
  const { publicKey, signTransaction } = useWallet()

  const handleSign = async () => {
    if (!publicKey || !signTransaction) return

    const transaction = new Transaction().add(/* 指令 */)
    transaction.feePayer = publicKey
    transaction.recentBlockhash = await connection.getLatestBlockhash()

    const signed = await signTransaction(transaction)
    // 现在可以发送 signed 交易
  }

  return <button onClick={handleSign}>签名交易</button>
}
```

### 3. 签名消息

签名任意消息:

```tsx
import { useWallet } from '@solana/wallet-adapter-react'
import { sign } from 'tweetnacl'

function SignMessage() {
  const { publicKey, signMessage } = useWallet()

  const handleSign = async () => {
    if (!publicKey || !signMessage) return

    const message = new TextEncoder().encode('Hello Solana!')
    const signature = await signMessage(message)

    // 验证签名
    const isValid = sign.detached.verify(
      message,
      signature,
      publicKey.toBytes()
    )
    console.log('签名有效:', isValid)
  }

  return <button onClick={handleSign}>签名消息</button>
}
```

## 自定义配置

### 1. 自定义钱包列表

选择支持的钱包:

```tsx
import { PhantomWalletAdapter, SolflareWalletAdapter, BackpackWalletAdapter } from '@solana/wallet-adapter-wallets'

const wallets = useMemo(
  () => [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter(),
    new BackpackWalletAdapter()
  ],
  []
)
```

### 2. 自定义 RPC 端点

使用自定义节点:

```tsx
const endpoint = useMemo(() => {
  return 'https://your-custom-rpc.com'
}, [])

<ConnectionProvider endpoint={endpoint}>
  {/* ... */}
</ConnectionProvider>
```

### 3. 错误处理

全局错误处理:

```tsx
import { WalletError } from '@solana/wallet-adapter-base'

function App() {
  const onError = useCallback((error: WalletError) => {
    console.error(error)
    // 显示错误通知
  }, [])

  return (
    <WalletProvider wallets={wallets} onError={onError}>
      {/* ... */}
    </WalletProvider>
  )
}
```

### 4. 自定义样式

定制 UI 组件外观:

```tsx
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui'

// 使用自定义 CSS 类
<WalletMultiButton className="my-custom-button" />

// 或者使用 CSS 覆盖默认样式
```

```css
.wallet-adapter-button {
  background-color: #512da8;
  border-radius: 8px;
}

.wallet-adapter-button:hover {
  background-color: #6a3fc0;
}
```

## 高级用法

### 1. 程序派生地址(PDA)

结合 PDA 使用:

```tsx
import { PublicKey } from '@solana/web3.js'
import { useWallet } from '@solana/wallet-adapter-react'

function UsePDA() {
  const { publicKey } = useWallet()

  const getPDA = async () => {
    if (!publicKey) return

    const [pda, bump] = await PublicKey.findProgramAddress(
      [Buffer.from('vault'), publicKey.toBuffer()],
      programId
    )

    console.log('PDA:', pda.toBase58())
  }

  return <button onClick={getPDA}>获取 PDA</button>
}
```

### 2. 与 Anchor 集成

结合 Anchor 框架:

```tsx
import { useAnchorWallet } from '@solana/wallet-adapter-react'
import { Program, AnchorProvider } from '@project-serum/anchor'

function AnchorIntegration() {
  const wallet = useAnchorWallet()
  const { connection } = useConnection()

  const program = useMemo(() => {
    if (!wallet) return null

    const provider = new AnchorProvider(connection, wallet, {})
    return new Program(idl, programId, provider)
  }, [wallet, connection])

  // 使用 program 调用智能合约
}
```

### 3. 多签交易

处理多签名交易:

```tsx
import { useWallet } from '@solana/wallet-adapter-react'

function Multisig() {
  const { signTransaction } = useWallet()

  const handleMultisig = async () => {
    const transaction = new Transaction().add(/* 指令 */)

    // 第一个签名者签名
    const signed = await signTransaction(transaction)

    // 收集其他签名者的签名
    // 然后发送完整签名的交易
  }
}
```

## 最佳实践

### 1. 错误处理

妥善处理钱包错误:

- 用户拒绝连接
- 交易签名被拒绝
- 网络错误
- 钱包未安装
- 余额不足

### 2. 用户体验

优化用户体验:

- 显示加载状态
- 提供清晰的错误提示
- 自动重连机制
- 交易确认提示
- 余额实时更新

### 3. 安全性

确保应用安全:

- 验证交易内容
- 检查交易签名
- 避免钓鱼攻击
- 安全存储敏感数据
- 使用 HTTPS

### 4. 性能优化

提升应用性能:

- 使用 useMemo 缓存钱包实例
- 避免不必要的重渲染
- 合理设置 autoConnect
- 优化 RPC 请求
- 实现请求去重

## 相关概念与技术

- **[Solana Web3.js](https://solana-labs.github.io/solana-web3.js/)**: Solana 的 JavaScript SDK
- **[Anchor](https://www.anchor-lang.com/)**: Solana 智能合约框架
- **[Phantom](https://phantom.app/)**: 最流行的 Solana 钱包
- **[Solflare](https://solflare.com/)**: Solana 多链钱包
- **[WalletConnect](https://walletconnect.com/)**: 移动端钱包连接协议

## 总结

Solana Wallet Adapter 通过提供标准化的钱包集成方案,极大地简化了 Solana DApp 的开发。它的模块化设计、多框架支持和丰富的钱包生态,使其成为 Solana 开发者的首选工具。无论是简单的钱包连接还是复杂的交易签名,Wallet Adapter 都提供了优雅且类型安全的解决方案。随着 Solana 生态的发展,Wallet Adapter 持续完善,为开发者提供更好的开发体验,为用户带来更流畅的使用体验。
