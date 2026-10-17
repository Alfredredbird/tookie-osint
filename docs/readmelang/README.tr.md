![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)

![GitHub contributors](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub forks](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub Repo stars](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# (Tookie-OSINT V4 Yayınlandı!)
Tookie-OSINT, maksimum performans için %100 sıfırdan yeniden yazıldı!
Çeviriler henüz tam olarak hazır değil.
Wiki ve Readme sayfaları güncelleme sürecindedir.

## 🌐 Dil Seçenekleri

> Dilinizi seçin / Select your language

| [English](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.en.md) | [Türkçe](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.tr.md) | [日本語](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ja.md) | [简体中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-cn.md) | [繁體中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-tw.md) | [Français](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fr.md) | [Español](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.es.md) | [Deutsch](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.de.md) | [Русский](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ru.md) | [Português](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.pt.md) | [Italiano](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.it.md) | [فارسی](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fa.md) | [العربية](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ar.md) | [हिन्दी](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.hi.md) | [Suomi](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fi.md) | [עברית](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.he.md) | [Bahasa Indonesia](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.id.md) |

# 🔎 Genel Bakış
Tookie-OSINT, kullanımı kolay ve son derece sade bir arayüze sahiptir.
Tookie-OSINT'in temel amacı, girilen kullanıcı adlarını farklı platformlar üzerinde tespit etmektir.
Sherlock aracına benzer bir mantıkla çalışır; farklı web sitelerindeki kullanıcı hesaplarını tarar ve bu süreçte %80'e yakın bir başarı oranına sahiptir.
Bu araç ben ve topluluk tarafından geliştirilmiş olup kullanımınıza sunulmuştur.
Aracın kötü niyetli kullanımından doğabilecek hiçbir sorumluluğu kabul etmiyorum. :(
Tookie-OSINT'in, yeni başlayan yazılımcıların veya sızma testi uzmanlarının (pentester) OSINT dünyasına adım atmalarına yardımcı olmak amacıyla oluşturulduğunu lütfen unutmayın. Nihai hedefim, Tookie-OSINT'i olabildiğince mükemmel ve yeni başlayanlar için anlaşılır hale getirmektir. Tookie-OSINT, Python 3.12 için optimize edilmiştir. Katkıda bulunmak isterseniz bir fork oluşturup değişikliklerinizi Pull Request (PR) olarak gönderebilirsiniz. :D

<img width="940" height="1299" alt="image" src="https://github.com/user-attachments/assets/bdd71b8b-2145-4d6d-9eec-36f7666a5673" />

# 📦 Kali Linux Kurulumu
Tookie-OSINT artık Kali Linux paket deposunda yer almaktadır!
Aşağıdaki komutla yükleyebilirsiniz:

    sudo apt install tookie-osint

Ayrıntılı bilgi için [buraya](https://www.kali.org/tools/tookie-osint/) göz atabilirsiniz.

# 📦 Linux Kurulumu
Gerekli bağımlılıklar otomatik olarak yüklenecektir.

    git clone https://github.com/alfredredbird/tookie-osint.git
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 Debian Tabanlı Sistemlerde Kurulum
Gerekli bağımlılıklar otomatik olarak yüklenecektir.

    1. Debian paketini indirin:
    https://github.com/Alfredredbird/tookie-osint/releases
    
    2. Kurulumu yapın:
    sudo dpkg -i tookie-osint.deb

# 📦 Diğer Kurulum Seçenekleri
Diğer kurulum talimatlarına Wiki sayfamızdan ulaşabilirsiniz.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py

# 💻 Test Edilen İşletim Sistemleri

<table>
    <tr>
        <th>İşletim Sistemi</th>
        <th>Sürüm</th>
    </tr>
    <tr>
        <td>MacOS</td>
        <td>Monterey 12.6.7</td>
    </tr>
    <tr>
        <td>Windows</td>
        <td>11 / 10</td>
    </tr>
    <tr>
        <td>Termux</td>
        <td>0.118.0</td>
    </tr>
    <tr>
        <td>Kali Linux</td>
        <td>Rolling / Sana</td>
    </tr>
    <tr>
        <td>Parrot OS</td>
        <td>3.1</td>
    </tr>
    <tr>
        <td>Ubuntu</td>
        <td>22.04 / 20.04</td>
    </tr>
    <tr>
        <td>Debian</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>Alpine</td>
        <td>3.10</td>
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

# 📖 Gereksinimler

Bağımlılıklar oldukça geniş bir listeye sahiptir:

- colorama
- requests
- argparse
- selenium
- webdriver-manager

# 🗣️ Desteklenen Wiki Dilleri
(Çevirmenlere ihtiyacımız var 😭)
(Aşağıdaki dillerin güncellenmesi gerekebilir)

- [x] İngilizce
- [x] İtalyanca
- [x] İbranice
- [x] İspanyolca
- [x] Fransızca
- [x] Arapça
- [x] Almanca
- [x] Hintçe
- [x] Rusça
- [x] Portekizce
- [x] Endonezce
- [x] Fince
- [x] Geleneksel Çince
- [x] Basitleştirilmiş Çince
- [x] Japonca
- [x] Farsça
- [x] Türkçe

# 📕 Planlanan Özellikler
 (Katkıda bulunmak isteyenler için harika ilk konular! :D)

- [X] Betik (Scripting) desteği
- [ ] Tor Arama (Planlanan)
- [ ] Web Arayüzü (Planlanan)
- [X] Web Scraper
- [X] Veri Web Kazıma (Data Webscrapping)
- [ ] Telefon Numarası OSINT
- [ ] Özel Eklentiler (Custom Plugins)
- [ ] Detaylı Raporlar (Beta)
- [ ] E-posta OSINT (Beta)
- [x] CSV
- [ ] Grafik Arayüz (GUI)
- [X] Daha Doğru Sonuçlar
- [ ] Bulunan URL'leri Otomatik Açma
- [X] Dosya Geri Yükleme
- [X] Webhooks (Beta)
- [x] Headless Modu
- [x] Otomasyon
- [X] Çoklu İzlek (Threading)

# 🍿 Tanıtım / Kullanım
Tookie-OSINT geniş bir kullanım seçeneği sunar.
`-h` parametresini kullanarak yardım menüsünü görüntüleyebilirsiniz.

<img width="769" height="1032" alt="image" src="https://github.com/user-attachments/assets/9ed8b048-42b0-49e8-86ef-923e6a6d5851" />

# ⁉️ Yardıma mı İhtiyacınız Var?
Yardım için https://github.com/alfredredbird/tookie-osint/issues adresine veya Wiki sayfasına göz atabilirsiniz.
Hâlâ yardıma ihtiyacınız varsa aşağıdaki iletişim kanallarından ve Discord sunucusundan ulaşabilirsiniz. :D

# 🤔 Aradığınız Web Sitesini Bulamadınız mı?
Siti içeren bir Pull Request (PR) veya hata bildirimi (Bug Report) açın, ekleyelim! :D

# 📗 Bilgi:

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
    <tr>
        <th>Sürümler (Releases)</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Katkıda Bulunanlar</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Makaleler
Aracımız hakkında yazılmış çeşitli makaleler bulunmaktadır. İncelemekten çekinmeyin :D (Bu makaleler ilgili yazarlara aittir.)

<table>
    <tr>
        <th>Sherlockeye</th>
        <th>https://sherlockeye.io/blog/tookie-osint-what-it-is-how-it-works</th>
    </tr>
    <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/news/757502/</th>
    </tr>
    <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/amp/publications/769690/</th>
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
        <th>Medevel</th>
        <th>https://medevel.com/31-osint-tools/</th>
    </tr>
    <tr>
        <th>Medium</th>
        <th>https://medium.com/age-of-awareness/osint-unleashed-the-5-best-tools-for-cyber-investigators-8ff08fe9a4ba</th>
    </tr>
    <tr>
        <th>Kali Linux Tutorials</th>
        <th>https://kalilinuxtutorials.com/tookie-osint/</th>
    </tr>
    <tr>
        <th>JJ Gallego</th>
        <th>https://medium.com/cyberscribers-exploring-cybersecurity/osint-for-nicknames-tookie-osint-1364a3c87acf</th>
    </tr>
</table>

# 🎬 Resmi Eğitim Videoları

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g

# 📘 İletişim

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Diğer Araçlar

Geliştirilen diğer araçlar:
- Bibi-Bird (Beta): https://github.com/alfredredbird/Bibi-Bird
- Open-Wrecks: https://github.com/Alfredredbird/Open-Wrecks

# 🤝 Ortaklıklar
Tookie-OSINT projesiyle ortaklık kurmak ister misiniz? İletişime geçmekten çekinmeyin.

Ortaklarımız:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT