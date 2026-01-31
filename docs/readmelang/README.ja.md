![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub コントリビューター](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub コードサイズ (バイト)](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub フォーク](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub リポジトリスター](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![コードスタイル: ブラック](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Repl.it で実行](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (ブランド名を変更する必要がありました)

# 🔎 概要
Tookie-osint は使いやすい UI を備えており、非常に簡単です。
Tookie-osint の主なアイデアは、入力から要求されたユーザー名を発見することです。
Tookie-osint は Sherlock というツールに似ています。さまざまな Web サイト上のすべてのユーザーアカウントを検出し、Tookie-osint はこのタスクにほぼ 80% の確率で成功します。
私たちのツールは私とコミュニティによって作成され、自由に使用できます。
私のツールによって引き起こされた悪意のある行為や責任については一切責任を負いません。:(
Tookie-osint は、新しいプログラマーやペンテスターが OSINT の世界に参入するのを支援するために作成されたことに注意してください。私の最終的な目標は、Tookie-osint をできる限り完璧にし、新しいプログラマーが理解しやすいようにすることです。また、Tookie-osint は Python 3.12 に最適化されていることにも注意してください。貢献したい場合は、フォークを作成し、プルリクエストを送信して変更を送信してください。:D

<img width="930" height="1056" alt="image" src="https://github.com/user-attachments/assets/da493d67-cde1-4ded-bf7e-af62d14dc016" />


# 📦 インストール
要件は自動的にインストールされます。

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 手動インストール
    最新のリリースを https://github.com/alfredredbird/tookie-osint/releases からダウンロードします。
    次に zip または tar.gz を展開します

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint




# 📦 その他の Linux インストール
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 🖋 Tookie を使用したスクリプト

詳細については、[こちら](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie) を参照してください。



# 💻 テスト済み OS

<table>
    <tr>
        <th>オペレーティングシステム</th>
        <th> バージョン </th>
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
        <td>ローリングリリース</td>
    </tr>
</table>

# 📖 要件

たくさんあります（笑）

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️サポートされている言語
(翻訳者が必要です 😭)
- [x] 英語
- [x] イタリア語
- [x] ヘブライ語
- [x] スペイン語
- [x] フランス語
- [x] アラビア語
- [x] ドイツ語
- [x] ヒンディー語
- [x] ロシア語
- [x] ポルトガル語
- [X] インドネシア語
- [X] フィンランド語
- [X] 中国語（繁体字）
- [x] 中国語（簡体字）
- [x] 日本語
- [x] ペルシャ語

# 📕 今後の機能
 （これらは素晴らしい最初の問題です :D）
- [ ] Tor 検索 (ベータ版)
- [X] WebUi (ベータ版)
- [X] ウェブスクレイパー
- [X] 電話番号 OSINT
- [X] カスタムプラグイン
- [ ] 詳細レポート (ベータ版)
- [ ] メール OSINT (ベータ版)
- [x] CSV
- [ ] URL ブルートフォース
- [ ] GUI
- [ ] より正確な結果 (ベータ版)
- [ ] 発見された URL を自動的に開く
- [ ] Web フック
- [x] ヘッドレスモード
- [x] 自動化

# 🍿 ショーケース
Tookie-osint にはさまざまなオプションがあります。
-h を 2 回入力すると、ヘルプメニューが表示されます。

![画像](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ ヘルプが必要ですか？
ヘルプについては、https://github.com/alfredredbird/tookie-osint/issues または WiKi を確認してください。
まだヘルプが必要ですか？以下の連絡先と Discord サーバー :D

# 🤔 探している Web サイトが見つかりませんか？
サイトでプルリクエストまたはバグレポートを作成していただければ、追加します。:D

# 📗 情報：

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>リリース</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>コントリビューター</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 記事
私たちのツールに関する記事がいくつか書かれています。ぜひチェックしてみてください :D これらの記事はそれぞれの所有者に帰属します。
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
        <th>インターネットインテリジェンス</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Kali Linux チュートリアル</th>
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

# 🎬 チュートリアル

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 連絡先

- Twitter: https://twitter.com/alfredredbird1

# 🛠 その他のツール

フリート内のその他のツール：
- Bibi-Bird (ベータ版): https://github.com/alfredredbird/Bibi-Bird


# 🤝 パートナーシップ
tookie-osint プロジェクトと提携しませんか？お気軽にご連絡ください。


パートナー：
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT