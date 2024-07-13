## Foundry 简介

[Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM) 是一种用于以太坊智能合约开发的先进工具集。它由 Paradigm 开发，是一个快速、便捷和高效的智能合约开发框架，提供了编译、测试、调试和部署合约的完整工具链。Foundry 的设计目标是提高开发效率简化 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 智能合约的开发流程。

### Foundry 的主要组件

1. **Forge**：
   - Forge 是 Foundry 的核心命令行工具，用于编译、测试和部署智能合约。
   - 主要功能包括：
     - 编译：`forge build` 命令编译智能合约。
     - 测试：`forge test` 命令运行测试，支持快速和高效的单元测试。
     - 部署：`forge create` 命令用于将合约部署到区块链上。
2. **Cast**：
   - Cast 是 Foundry 的另一重要工具，提供了与以太坊网络进行交互的命令行界面。
   - 功能包括发送交易、查询链上数据、调用智能合约等。例如，`cast send` 命令用于发送交易，`cast call` 命令用于调用合约方法。
3. **Anvil**：一个高性能的本地测试网络，用于模拟以太坊区块链环境。它提供了快速的交易确认和丰富的测试功能，便于开发和调试。
   
4. **Chisel**: 一个先进的Solidity REPL。它可以用来快速测试在本地或 fork 网络上的 Solidity 片段的行为。

### 使用 Foundry 的示例

以下是使用 Foundry 编写、测试和部署智能合约的基本步骤：

1. **安装 Foundry**：
   - 通过以下命令安装 Foundry：
     ```sh
     curl -L https://foundry.paradigm.xyz | bash
     foundryup
     ```

2. **初始化项目**：
   - 使用 `forge init` 命令初始化一个新的智能合约项目：
     ```sh
     forge init my-foundry-project
     cd my-foundry-project
     ```

3. **编写智能合约**：
   - 在 `src` 目录下编写你的智能合约，例如 `HelloWorld.sol`：
     ```solidity
     // SPDX-License-Identifier: MIT
     pragma solidity ^0.8.0;
     
     contract HelloWorld {
         string public message;
     
         constructor(string memory _message) {
             message = _message;
         }
     
         function setMessage(string memory _message) public {
             message = _message;
         }
     }
     ```

4. **编译合约**：
   - 使用 `forge build` 命令编译合约：
     ```sh
     forge build
     ```

5. **测试合约**：
   - 在 `test` 目录下编写测试文件，例如 `HelloWorld.t.sol`：
     ```solidity
     // SPDX-License-Identifier: MIT
     pragma solidity ^0.8.0;
     
     import "forge-std/Test.sol";
     import "../src/HelloWorld.sol";
     
     contract HelloWorldTest is Test {
         HelloWorld hello;
     
         function setUp() public {
             hello = new HelloWorld("Hello, Foundry!");
         }
     
         function testInitialMessage() public {
             assertEq(hello.message(), "Hello, Foundry!");
         }
     
         function testSetMessage() public {
             hello.setMessage("Hello, Ethereum!");
             assertEq(hello.message(), "Hello, Ethereum!");
         }
     }
     ```

6. **运行测试**：
   - 使用 `forge test` 命令运行测试：
     ```sh
     forge test
     ```

7. **合约部署**

   Forge 提供 create 命令和 script  两个方式部署：

   `create` 命令部署合约，方法如下：

   ```
   forge create  src/HelloWorld.sol:HelloWorld --constructor-args "Hello" --rpc-url <RPC_URL>  --private-key $PRIVATE_KEY
   ```

   复杂一些的合约，更多的使用 script， 在 `scripts` 目录下创建一个新的部署脚本，例如 `DeployHelloWorld.s.sol`：

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.0;
   
   import "forge-std/Script.sol";
   import "../src/HelloWorld.sol";
   
   contract DeployHelloWorld is Script {
       function run() external {
           vm.startBroadcast();
   
           new HelloWorld("Hello, Foundry!");
   
           vm.stopBroadcast();
       }
   }
   ```

   在这个脚本中，`vm.startBroadcast()` 和 `vm.stopBroadcast()` 用于指示在区块链上广播交易。`new HelloWorld("Hello, Foundry!");` 是部署合约的命令。

   ```
   forge script scripts/DeployHelloWorld.s.sol --rpc-url <RPC_URL> --private-key $PRIVATE_KEY --broadcast
   ```

   


## 更多

1. DeCert.me Foundry 开发教程： https://decert.me/tutorial/solidity/tools/foundry

2. Foundry 文档： 英文： https://book.getfoundry.sh/  中文：https://learnblockchain.cn/docs/foundry/i18n/zh/

   