![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub contributors](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub forks](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub Repo stars](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# (Tookie-OSINT V4 is here!)
Tookie-OSINT has been re-written 100% from scratch for ultimate performance!
Translations are still not ready yet.
The wiki and readme are going through some changes. 

## 🌐 Language

> Select your language / 言語を選択してください / 选择你的语言 / Sélectionnez votre langue / Seleccione su idioma / Wählen Sie Ihre Sprache / Выберите язык / اختر لغتك / زبان خود را انتخاب کنید / Selecione seu idioma / Scegli la tua lingua / 선택 언어 / Pilih bahasa Anda / בחר את השפה שלך / अपनी भाषा चुनें / Valitse kieli / 選擇您的語言

| [English](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.en.md) | [日本語](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ja.md) | [简体中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-cn.md) | [繁體中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-tw.md) | [Français](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fr.md) | [Español](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.es.md) | [Deutsch](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.de.md) | [Русский](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ru.md) | [Português](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.pt.md) | [Italiano](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.it.md) | [فارسی](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fa.md) | [العربية](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ar.md) | [हिन्दी](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.hi.md) | [Suomi](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fi.md) | [עברית](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.he.md) |
| [Bahasa Indonesia](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.id.md) |

<!--
デバッグ用: 言語切り替えテーブルが正しく表示されているか確認してください。
If you find any issues with the language links, please open an issue or PR.
-->

# 🔎 Overview
Tookie-osint has a simple-to-use UI and is really straightforward.
The main idea of Tookie-osint is to discover usernames that are requested from an input.
Tookie-osint is similar to the tool called Sherlock. It discovers all the user accounts across different websites and Tookie-osint is successful at this task almost 80% of the time.
Our tool was created by me and the community and is available for your use.
I do not take responsibility for any malicious actions and/or responsibility caused by my tool. :(
Please note that Tookie-osint was created to help new programmers or pentesters get into the world of OSINT. My end term goal is to make Tookie-osint as perfect as I can and make it easy for new programmers to understand. Also take note that Tookie-osint is optimized for Python 3.12. If you want to contribute, make a fork and make a pull request to submit your changes. :D
<img width="769" height="1032" alt="image" src="https://github.com/user-attachments/assets/de7a5e05-d632-4199-9857-d1ca9000e8f2" />




# 📦 Linux Installation
The requirements will be automatically installed.

    git clone https://github.com/alfredredbird/tookie-osint.git
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 Debian Based Installation
The requirements will be automatically installed.

    download debian packaged from
    https://github.com/Alfredredbird/tookie-osint/releases
    
    sudo dpgk -i tookie-osint.deb

# 📦 Manual Install
    download the latest release from: https://github.com/alfredredbird/tookie-osint/releases.
    then extract the zip or tar.gz

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint

# 📦 Other Installations
You can find more install instructions on the Wiki.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 💻 Tested OS

<table>
    <tr>
        <th>Operative system</th>
        <th> Version </th>
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
        <td>Rolling Release</td>
    </tr>
</table>

# 📖 Requirements

There Is A Lot Lol

- colorama 
- requests
- argparse
- selenium 
- webdriver-manager 

# 🗣️Supported Languages
(we need translators 😭)
(The following languages are ready but not implemented.)
- [x] English
- [ ] Italian
- [ ] Hebrew
- [ ] Spanish
- [ ] French
- [ ] Arabic
- [ ] German
- [ ] Hindi
- [ ] Russian
- [ ] Portuguese
- [ ] Indonesian
- [ ] Finnish
- [ ] Chinese traditional
- [ ] Chinese Simplified
- [ ] Japanese
- [ ] Farsi
- [ ] Turkish

# 📕 Upcoming Features
 (They Are Great First Issues :D)
- [ ] Tor Searching (planned)
- [ ] WebUi (planned)
- [X] Webscraper
- [X] Data Webscrapping
- [ ] Phone Number OSINT
- [ ] Custom Plugins
- [ ] Detailed Reports (in beta)
- [ ] Email OSINT (in beta)
- [x] CSV
- [ ] Url Brute Forcing
- [ ] GUI
- [X] More Accurate Results
- [ ] Auto Open Discovered URLs
- [ ] Web Hooks
- [x] Headless mode
- [x] Automation
- [X] Threading

# 🍿 Showcase
Tookie-osint has a wide variety of options to use.
Using `-h` shows the help menu.

<img width="769" height="1032" alt="image" src="https://github.com/user-attachments/assets/9ed8b048-42b0-49e8-86ef-923e6a6d5851" />


# ⁉️ Need Help?
Check out https://github.com/alfredredbird/tookie-osint/issues or the WiKi for help.
Still Need Help? Contact And Discord Server Below :D

# 🤔 Cant Find The WebSite Your Looking For?
Make a pull request or a bug report with the site and we will add it. :D

# 📗 Info:

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Releases</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Contributors</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Articles
There has been several articles written about our tool. Feal free to check them out :D  Theses articles belong to their respectful owners.
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
        <th>internet intelligence</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Kali Linux Tutorials</th>
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

# 🎬 Official Tutorials

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
  
# 📘 Contact

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Other Tools

Other tools in the fleet:
- Bibi-Bird (beta): https://github.com/alfredredbird/Bibi-Bird
- Open-Wrecks: https://github.com/Alfredredbird/Open-Wrecks


# 🤝 Partnership
Want to partner with the tookie-osint project? Feel free to reach out.


Partners:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT
