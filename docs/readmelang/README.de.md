![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub-Mitwirkende](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub-Code-Größe in Bytes](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub-Forks](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub-Repo-Sterne](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Codestil: schwarz](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Auf Repl.it ausführen](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (Wir mussten umfirmieren)

# 🔎 Übersicht
Tookie-osint hat eine einfach zu bedienende Benutzeroberfläche und ist wirklich unkompliziert.
Die Hauptidee von Tookie-osint ist es, Benutzernamen zu entdecken, die von einer Eingabe angefordert werden.
Tookie-osint ähnelt dem Tool namens Sherlock. Es entdeckt alle Benutzerkonten auf verschiedenen Websites und Tookie-osint ist bei dieser Aufgabe zu fast 80 % erfolgreich.
Unser Tool wurde von mir und der Community erstellt und steht Ihnen zur Verfügung.
Ich übernehme keine Verantwortung für böswillige Handlungen und/oder Verantwortung, die durch mein Tool verursacht werden. :(
Bitte beachten Sie, dass Tookie-osint erstellt wurde, um neuen Programmierern oder Pentestern den Einstieg in die Welt von OSINT zu erleichtern. Mein langfristiges Ziel ist es, Tookie-osint so perfekt wie möglich zu machen und es neuen Programmierern leicht verständlich zu machen. Beachten Sie auch, dass Tookie-osint für Python 3.12 optimiert ist. Wenn Sie einen Beitrag leisten möchten, erstellen Sie einen Fork und stellen Sie eine Pull-Anfrage, um Ihre Änderungen einzureichen. :D

![Bild](https://github.com/Alfredredbird/tookie-osint/assets/105014217/380da10a-ff65-4137-a213-7bdd0dfdb9ed)


# 📦 Installation
Die Anforderungen werden automatisch installiert.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint

# 📦 Manuelle Installation
    laden Sie die neueste Version von herunter: https://github.com/alfredredbird/tookie-osint/releases.
    extrahieren Sie dann die Zip- oder tar.gz-Datei

    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint


# 📦 Termux-Installation

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 Andere Linux-Installationen
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 tookie-osint


# 🖋 Scripting mit Tookie

Weitere Informationen finden Sie [hier](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie).



# 💻 Getestete Betriebssysteme

<table>
    <tr>
        <th>Betriebssystem</th>
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

# 📖 Anforderungen

Es gibt eine Menge Lol

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️Unterstützte Sprachen
(wir brauchen Übersetzer 😭)
- [x] Englisch
- [x] Italienisch
- [x] Hebräisch
- [x] Spanisch
- [x] Französisch
- [x] Arabisch
- [x] Deutsch
- [x] Hindi
- [x] Russisch
- [x] Portugiesisch
- [X] Indonesisch
- [X] Finnisch
- [X] Chinesisch (traditionell)
- [x] Chinesisch (vereinfacht)
- [x] Japanisch
- [x] Farsi

# 📕 Kommende Funktionen
 (Sie sind großartige erste Ausgaben :D)
- [ ] Tor-Suche (in Beta)
- [X] WebUi (in Beta)
- [X] Webscraper
- [X] Telefonnummer OSINT
- [X] Benutzerdefinierte Plugins
- [ ] Detaillierte Berichte (in Beta)
- [ ] E-Mail-OSINT (in Beta)
- [x] CSV
- [ ] Url Brute Forcing
- [ ] GUI
- [ ] Genauere Ergebnisse (in Beta)
- [ ] Entdeckte URLs automatisch öffnen
- [ ] Web-Hooks
- [x] Headless-Modus
- [x] Automatisierung

# 🍿 Schaufenster
Tookie-osint hat eine Vielzahl von Optionen zur Verwendung.
Die zweimalige Eingabe von -h zeigt das Hilfemenü an.

![Bild](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ Brauchen Sie Hilfe?
Schauen Sie sich https://github.com/alfredredbird/tookie-osint/issues oder das WiKi an, um Hilfe zu erhalten.
Brauchen Sie immer noch Hilfe? Kontakt und Discord Server unten :D

# 🤔 Können Sie die gesuchte Website nicht finden?
Stellen Sie eine Pull-Anfrage oder einen Fehlerbericht mit der Website und wir werden sie hinzufügen. :D

# 📗 Info:

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Veröffentlichungen</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Mitwirkende</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Artikel
Es wurden mehrere Artikel über unser Tool geschrieben. Schauen Sie sie sich ruhig an :D Diese Artikel gehören ihren respektvollen Besitzern.
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

# 🎬 Tutorials

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 Kontakt

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Andere Werkzeuge

Andere Werkzeuge in der Flotte:
- Bibi-Bird (beta): https://github.com/alfredredbird/Bibi-Bird


# 🤝 Partnerschaft
Möchten Sie mit dem tookie-osint-Projekt zusammenarbeiten? Zögern Sie nicht, uns zu kontaktieren.


Partner:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT