![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub 貢獻者](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub 程式碼大小 (位元組)](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub 分支](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub 儲存庫星級](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![程式碼樣式：黑色](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![在 Repl.it 上執行](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (我們必須重塑品牌)

# 🔎 總覽
Tookie-osint 有一個簡單易用的使用者介面，而且非常直接。
Tookie-osint 的主要思想是從輸入中發現請求的使用者名稱。
Tookie-osint 類似於一個名為 Sherlock 的工具。它會發現不同網站上的所有使用者帳戶，Tookie-osint 在這項任務上的成功率幾乎達到 80%。
我們的工具是由我和社群創建的，可供您使用。
對於因我的工具造成的任何惡意行為和/或責任，我概不負責。:(
請注意，Tookie-osint 的創建是為了幫助新的程式設計師或滲透測試人員進入 OSINT 的世界。我的最終目標是讓 Tookie-osint 盡可能完美，並讓新的程式設計師易於理解。另請注意，Tookie-osint 已針對 Python 3.12 進行了最佳化。如果您想做出貢獻，請建立一個分支並提出拉取請求以提交您的變更。:D

<img width="952" height="1300" alt="image" src="https://github.com/user-attachments/assets/fea15d7b-1e6d-44d7-b444-aefa56bcc6b2" />


# 📦 安裝
需求將會自動安裝。

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 手動安裝
    從以下網址下載最新版本：https://github.com/alfredredbird/tookie-osint/releases。
    然後解壓縮 zip 或 tar.gz

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint


# 📦 Termux 安裝

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 其他 Linux 安裝
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 🖋 使用 Tookie 編寫指令碼

請參閱[此處](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie)以取得更多詳細資料。



# 💻 測試的作業系統

<table>
    <tr>
        <th>作業系統</th>
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
        <td>滾動發行</td>
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

# 🗣️支援的語言
(我們需要翻譯人員 😭)
- [x] 英文
- [x] 義大利文
- [x] 希伯來文
- [x] 西班牙文
- [x] 法文
- [x] 阿拉伯文
- [x] 德文
- [x] 印度文
- [x] 俄文
- [x] 葡萄牙文
- [X] 印尼文
- [X] 芬蘭文
- [X] 繁體中文
- [x] 簡體中文
- [x] 日文
- [x] 波斯文

# 📕 即將推出的功能
 （它們是很棒的初步問題 :D）
- [ ] Tor 搜尋（測試版）
- [X] WebUi（測試版）
- [X] 網路爬蟲
- [X] 電話號碼 OSINT
- [X] 自訂外掛程式
- [ ] 詳細報告（測試版）
- [ ] 電子郵件 OSINT（測試版）
- [x] CSV
- [ ] 網址暴力破解
- [ ] GUI
- [ ] 更準確的結果（測試版）
- [ ] 自動開啟發現的網址
- [ ] Web Hook
- [x] 無頭模式
- [x] 自動化

# 🍿 展示
Tookie-osint 有多種選項可供使用。
輸入 -h 兩次會顯示說明功能表。

![圖片](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ 需要協助嗎？
請查看 https://github.com/alfredredbird/tookie-osint/issues 或 WiKi 以取得協助。
仍需要協助嗎？請聯絡下方的 Discord 伺服器 :D

# 🤔 找不到您要尋找的網站嗎？
提出拉取請求或包含網站的錯誤報告，我們會將其新增。:D

# 📗 資訊：

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>發行版本</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>貢獻者</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 文章
關於我們的工具，已經有幾篇文章發表。歡迎隨時查看 :D 這些文章屬於其各自的所有者。
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
        <th>網路情報</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Kali Linux 教學</th>
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

# 🎬 教學

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 聯絡方式

- Twitter：https://twitter.com/alfredredbird1

# 🛠 其他工具

機隊中的其他工具：
- Bibi-Bird（測試版）：https://github.com/alfredredbird/Bibi-Bird


# 🤝 合作夥伴關係
想與 tookie-osint 專案合作嗎？歡迎隨時與我們聯繫。


合作夥伴：
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT