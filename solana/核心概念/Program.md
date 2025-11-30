## 程序 Program

在 Solana 中，程序（Program）相当于其他区块链的智能合约。程序是存储在区块链上的可执行代码，由 eBPF 字节码组成，通过交易中的指令调用执行特定逻辑。

### 程序特性

**无状态**
[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 程序本身不存储状态：
- 程序代码是只读的
- 所有状态存储在独立的账户中
- 程序通过账户参数访问数据

这种设计使程序可以并行执行，提高性能。

**可升级 vs 不可升级**
- **不可升级程序**：部署后代码不可更改，安全但不灵活
- **可升级程序**：可通过升级权限更新代码，灵活但需信任

**Rent-exempt**
程序账户必须达到租金豁免标准，确保永久存在。

### 程序类型

**1. Native Programs**
[Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 内置的系统程序：
- System Program：创建账户、转账
- Token [Program](https://learnblockchain.cn/tags/Program?map=Solana)：[SPL Token](https://learnblockchain.cn/tags/SPL Token?map=Solana) 操作
- Associated Token [Program](https://learnblockchain.cn/tags/Program?map=Solana)：Token 账户管理
- BPF Loader：加载和升级程序

**2. 自定义程序**
开发者编写的程序：
- 使用 [Rust](https://learnblockchain.cn/tags/Rust)、C 编写
- 编译成 eBPF 字节码
- 部署到链上

### 程序开发

**基础结构**
```rust
use solana_program::{
    account_info::AccountInfo,
    entrypoint,
    entrypoint::ProgramResult,
    pubkey::Pubkey,
};

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // 业务逻辑
    Ok(())
}
```

**使用 [Anchor](https://learnblockchain.cn/tags/Anchor?map=Solana) 框架**
```rust
use anchor_lang::prelude::*;

#[program]
pub mod my_program {
    use super::*;
    
    pub fn initialize(ctx: Context<Initialize>, data: u64) -> Result<()> {
        let account = &mut ctx.accounts.my_account;
        account.data = data;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub my_account: Account<'info, MyAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct MyAccount {
    pub data: u64,
}
```

### 程序部署

**1. 编译**
```bash
cargo build-bpf
```

**2. 部署**
```bash
solana program deploy target/deploy/my_program.so
```

**3. 升级**
```bash
solana program upgrade target/deploy/my_program.so <PROGRAM_ID>
```

### 程序账户结构

每个程序有两个关联账户：

**程序账户**
- 存储 eBPF 字节码
- 标记为可执行（executable）
- 所有者是 BPF Loader

**程序数据账户**
- 存储程序代码的实际数据
- 可升级程序独有
- 包含升级权限信息

### 跨程序调用（[CPI](https://learnblockchain.cn/tags/CPI?map=Solana)）

程序可以调用其他程序：

```rust
invoke(
    &instruction,
    &[account1, account2],
)?;

// 或使用 PDA 签名
invoke_signed(
    &instruction,
    &[account1, account2, pda],
    &[&[b"seed", &[bump]]],
)?;
```

**[CPI](https://learnblockchain.cn/tags/CPI?map=Solana) 限制**
- 最大调用深度：4 层
- 继承调用者权限
- 共享 CU 预算

### 程序安全

**常见漏洞**
- 缺少签名者检查
- 账户所有者验证不足
- 整数溢出
- 重入攻击
- [PDA](https://learnblockchain.cn/tags/PDA?map=Solana) 推导验证遗漏

**安全最佳实践**
- 使用 [Anchor](https://learnblockchain.cn/tags/Anchor?map=Solana) 框架的约束检查
- 验证所有输入参数
- 使用安全的数学运算
- 进行审计和测试

### 程序优化

**1. 减少 CU 消耗**
- 优化算法
- 减少账户访问
- 使用 zero-copy

**2. 减小程序大小**
- 移除未使用的依赖
- 使用 LTO（Link Time Optimization）
- 压缩指令

**3. 提高并行性**
- 明确账户读写权限
- 避免不必要的可写账户

### 相关概念

- **eBPF**：程序的字节码格式
- **[Anchor](https://learnblockchain.cn/tags/Anchor?map=Solana)**：流行的 [Solana](https://learnblockchain.cn/tags/Solana?map=Solana) 程序开发框架
- **[CPI](https://learnblockchain.cn/tags/CPI?map=Solana)**：跨程序调用机制
- **[PDA](https://learnblockchain.cn/tags/PDA?map=Solana)**：程序派生地址，程序控制的账户
