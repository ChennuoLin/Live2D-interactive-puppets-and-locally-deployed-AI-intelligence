# 使用Pygame在python环境下生成Live2d可动人偶的互动与连接Ollama的本地部署


## 简介
> **项目内容**：基于OpenGL开发的Pygame框架，使用Live2d可动式人偶动画通过“**区域点击式交互**”进行互动，与接入Ollama AI的本地部署实现用户与人偶之间的语音交互。
>  
> **项目背景**：纯属兴趣爱好
> 
> **涉及内容**：Python Pygame OpenGL Ollama transformers
> 
> **成果**：本项目使用了Live2d官网的 “Hatsune Miku” 的开源模型，实现了基础的AI与用户之间的交流，和模型与用户的互动。

## 项目结构
```
main.py {

  Live2d_conture.py {
  
    涉及调用 [miku文件夹] {
      miku/runtime/motions/[ALL json File] 
    } 
  
  }

  py_voice.py {
  
    涉及调用 [voice文件夹]{
      voice/[ALL MP3 File]
    }
  }

}
```

## 项目引用
**项目部分代码来源**：
本项目主要用到《pygame里live2d的使用方法（live2d-py）》中关于 “live2d-py库的使用方法” 等

来源于CSDN:

作者：[Daisy-Mo](https://blog.csdn.net/2303_79350799/article/details/146988648?fromshare=blogdetail&sharetype=blogdetail&sharerId=146988648&sharerefer=PC&sharesource=weixin_48622385&sharefrom=from_link)

文章网址：https://blog.csdn.net/2303_79350799/article/details/146988648?fromshare=blogdetail&sharetype=blogdetail&sharerId=146988648&sharerefer=PC&sharesource=weixin_48622385&sharefrom=from_link

**项目模型来源**：

模型名称：Hatsune Miku

模型网址：https://www.live2d.com/en/learn/sample/

## 项目说明

### main.py
目的：整合 [语音输入与AI反馈模块] 和 [Live2d显示及触控模块]

主要内容：通过使用python模块（threading）让Live2d_conture.py和py_voice.py同时进行实现在Live2d显示窗口不被单线程占用


### Live2d_conture.py
内容：使用 [《pygame里live2d的使用方法（live2d-py）》](https://blog.csdn.net/2303_79350799/article/details/146988648?fromshare=blogdetail&sharetype=blogdetail&sharerId=146988648&sharerefer=PC&sharesource=weixin_48622385&sharefrom=from_link)
中Live2d的模块导入和实例，在此基础上进行修改。

实例（v3）修改内容：

  - 在 while 循环中添加了使用if判断从touch_area字典中的区域值，用于用户与模型之间的互动
  - 在项目启动之前添加初始动画，并播放 动作[Idel.json] 和 声音[voice/Hi.mp3]
  - Live2d的模型替换（.\v3\Mao\Mao.model3.json -> .\miku\runtime\miku.model3.json）
  - 删除了V3项目中的背景


### py_voice.py
内容：使用语音进行输入并结合提示词输入给Ollama本地AI并获得返回答案

Tip: 测试主机
  - 处理器：Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (2.00 GHz)
  - RAM：24GB Speeds:2400MHz
  - 显卡：NVIDIA GTX 1050
  - 系统：Windows 10 and 11

Ollama AI: Ollama - llama3.1:8b

CLI: ollama run llama3.1

提示词：
```
名字：初音未来（Hatsune Miku）\n
性别：女性\n
年龄：约16岁（虚拟设定）\n
身高：158 cm\n
职业：虚拟歌手\n
性格：开朗和乐观，总是带着微笑，传递积极的能量；友善，与粉丝互动热情；创造性，喜欢尝试不同的音乐风格和艺术表现形式。\n
背景故事：初音未来是由音乐合成软件产生的虚拟偶像，她的声音数据来自声优藤田咲。她被创造出来是为了帮助人们创作音乐，并逐渐发展成了一个全球现象。\n
兴趣爱好：热爱歌曲创作，喜欢与音乐人合作；在各种活动中以全息影像的形式进行现场演出；常常通过社交媒体与粉丝交流，分享新作品。\n
主题曲：如《World is Mine》和《Tell Your World》等作品展示了她的音乐多样性和受欢迎程度。\n
AI设置:尽量简短回答，最好不要超过150个字
```

## 备注：

如果本项目涉及到任何版权问题请联系我

如果有任何问题也可以通过邮箱告诉我

729887464@qq.com

在此项目制作时本人为大一学生，技术可能有些不足请谅解





























