## Wagmi 概述

Wagmi 是一个为 React 应用设计的以太坊开发 Hooks 库,提供了 20 多个 Hooks 来处理账户连接、合约交互、交易发送、ENS 解析等常见需求。基于 [Viem](https://learnblockchain.cn/tags/Viem?map=EVM) 构建,Wagmi 以其类型安全、高性能和模块化设计成为 React Web3 开发的首选库。它不仅简化了区块链交互的复杂性,还提供了缓存、请求去重、多链支持等企业级特性。

**官方网站**: https://wagmi.sh/

## 核心特性

### 1. 丰富的 Hooks

全面的功能覆盖:

- **账户管理**: useAccount、useConnect、useDisconnect、useSwitchAccount
- **网络管理**: useChainId、useSwitchChain、useChains
- **余额查询**: useBalance、useToken
- **合约交互**: useReadContract、useWriteContract、useWatchContractEvent
- **交易操作**: useSendTransaction、useWaitForTransactionReceipt
- **ENS 支持**: useEnsName、useEnsAddress、useEnsAvatar
- **签名功能**: useSignMessage、useSignTypedData

### 2. 类型安全

完整的 TypeScript 支持:

- **自动类型推断**: 根据 [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 自动推断函数参数和返回类型
- **编译时检查**: 在编译阶段发现类型错误
- **智能提示**: IDE 自动完成和参数提示
- **类型保护**: 确保运行时类型安全
- **泛型支持**: 支持泛型合约和自定义类型

### 3. 查询缓存

基于 TanStack Query:

- **自动缓存**: 智能缓存查询结果
- **请求去重**: 相同请求自动合并
- **后台更新**: 自动在后台刷新过期数据
- **乐观更新**: 支持乐观 UI 更新
- **缓存持久化**: 可选的本地存储持久化

### 4. 多链支持

跨链开发简化:

- **链配置**: 预定义主流区块链配置
- **动态切换**: 用户一键切换网络
- **多链状态**: 同时管理多个链的状态
- **自定义链**: 轻松添加自定义网络
- **测试网**: 内置测试网络支持

## 快速开始

### 安装

```bash
npm install wagmi viem@2.x @tanstack/react-query
```

### 基础配置

```tsx
import { WagmiProvider, createConfig, http } from 'wagmi'
import { mainnet, sepolia } from 'wagmi/chains'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

// 创建配置
const config = createConfig({
  chains: [mainnet, sepolia],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http()
  }
})

const queryClient = new QueryClient()

function App() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        {/* Your App */}
      </QueryClientProvider>
    </WagmiProvider>
  )
}
```

### 连接钱包

```tsx
import { useConnect, useAccount, useDisconnect } from 'wagmi'
import { injected } from 'wagmi/connectors'

function Connect() {
  const { connect } = useConnect()
  const { address, isConnected } = useAccount()
  const { disconnect } = useDisconnect()

  if (isConnected) {
    return (
      <div>
        <p>已连接: {address}</p>
        <button onClick={() => disconnect()}>断开</button>
      </div>
    )
  }

  return (
    <button onClick={() => connect({ connector: injected() })}>
      连接 MetaMask
    </button>
  )
}
```

## 常用 Hooks

### 1. 账户和网络

获取账户和网络信息:

```tsx
import { useAccount, useChainId, useBalance } from 'wagmi'

function Account() {
  const { address, isConnected, connector } = useAccount()
  const chainId = useChainId()
  const { data: balance } = useBalance({ address })

  return (
    <div>
      <p>地址: {address}</p>
      <p>链 ID: {chainId}</p>
      <p>余额: {balance?.formatted} {balance?.symbol}</p>
      <p>连接器: {connector?.name}</p>
    </div>
  )
}
```

### 2. 读取合约

读取智能合约数据:

```tsx
import { useReadContract } from 'wagmi'
import { erc20Abi } from 'viem'

function TokenBalance({ address, tokenAddress }) {
  const { data: balance } = useReadContract({
    address: tokenAddress,
    abi: erc20Abi,
    functionName: 'balanceOf',
    args: [address]
  })

  return <p>代币余额: {balance?.toString()}</p>
}
```

### 3. 写入合约

执行合约写入操作:

```tsx
import { useWriteContract, useWaitForTransactionReceipt } from 'wagmi'
import { erc20Abi, parseUnits } from 'viem'

function Transfer() {
  const { data: hash, writeContract } = useWriteContract()

  const { isLoading, isSuccess } = useWaitForTransactionReceipt({
    hash
  })

  const handleTransfer = () => {
    writeContract({
      address: '0x...',
      abi: erc20Abi,
      functionName: 'transfer',
      args: ['0xRecipient...', parseUnits('1', 18)]
    })
  }

  return (
    <div>
      <button onClick={handleTransfer} disabled={isLoading}>
        {isLoading ? '发送中...' : '发送代币'}
      </button>
      {isSuccess && <p>交易成功!</p>}
    </div>
  )
}
```

### 4. 监听事件

监听合约事件:

```tsx
import { useWatchContractEvent } from 'wagmi'
import { erc20Abi } from 'viem'

function TransferListener() {
  useWatchContractEvent({
    address: '0x...',
    abi: erc20Abi,
    eventName: 'Transfer',
    onLogs(logs) {
      console.log('收到 Transfer 事件:', logs)
    }
  })

  return <p>监听 Transfer 事件中...</p>
}
```

### 5. 发送交易

发送 ETH 交易:

```tsx
import { useSendTransaction, useWaitForTransactionReceipt } from 'wagmi'
import { parseEther } from 'viem'

function SendETH() {
  const { data: hash, sendTransaction } = useSendTransaction()
  const { isLoading, isSuccess } = useWaitForTransactionReceipt({ hash })

  const handleSend = () => {
    sendTransaction({
      to: '0xRecipient...',
      value: parseEther('0.01')
    })
  }

  return (
    <div>
      <button onClick={handleSend} disabled={isLoading}>
        发送 0.01 ETH
      </button>
      {isSuccess && <p>发送成功!</p>}
    </div>
  )
}
```

### 6. ENS 解析

使用 ENS 域名:

```tsx
import { useEnsName, useEnsAddress, useEnsAvatar } from 'wagmi'

function ENSProfile({ address }) {
  const { data: ensName } = useEnsName({ address })
  const { data: avatar } = useEnsAvatar({ name: ensName })

  return (
    <div>
      {avatar && <img src={avatar} alt="ENS Avatar" />}
      <p>{ensName ?? address}</p>
    </div>
  )
}
```

## 高级功能

### 1. 多链配置

支持多个区块链:

```tsx
import { createConfig, http } from 'wagmi'
import { mainnet, polygon, arbitrum, optimism } from 'wagmi/chains'

const config = createConfig({
  chains: [mainnet, polygon, arbitrum, optimism],
  transports: {
    [mainnet.id]: http('https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY'),
    [polygon.id]: http('https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY'),
    [arbitrum.id]: http(),
    [optimism.id]: http()
  }
})
```

### 2. 连接器配置

配置多种钱包连接方式:

```tsx
import { createConfig, http } from 'wagmi'
import { injected, walletConnect, coinbaseWallet } from 'wagmi/connectors'

const config = createConfig({
  chains: [mainnet],
  connectors: [
    injected(),
    walletConnect({ projectId: 'YOUR_PROJECT_ID' }),
    coinbaseWallet({ appName: 'My App' })
  ],
  transports: {
    [mainnet.id]: http()
  }
})
```

### 3. 批量请求

Multicall 批量查询:

```tsx
import { useReadContracts } from 'wagmi'
import { erc20Abi } from 'viem'

function BatchRead() {
  const { data } = useReadContracts({
    contracts: [
      {
        address: '0xToken1',
        abi: erc20Abi,
        functionName: 'balanceOf',
        args: ['0xUser']
      },
      {
        address: '0xToken2',
        abi: erc20Abi,
        functionName: 'balanceOf',
        args: ['0xUser']
      }
    ]
  })

  return (
    <div>
      <p>Token1: {data?.[0].result?.toString()}</p>
      <p>Token2: {data?.[1].result?.toString()}</p>
    </div>
  )
}
```

### 4. 自定义 Hook

创建自定义 Hook:

```tsx
import { useReadContract } from 'wagmi'
import { erc20Abi } from 'viem'

function useTokenBalance(address, tokenAddress) {
  const { data: balance, isLoading } = useReadContract({
    address: tokenAddress,
    abi: erc20Abi,
    functionName: 'balanceOf',
    args: [address],
    watch: true // 自动刷新
  })

  return {
    balance: balance?.toString(),
    isLoading
  }
}
```

## 最佳实践

### 1. 错误处理

完善的错误处理:

```tsx
import { useWriteContract } from 'wagmi'

function Transfer() {
  const { writeContract, error, isError } = useWriteContract()

  if (isError) {
    return <p>错误: {error.message}</p>
  }

  // ...
}
```

### 2. 加载状态

优雅的加载状态管理:

```tsx
import { useReadContract } from 'wagmi'

function Data() {
  const { data, isLoading, isError, error } = useReadContract({
    // ...
  })

  if (isLoading) return <p>加载中...</p>
  if (isError) return <p>错误: {error.message}</p>

  return <p>数据: {data}</p>
}
```

### 3. 性能优化

优化渲染性能:

- 合理使用缓存时间和刷新间隔
- 避免不必要的 Hook 调用
- 使用 React.memo 优化组件
- 合理使用 watch 参数自动更新

### 4. 类型安全

充分利用 TypeScript:

```tsx
import { useReadContract } from 'wagmi'
import { Abi } from 'viem'

const myAbi = [...] as const // 使用 as const 保留字面类型

function MyComponent() {
  const { data } = useReadContract({
    abi: myAbi,
    functionName: 'myFunction', // 类型安全的函数名
    args: [...] // 自动推断参数类型
  })
  // data 的类型被自动推断
}
```

## 生态系统

### 官方工具

- **Wagmi CLI**: 从 [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 生成 React Hooks
- **[Viem](https://learnblockchain.cn/tags/Viem?map=EVM)**: 底层以太坊库
- **TanStack Query**: 数据获取和缓存
- **Wagmi Dev Tools**: 开发调试工具

### 集成方案

- **RainbowKit**: UI 组件库
- **ConnectKit**: 另一个 UI 方案
- **Web3Modal**: 钱包连接 UI
- **Dynamic**: 钱包和认证解决方案

## 相关概念与技术

- **[Viem](https://viem.sh/)**: Wagmi 的底层库,提供类型安全的以太坊交互
- **[RainbowKit](https://www.rainbowkit.com/)**: 基于 Wagmi 的钱包连接 UI 库
- **[TanStack Query](https://tanstack.com/query)**: React 数据获取和状态管理库
- **[Ethers.js](https://docs.ethers.org/)**: 另一个以太坊 JavaScript 库
- **[Web3.js](https://web3js.readthedocs.io/)**: 经典的以太坊 JavaScript 库

## 总结

Wagmi 通过提供类型安全、高性能的 React Hooks,极大地简化了以太坊 [DApp](https://learnblockchain.cn/tags/DApp) 开发。它的模块化设计、强大的缓存机制和完善的 TypeScript 支持,使其成为 React Web3 开发的事实标准。无论是简单的钱包连接还是复杂的 [DeFi](https://learnblockchain.cn/tags/DeFi?map=EVM) 协议交互,Wagmi 都能提供优雅的解决方案。结合 RainbowKit 等 UI 库,开发者可以快速构建出用户体验出色的 Web3 应用。
