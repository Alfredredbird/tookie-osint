![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub 贡献者](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub 代码大小（字节）](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub 分叉](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub 存储库星标](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![代码风格：黑色](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![在 Repl.it 上运行](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (我们必须重塑品牌)

# 🔎 概述
Tookie-osint 有一个简单易用的用户界面，而且非常直接。
Tookie-osint 的主要思想是从输入中发现请求的用户名。
Tookie-osint 类似于一个名为 Sherlock 的工具。它会发现不同网站上的所有用户帐户，Tookie-osint 在这项任务上的成功率几乎达到 80%。
我们的工具是由我和社区创建的，可供您使用。
对于因我的工具造成的任何恶意行为和/或责任，我概不负责。:(
请注意，Tookie-osint 的创建是为了帮助新的程序员或渗透测试人员进入 OSINT 的世界。我的最终目标是让 Tookie-osint 尽可能完美，并让新的程序员易于理解。另请注意，Tookie-osint 已针对 Python 3.12 进行了优化。如果您想做出贡献，请创建一个分支并提出拉取请求以提交您的更改。:D

![图片](https://github.com/Alfredredbird/tookie-osint/assets/105014217/380da10a-ff65-4137-a213-7bdd0dfdb9ed)


# 📦 安装
需求将会自动安装。

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint

# 📦 手动安装
    从以下网址下载最新版本：https://github.com/alfredredbird/tookie-osint/releases。
    然后解压缩 zip 或 tar.gz

    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint


# 📦 Termux 安装

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 其他 Linux 安装
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 tookie-osint


# 🖋 使用 Tookie 编写脚本

请参阅[此处](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie)以获取更多详细信息。



# 💻 测试的操作系统

<table>
    <tr>
        <th>操作系统</th>
        <th> 版本 </th>
    </tr>
    <tr>
        <td>MacOS</td>
        <td> Monterey 12.6.7 </td>
    </tr>
    <tr>
        <td>Windows</td>
        <td>11/10</td>
    </tr>
 <tr>
        <td>Termux</td>
        <td>0.118.0</td>
    </tr>
    <tr>
        <td>Kali linux</td>
        <td> Rolling / Sana</td>
    </tr>
    <tr>
        <td>Parrot OS</td>
        <td>3.1 </td>
    </tr>
    <tr>
        <td>Ubuntu</td>
        <td>22.04/20.04 </td>
    </tr>
    <tr>
        <td>Debian</td>
        <td>10.00 </td>
    </tr>
   <tr>
        <td>Alpine</td>
        <td>3.10 </td>
    </tr>
  <tr>
        <td>Fedora</td>
        <td>v33</td>
    </tr>
  <tr>
        <td>Arch Linux</td>
        <td>2021.07.01</td>
    </tr>
  <tr>
        <td>Manjaro</td>
        <td>21</td>
    </tr>
   <tr>
        <td>Void</td>
        <td>滚动发行</td>
    </tr>
</table>

# 📖 需求

有很多哈哈

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️支持的语言
(我们需要翻译人员 😭)
- [x] 英文
- [x] 意大利文
- [x] 希伯来文
- [x] 西班牙文
- [x] 法文
- [x] 阿拉伯文
- [x] 德文
- [x] 印度文
- [x] 俄文
- [x] 葡萄牙文
- [X] 印尼文
- [X] 芬兰文
- [X] 繁体中文
- [x] 简体中文
- [x] 日文
- [x] 波斯文

# 📕 即将推出的功能
 （它们是很棒的初步问题 :D）
- [ ] Tor 搜索（测试版）
- [X] WebUi（测试版）
- [X] 网络爬虫
- [X] 电话号码 OSINT
- [X] 自定义插件
- [ ] 详细报告（测试版）
- [ ] 电子邮件 OSINT（测试版）
- [x] CSV
- [ ] 网址暴力破解
- [ ] GUI
- [ ] 更准确的结果（测试版）
- [ ] 自动打开发现的网址
- [ ] Web Hook
- [x] 无头模式
- [x] 自动化

# 🍿 展示
Tookie-osint 有多种选项可供使用。
输入 -h 两次会显示帮助菜单。

![图片](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ 需要帮助吗？
请查看 https://github.com/alfredredbird/tookie-osint/issues 或 WiKi 以获取帮助。
仍需要帮助吗？请联系下方的 Discord 服务器 :D

# 🤔 找不到您要寻找的网站吗？
提出拉取请求或包含网站的错误报告，我们会将其添加。:D

# 📗 信息：

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>发行版本</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>贡献者</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 文章
关于我们的工具，已经有几篇文章发表。欢迎随时查看 :D 这些文章属于其各自的所有者。
<table>
    <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/news/757502/</th>
    </tr>
 <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/amp/publications/769690/</th></th>
    </tr>

   <tr>
        <th>Speka Media</th>
        <th>https://speka.media/rozrobniki-predstavili-alfred-vidkritu-utilitu-dlya-osint-pygwkp</th>
    </tr>
    <tr>
        <th>Sibnet</th>
        <th>https://info.sibnet.ru/article/646445/</th>
    </tr>
    <tr>
        <th>NetRunner</th>
        <th>https://blog.netrunner.lol/alfred-advanced-osint-info-gathering-tool-afc1a7afd8a3</th>
    </tr>

   <tr>
        <th>gebutcher</th>
        <th>https://gebutcher.blogspot.com/2023/10/Osintalfred.html?m=1</th>
    </tr>
     <tr>
        <th>Iguru</th>
        <th>https://iguru.gr/alfred-ena-proigmeno-osint-programma/</th>
    </tr>
    <tr>
        <th>Medevel</th>
        <th>https://medevel.com/31-osint-tools/</th>
    </tr>
    <tr>
        <th>Medium</th>
        <th>https://medium.com/age-of-awareness/osint-unleashed-the-5-best-tools-for-cyber-investigators-8ff08fe9a4ba</th>
    </tr>
     <tr>
        <th>TechnoNews</th>
        <th>https://techno-news.net/2023/08/28/news_7132/</th>
    </tr>
    <tr>
        <th>Xhref</th>
        <th>  https://xhref.blogspot.com/2023/10/alfred-utilitas-open-source-untuk-osint.html</th>
    </tr>
     <tr>
        <th>JOEE txt</th>
        <th>https://www.joeetxt.com/2023/10/alfred-utilitas-open-source-untuk-osint.html</th>
    </tr>
    <tr>
        <th>网络情报</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Kali Linux 教程</th>
        <th>https://kalilinuxtutorials.com/tookie-osint/</th>
    </tr>
    <tr>
        <th>Hacks.gr</th>
        <th>https://en.hacks.gr/tookie-osint-ergaleio-sullogis-kai-analysis-dimosion-dedomenon/
    </th>
        <tr>
        <th>JJ Gallego</th>
        <th>https://medium.com/cyberscribers-exploring-cybersecurity/osint-for-nicknames-tookie-osint-1364a3c87acf</th>
    </tr>
    </tr>



</table>

# 🎬 教程

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 联系方式

- Twitter：https://twitter.com/alfredredbird1

# 🛠 其他工具

机队中的其他工具：
- Bibi-Bird（测试版）：https://github.com/alfredredbird/Bibi-Bird


# 🤝 合作伙伴关系
想与 tookie-osint 项目合作吗？欢迎随时与我们联系。


合作伙伴：
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT