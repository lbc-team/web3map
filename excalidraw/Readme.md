## 图谱制作

在 登链社区上[图谱](https://learnblockchain.cn/maps/Roadmap)  ， 是通过 [excalidraw](https://excalidraw.com/) 制作，excalidraw 是一个开源的制图工具。

登链社区开源了所有的图谱文件，希望可以帮助大家学习的时候有更清晰的路线，也希望对想制作图谱的朋友有所帮助。

## 图谱源文件

本文件夹下都是制图的原始文件：
学习路线图：[Roadmap.excalidraw](./Roadmap.excalidraw)
Web3 图谱：[Web3.excalidraw](./Web3.excalidraw)
BTC 图谱：[BTC.excalidraw](./BTC.excalidraw)
EVM 图谱：[EVM.excalidraw](./EVM.excalidraw)
Solana 图谱：[Solana.excalidraw](./Solana.excalidraw)
Move 图谱：[Move.excalidraw](./Move.excalidraw)
ZKP 图谱：[ZKP.excalidraw](./ZKP.excalidraw)
Web3 开发岗位图：[Job.excalidraw](./Job.excalidraw)
Solidity 图谱：[Solidity.excalidraw](./Solidity.excalidraw)

## 如何参与贡献

欢迎大家参与贡献，你可以修改当前图谱以及创建新的图谱。

我们会根据你的贡献程度发放一些奖励，你可以在[这里](https://github.com/orgs/lbc-team/discussions/14)查看到奖励发放情况。



### 修改图谱

先下载图谱原始文件，然后打开 [excalidraw](https://excalidraw.com/)  按以下方式导入图谱：

![导入](https://img.learnblockchain.cn/pics/20241122184616.png)

之后你就可以按自己的想法修改了。

修改完成后，导出图谱：

![导出图谱](https://img.learnblockchain.cn/pics/20241122185424.png)

用导出图谱的图谱提交 PR 就可以。

### 创建新的图谱

如果你想创建新的图谱，直接用新图谱文件提交 PR 就可以，review 通过后，我们会在登链社区网站上展示。



#### 图谱超链接功能

 excalidraw 作图是可以添加元素的的链接的，登链社区在链接做了一些定制，以便和登链社区的标签百科功能打通。

如果你想做制作一个图谱加入到登链社区中，图谱超链接功能可以选择添加此定制功能（可选），则可实现如下功能：

![](https://img.learnblockchain.cn/pics/20241122214352.png)

当用户点击图谱元素、或者点击文章标签时，都将打开如上图的右侧详情，这样可以和站内其他的相关内容有机的组织在一起。

使用改定制链接很简单，只需要把链接内容按如下使用逗号分割的 3 段式规则填写，例如上图 Solidity 对应的链接内容为：

`Solidity,,https://github.com/lbc-team/web3map/blob/main/eth/开发/Solidity.md`

说明：

1. 第一个`,`前的部分，Solidity 表示对应登链社区网站的标签

2. 第一个`,` 和第二个`,`中间的部分，当前留空，可填一个 URL 链接，若填写会直接跳转到 URL 对应的网址。
3. 第二个`,`后的部分， 对应着百科词条解释的 markdown url，对应着[这个文件](https://github.com/lbc-team/web3map/blob/main/eth/开发/Solidity.md)。







