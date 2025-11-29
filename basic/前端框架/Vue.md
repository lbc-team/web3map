## Vue.js 概述

Vue.js 是一个用于构建用户界面的渐进式 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 框架,由尤雨溪于 2014 年创建。Vue 以其简洁的语法、灵活的架构和优秀的性能成为最受欢迎的前端框架之一。通过响应式数据绑定和组件系统,Vue 让开发者能够高效地构建从简单到复杂的 Web 应用,在 Web3 开发中也被广泛采用。

**官方网站**: https://vuejs.org/

## 核心特性

### 1. 响应式系统

Vue 的核心机制:

- **数据劫持**: 通过 Proxy 拦截数据访问
- **自动更新**: 数据变化自动更新视图
- **依赖收集**: 智能追踪数据依赖
- **批量更新**: 异步批量更新 DOM
- **细粒度响应**: 组件级别的精确更新

### 2. 组件系统

可复用的构建块:

- **单文件组件**: .vue 文件封装逻辑、模板和样式
- **Props 传递**: 父子组件通信
- **事件发送**: 子组件向父组件通信
- **插槽**: 灵活的内容分发
- **组合式 API**: Vue 3 新的组合方式

### 3. 模板语法

声明式渲染:

- **插值**: {{ message }}
- **指令**: v-bind、v-if、v-for、v-on
- **修饰符**: .prevent、.stop、.once
- **缩写**: : 代替 v-bind,@ 代替 v-on
- **动态参数**: v-bind:[key]

### 4. 虚拟 DOM

性能优化:

- **虚拟节点**: 轻量级的 DOM 表示
- **Diff 算法**: 高效的差异比较
- **批量更新**: 减少 DOM 操作
- **编译优化**: Vue 3 编译时优化
- **Tree-shaking**: 更小的打包体积

## Vue 3 新特性

### Composition API

新的组合方式:

```vue
<script setup>
import { ref, computed, onMounted } from 'vue'

// 响应式数据
const count = ref(0)
const doubled = computed(() => count.value * 2)

// 方法
function increment() {
  count.value++
}

// 生命周期
onMounted(() => {
  console.log('组件已挂载')
})
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Doubled: {{ doubled }}</p>
    <button @click="increment">增加</button>
  </div>
</template>
```

### Teleport

传送组件:

```vue
<teleport to="body">
  <div class="modal">
    <!-- 渲染到 body 标签 -->
  </div>
</teleport>
```

### Suspense

异步组件:

```vue
<Suspense>
  <template #default>
    <AsyncComponent />
  </template>
  <template #fallback>
    <div>加载中...</div>
  </template>
</Suspense>
```

## Web3 开发

### Vue + Wagmi

使用 Vue 开发 Web3 应用:

```bash
# 创建 Vue 项目
npm create vue@latest my-web3-app
cd my-web3-app

# 安装 Web3 依赖
npm install @wagmi/vue @wagmi/core viem
```

### 钱包连接

```vue
<script setup>
import { useConnect, useAccount, useDisconnect } from '@wagmi/vue'
import { injected } from '@wagmi/connectors'

const { connect } = useConnect()
const { address, isConnected } = useAccount()
const { disconnect } = useDisconnect()

function handleConnect() {
  connect({ connector: injected() })
}
</script>

<template>
  <div>
    <button v-if="!isConnected" @click="handleConnect">
      连接钱包
    </button>
    <div v-else>
      <p>地址: {{ address }}</p>
      <button @click="disconnect">断开</button>
    </div>
  </div>
</template>
```

### 读取合约

```vue
<script setup>
import { useReadContract } from '@wagmi/vue'
import { erc20Abi } from 'viem'

const { data: balance } = useReadContract({
  address: '0x...',
  abi: erc20Abi,
  functionName: 'balanceOf',
  args: ['0xUserAddress']
})
</script>

<template>
  <div>
    <p>余额: {{ balance }}</p>
  </div>
</template>
```

### 发送交易

```vue
<script setup>
import { useWriteContract, useWaitForTransactionReceipt } from '@wagmi/vue'
import { erc20Abi, parseUnits } from 'viem'

const { data: hash, writeContract } = useWriteContract()
const { isLoading, isSuccess } = useWaitForTransactionReceipt({
  hash
})

function transfer() {
  writeContract({
    address: '0x...',
    abi: erc20Abi,
    functionName: 'transfer',
    args: ['0xRecipient', parseUnits('1', 18)]
  })
}
</script>

<template>
  <div>
    <button @click="transfer" :disabled="isLoading">
      {{ isLoading ? '发送中...' : '发送代币' }}
    </button>
    <p v-if="isSuccess">发送成功!</p>
  </div>
</template>
```

## 生态系统

### 核心库

- **Vue Router**: 官方路由管理器
- **Pinia**: 新一代状态管理(替代 Vuex)
- **Vue Devtools**: 开发者工具
- **Vite**: 极速构建工具
- **Vitest**: 测试框架

### UI 框架

- **Element Plus**: 企业级 UI 组件库
- **Vuetify**: Material Design 组件
- **Ant Design Vue**: Ant Design 的 Vue 版本
- **Naive UI**: 现代化组件库
- **Quasar**: 全平台框架

### Web3 工具

- **@wagmi/vue**: Vue 的 Wagmi 集成
- **vue-dapp**: Vue Web3 工具集
- **ethers-vue**: Ethers.js Vue 封装
- **web3modal**: 钱包连接 UI

## Nuxt.js

Vue 的全栈框架:

### 创建 Nuxt 项目

```bash
npx nuxi@latest init my-nuxt-app
cd my-nuxt-app
npm install
npm run dev
```

### 服务端渲染

```vue
<!-- pages/index.vue -->
<script setup>
const { data: posts } = await useFetch('/api/posts')
</script>

<template>
  <div>
    <h1>文章列表</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        {{ post.title }}
      </li>
    </ul>
  </div>
</template>
```

### API Routes

```typescript
// server/api/posts.ts
export default defineEventHandler(async (event) => {
  const posts = await fetchPosts()
  return posts
})
```

## 最佳实践

### 1. 组件设计

- 单一职责原则
- Props 类型验证
- 合理使用插槽
- 避免过深嵌套
- 复用公共逻辑

### 2. 性能优化

```vue
<script setup>
import { computed, watch } from 'vue'

// 使用 computed 缓存计算结果
const filteredList = computed(() => {
  return list.value.filter(item => item.active)
})

// 使用 watchEffect 自动追踪依赖
watchEffect(() => {
  console.log(count.value)
})
</script>

<template>
  <!-- 使用 v-once 只渲染一次 -->
  <div v-once>{{ staticContent }}</div>

  <!-- 使用 key 优化列表渲染 -->
  <div v-for="item in items" :key="item.id">
    {{ item.name }}
  </div>
</template>
```

### 3. 状态管理

使用 Pinia:

```typescript
// stores/counter.ts
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),

  getters: {
    doubled: (state) => state.count * 2
  },

  actions: {
    increment() {
      this.count++
    }
  }
})
```

### 4. TypeScript 支持

```vue
<script setup lang="ts">
interface Props {
  title: string
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})

const emit = defineEmits<{
  update: [value: number]
  delete: [id: string]
}>()
</script>
```

## 相关概念与技术

- **[React](https://react.dev/)**: Facebook 开发的 UI 库
- **[Svelte](https://svelte.dev/)**: 编译时框架
- **[Angular](https://angular.io/)**: Google 开发的全栈框架
- **[Vite](https://vitejs.dev/)**: 下一代前端构建工具
- **[Pinia](https://pinia.vuejs.org/)**: Vue 状态管理库

## 总结

Vue.js 以其渐进式设计理念、优雅的 API 和强大的生态系统,成为前端开发的热门选择。Vue 3 的 Composition API 和性能优化使其更加强大和灵活。在 Web3 开发中,Vue 通过 @wagmi/vue 等工具也能提供出色的开发体验。无论是构建传统 Web 应用还是去中心化应用,Vue 都能提供高效、优雅的解决方案。
