![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHubin osallistujat](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHubin koodin koko tavuina](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub-haarat](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub-repon tähdet](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Koodityyli: musta](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Suorita Repl.it:ssä](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (Meidän piti brändätä uudelleen)

# 🔎 Yleiskatsaus
Tookie-osintilla on helppokäyttöinen käyttöliittymä ja se on todella suoraviivainen.
Tookie-osintin pääidea on löytää käyttäjätunnuksia, joita pyydetään syötteestä.
Tookie-osint on samanlainen kuin Sherlock-niminen työkalu. Se löytää kaikki käyttäjätilit eri verkkosivustoilta ja Tookie-osint onnistuu tässä tehtävässä lähes 80% ajasta.
Työkalumme on minun ja yhteisön luoma, ja se on käytettävissäsi.
En ota vastuuta mistään haitallisista toimista ja/tai vastuusta, joka aiheutuu työkalustani. :(
Huomaa, että Tookie-osint luotiin auttamaan uusia ohjelmoijia tai pentestereitä pääsemään OSINT-maailmaan. Pitkän aikavälin tavoitteenani on tehdä Tookie-osintista niin täydellinen kuin mahdollista ja tehdä siitä helppo ymmärtää uusille ohjelmoijille. Huomaa myös, että Tookie-osint on optimoitu Python 3.12:lle. Jos haluat osallistua, tee haara ja tee vetopyyntö lähettääksesi muutoksesi. :D

![kuva](https://github.com/Alfredredbird/tookie-osint/assets/105014217/380da10a-ff65-4137-a213-7bdd0dfdb9ed)


# 📦 Asennus
Vaatimukset asennetaan automaattisesti.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint

# 📦 Manuaalinen asennus
    lataa uusin julkaisu osoitteesta: https://github.com/alfredredbird/tookie-osint/releases.
    pura sitten zip- tai tar.gz-tiedosto

    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint


# 📦 Termux-asennus

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 Muut Linux-asennukset
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 tookie-osint


# 🖋 Komentosarjat Tookien kanssa

Katso lisätietoja [täältä](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie).



# 💻 Testatut käyttöjärjestelmät

<table>
    <tr>
        <th>Käyttöjärjestelmä</th>
        <th> Versio </th>
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
        <td>Liukuva julkaisu</td>
    </tr>
</table>

# 📖 Vaatimukset

On paljon Lol

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️Tuetut kielet
(tarvitsemme kääntäjiä 😭)
- [x] Englanti
- [x] Italia
- [x] Heprea
- [x] Espanja
- [x] Ranska
- [x] Arabia
- [x] Saksa
- [x] Hindi
- [x] Venäjä
- [x] Portugali
- [X] Indonesia
- [X] Suomi
- [X] Perinteinen kiina
- [x] Yksinkertaistettu kiina
- [x] Japani
- [x] Farsi

# 📕 Tulevat ominaisuudet
 (Ne ovat hienoja ensimmäisiä numeroita :D)
- [ ] Tor-haku (beta)
- [X] Web-käyttöliittymä (beta)
- [X] Verkkosivujen kaavin
- [X] Puhelinnumeron OSINT
- [X] Mukautetut laajennukset
- [ ] Yksityiskohtaiset raportit (beta)
- [ ] Sähköpostin OSINT (beta)
- [x] CSV
- [ ] URL-osoitteen raa'an voiman käyttö
- [ ] Graafinen käyttöliittymä
- [ ] Tarkemmat tulokset (beta)
- [ ] Avaa löydetyt URL-osoitteet automaattisesti
- [ ] Verkkokoukut
- [x] Päätön tila
- [x] Automaatio

# 🍿 Esittely
Tookie-osintilla on laaja valikoima vaihtoehtoja käytettäväksi.
Kirjoittamalla -h kahdesti näytetään ohjevalikko.

![kuva](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ Tarvitsetko apua?
Katso https://github.com/alfredredbird/tookie-osint/issues tai WiKi saadaksesi apua.
Tarvitsetko edelleen apua? Ota yhteyttä ja Discord-palvelin alla :D

# 🤔 Etkö löydä etsimääsi verkkosivustoa?
Tee vetopyyntö tai virheraportti sivustosta, niin lisäämme sen. :D

# 📗 Tiedot:

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Julkaisut</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Osallistujat</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Artikkelit
Työkalustamme on kirjoitettu useita artikkeleita. Voit vapaasti tutustua niihin :D Nämä artikkelit kuuluvat niiden kunnioittaville omistajille.
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
        <th>Kali Linux -oppaat</th>
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

# 🎬 Oppaat

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 Yhteystiedot

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Muut työkalut

Muut laivaston työkalut:
- Bibi-Bird (beta): https://github.com/alfredredbird/Bibi-Bird


# 🤝 Kumppanuus
Haluatko tehdä yhteistyötä tookie-osint-projektin kanssa? Ota rohkeasti yhteyttä.


Kumppanit:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT