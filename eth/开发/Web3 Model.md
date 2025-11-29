## Reown SDK (Web3Modal) 概述

Reown SDK(前身为 Web3Modal)是由 WalletConnect 团队开发的钱包连接 UI 库,为 Web3 应用提供了美观、易用的钱包连接界面。通过单一 SDK 支持 300+ [钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85),包括浏览器钱包、移动钱包和硬件钱包,Reown 大幅简化了多钱包集成的复杂度。作为 WalletConnect 生态的核心组件,Reown SDK 已被数千个 [DApp](https://learnblockchain.cn/tags/DApp) 采用,是 Web3 钱包连接的标准解决方案。

**官方网站**: https://reown.com/

**注**: Web3Modal 于 2024 年品牌升级为 Reown SDK,核心功能保持一致。

## 核心特性

### 1. 多钱包支持

广泛的钱包生态:

- **300+ [钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)**: 支持主流和长尾钱包
- **自动检测**: 检测用户已安装的钱包
- **WalletConnect**: 通过扫码连接移动钱包
- **钱包推荐**: 智能推荐合适的钱包
- **自定义列表**: 配置显示的钱包

### 2. 多链支持

跨链钱包连接:

- **Ethereum**: 以太坊及其 Layer 2
- **[Solana](https://learnblockchain.cn/tags/Solana?map=Solana)**: [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 生态
- **Cosmos**: Cosmos 生态链
- **Polkadot**: Polkadot 生态
- **其他链**: 持续增加新链支持

### 3. 美观的 UI

现代化设计:

- **响应式**: 适配移动端和桌面端
- **深色模式**: 内置深浅色主题
- **可定制**: 自定义品牌颜色和样式
- **多语言**: 支持国际化
- **流畅动画**: 优雅的交互动画

### 4. 完整功能

一站式解决方案:

- **账户管理**: 显示账户信息和余额
- **网络切换**: 便捷的网络切换 UI
- **交易历史**: 查看最近交易
- **断开连接**: 清晰的断开流程
- **错误处理**: 友好的错误提示

## 快速开始

### 安装

```bash
# 安装 Reown SDK (AppKit)
npm install @reown/appkit @reown/appkit-adapter-wagmi wagmi viem
```

### React 集成

使用 Wagmi 适配器:

```tsx
import { createAppKit } from '@reown/appkit/react'
import { WagmiProvider } from 'wagmi'
import { arbitrum, mainnet } from '@reown/appkit/networks'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'

// 1. 获取 projectId
const projectId = 'YOUR_PROJECT_ID'

// 2. 创建 wagmiAdapter
const wagmiAdapter = new WagmiAdapter({
  networks: [mainnet, arbitrum],
  projectId
})

// 3. 创建 modal
createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet, arbitrum],
  projectId,
  metadata: {
    name: 'My App',
    description: 'My App description',
    url: 'https://myapp.com',
    icons: ['https://myapp.com/icon.png']
  }
})

const queryClient = new QueryClient()

function App() {
  return (
    <WagmiProvider config={wagmiAdapter.wagmiConfig}>
      <QueryClientProvider client={queryClient}>
        {/* Your App */}
        <w3m-button />
      </QueryClientProvider>
    </WagmiProvider>
  )
}
```

### Vue 集成

```typescript
import { createAppKit } from '@reown/appkit/vue'
import { mainnet, arbitrum } from '@reown/appkit/networks'
import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'

const projectId = 'YOUR_PROJECT_ID'

const wagmiAdapter = new WagmiAdapter({
  networks: [mainnet, arbitrum],
  projectId
})

createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet, arbitrum],
  projectId,
  metadata: {
    name: 'My App',
    description: 'My App description',
    url: 'https://myapp.com',
    icons: ['https://myapp.com/icon.png']
  }
})
```

### 使用按钮组件

```tsx
// 默认连接按钮
<w3m-button />

// 账户按钮
<w3m-account-button />

// 网络按钮
<w3m-network-button />
```

## 自定义配置

### 主题定制

```typescript
createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet],
  projectId,
  themeMode: 'dark', // 'light' | 'dark'
  themeVariables: {
    '--w3m-accent': '#7b3ff2',
    '--w3m-border-radius-master': '2px'
  }
})
```

### 功能配置

```typescript
createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet],
  projectId,
  features: {
    analytics: true, // 启用分析
    email: true, // 启用邮箱登录
    socials: ['google', 'github'], // 社交登录
    emailShowWallets: true // 显示钱包选项
  }
})
```

### 钱包配置

```typescript
createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet],
  projectId,
  featuredWalletIds: [
    'wallet-id-1',
    'wallet-id-2'
  ],
  includeWalletIds: ['metamask', 'rainbow'],
  excludeWalletIds: ['wallet-to-exclude']
})
```

## 高级功能

### 编程控制

```typescript
import { useAppKit } from '@reown/appkit/react'

function MyComponent() {
  const { open, close } = useAppKit()

  return (
    <>
      <button onClick={() => open()}>打开模态框</button>
      <button onClick={() => open({ view: 'Networks' })}>
        选择网络
      </button>
    </>
  )
}
```

### 事件监听

```typescript
import { useAppKitEvents } from '@reown/appkit/react'

function MyComponent() {
  const events = useAppKitEvents()

  // 监听连接事件
  useEffect(() => {
    const handleConnect = () => {
      console.log('钱包已连接')
    }

    // 订阅事件
    return () => {
      // 清理
    }
  }, [events])
}
```

### 自定义钱包

```typescript
createAppKit({
  adapters: [wagmiAdapter],
  networks: [mainnet],
  projectId,
  customWallets: [
    {
      id: 'myWallet',
      name: 'My Custom Wallet',
      homepage: 'https://mywallet.com',
      image_url: 'https://mywallet.com/icon.png',
      mobile_link: 'mywallet://',
      desktop_link: 'https://mywallet.com/download'
    }
  ]
})
```

## Solana 支持

### Solana 适配器

```typescript
import { createAppKit } from '@reown/appkit/react'
import { SolanaAdapter } from '@reown/appkit-adapter-solana/react'
import { solana, solanaTestnet } from '@reown/appkit/networks'
import { PhantomWalletAdapter, SolflareWalletAdapter } from '@solana/wallet-adapter-wallets'

const solanaAdapter = new SolanaAdapter({
  wallets: [new PhantomWalletAdapter(), new SolflareWalletAdapter()]
})

createAppKit({
  adapters: [solanaAdapter],
  networks: [solana, solanaTestnet],
  projectId,
  metadata: {
    name: 'My [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) App',
    description: 'My Solana [DApp](https://learnblockchain.cn/tags/DApp)',
    url: 'https://myapp.com',
    icons: ['https://myapp.com/icon.png']
  }
})
```

## 最佳实践

### 1. 用户体验

- 显示清晰的连接状态
- 提供友好的错误提示
- 支持多种连接方式
- 优化移动端体验
- 实现自动重连

### 2. 性能优化

- 按需加载钱包列表
- 缓存钱包连接状态
- 优化图片资源
- 减少不必要的重渲染
- 使用代码分割

### 3. 安全建议

- 验证钱包连接状态
- 检查网络 ID
- 实现签名验证
- 处理断开连接
- 保护敏感操作

## 与其他方案对比

|特性|Reown SDK|RainbowKit|ConnectKit|
|---|---|---|---|
|钱包数量|300+|100+|50+|
|多链支持|是|仅 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM)|仅 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM)|
|UI 质量|优秀|优秀|良好|
|定制化|高|高|中|
|邮箱登录|支持|不支持|不支持|
|社交登录|支持|不支持|不支持|

## 迁移指南

### 从 Web3Modal v2 迁移

```typescript
// 旧版 Web3Modal v2
import { Web3Modal } from '@web3modal/html'

// 新版 Reown SDK
import { createAppKit } from '@reown/appkit/react'

// 配置基本相同,部分 API 有调整
```

## 相关概念与技术

- **[WalletConnect](https://walletconnect.com/)**: Reown 的底层协议
- **[RainbowKit](https://www.rainbowkit.com/)**: 另一个钱包连接 UI 库
- **[Wagmi](https://wagmi.sh/)**: React Hooks for Ethereum
- **[Web3.js](https://web3js.org/)**: 以太坊 JavaScript API
- **[Ethers.js](https://docs.ethers.org/)**: 以太坊库

## 总结

Reown SDK(Web3Modal)通过提供美观的 UI 和强大的功能,成为 Web3 应用钱包连接的首选方案。其支持 300+ 钱包、多链兼容和丰富的定制选项,使开发者能够轻松为用户提供一流的钱包连接体验。随着品牌升级到 Reown,SDK 将继续演进,为 Web3 生态提供更好的基础设施支持。无论是以太坊、Solana 还是其他区块链的 DApp,Reown SDK 都是值得信赖的选择。
