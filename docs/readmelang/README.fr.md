![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![Contributeurs GitHub](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![Taille du code GitHub en octets](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![Forks GitHub](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![Étoiles du dépôt GitHub](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Style de code : noir](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Exécuter sur Repl.it](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (Nous avons dû changer de nom)

# 🔎 Aperçu
Tookie-osint a une interface utilisateur simple à utiliser et est très simple.
L'idée principale de Tookie-osint est de découvrir les noms d'utilisateur demandés à partir d'une entrée.
Tookie-osint est similaire à l'outil appelé Sherlock. Il découvre tous les comptes d'utilisateurs sur différents sites Web et Tookie-osint réussit cette tâche près de 80 % du temps.
Notre outil a été créé par moi et la communauté et est disponible pour votre usage.
Je n'assume aucune responsabilité pour les actions malveillantes et/ou la responsabilité causées par mon outil. :(
Veuillez noter que Tookie-osint a été créé pour aider les nouveaux programmateurs ou pentesteurs à entrer dans le monde de l'OSINT. Mon objectif à terme est de rendre Tookie-osint aussi parfait que possible et de le rendre facile à comprendre pour les nouveaux programmateurs. Notez également que Tookie-osint est optimisé pour Python 3.12. Si vous souhaitez contribuer, créez un fork et effectuez une pull request pour soumettre vos modifications. :D

<img width="952" height="1300" alt="image" src="https://github.com/user-attachments/assets/fea15d7b-1e6d-44d7-b444-aefa56bcc6b2" />


# 📦 Installation
Les dépendances seront installées automatiquement.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 Installation manuelle
    téléchargez la dernière version depuis : https://github.com/alfredredbird/tookie-osint/releases.
    extrayez ensuite le zip ou le tar.gz

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint


# 📦 Installation de Termux

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 Autres installations Linux
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 🖋 Scripting avec Tookie

Veuillez consulter [Ici](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie) pour plus de détails.



# 💻 Systèmes d'exploitation testés

<table>
    <tr>
        <th>Système d'exploitation</th>
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
        <td>Version continue</td>
    </tr>
</table>

# 📖 Exigences

Il y en a beaucoup mdr

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️Langues prises en charge
(nous avons besoin de traducteurs 😭)
- [x] Anglais
- [x] Italien
- [x] Hébreu
- [x] Espagnol
- [x] Français
- [x] Arabe
- [x] Allemand
- [x] Hindi
- [x] Russe
- [x] Portugais
- [X] Indonésien
- [X] Finnois
- [X] Chinois traditionnel
- [x] Chinois simplifié
- [x] Japonais
- [x] Farsi

# 📕 Fonctionnalités à venir
 (Ce sont de super premiers numéros :D)
- [ ] Recherche Tor (en version bêta)
- [X] Interface utilisateur Web (en version bêta)
- [X] Webscraper
- [X] OSINT de numéro de téléphone
- [X] Plugins personnalisés
- [ ] Rapports détaillés (en version bêta)
- [ ] OSINT par e-mail (en version bêta)
- [x] CSV
- [ ] Forçage brut d'URL
- [ ] GUI
- [ ] Résultats plus précis (en version bêta)
- [ ] Ouverture automatique des URL découvertes
- [ ] Web Hooks
- [x] Mode sans tête
- [x] Automatisation

# 🍿 Vitrine
Tookie-osint propose une grande variété d'options à utiliser.
Taper -h deux fois affiche le menu d'aide.

![image](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ Besoin d'aide ?
Consultez https://github.com/alfredredbird/tookie-osint/issues ou le WiKi pour obtenir de l'aide.
Vous avez encore besoin d'aide ? Contactez-nous et rejoignez le serveur Discord ci-dessous :D

# 🤔 Vous ne trouvez pas le site Web que vous cherchez ?
Faites une pull request ou un rapport de bogue avec le site et nous l'ajouterons. :D

# 📗 Infos :

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Versions</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Contributeurs</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Articles
Plusieurs articles ont été rédigés sur notre outil. N'hésitez pas à les consulter :D Ces articles appartiennent à leurs propriétaires respectifs.
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

# 🎬 Tutoriels

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 Contact

- Twitter : https://twitter.com/alfredredbird1

# 🛠 Autres outils

Autres outils de la flotte :
- Bibi-Bird (bêta) : https://github.com/alfredredbird/Bibi-Bird


# 🤝 Partenariat
Vous souhaitez vous associer au projet tookie-osint ? N'hésitez pas à nous contacter.


Partenaires :
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT