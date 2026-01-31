![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![Участники GitHub](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![Размер кода GitHub в байтах](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![Форки GitHub](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![Звезды репозитория GitHub](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Стиль кода: черный](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Запустить на Repl.it](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (Нам пришлось провести ребрендинг)

# 🔎 Обзор
Tookie-osint имеет простой в использовании пользовательский интерфейс и очень прост.
Основная идея Tookie-osint - находить имена пользователей, которые запрашиваются из ввода.
Tookie-osint похож на инструмент под названием Sherlock. Он обнаруживает все учетные записи пользователей на разных веб-сайтах, и Tookie-osint успешно справляется с этой задачей почти в 80% случаев.
Наш инструмент был создан мной и сообществом и доступен для вашего использования.
Я не несу ответственности за любые злонамеренные действия и/или ответственность, вызванные моим инструментом. :(
Обратите внимание, что Tookie-osint был создан, чтобы помочь новым программистам или пентестерам войти в мир OSINT. Моя конечная цель - сделать Tookie-osint как можно более совершенным и легким для понимания новыми программистами. Также обратите внимание, что Tookie-osint оптимизирован для Python 3.12. Если вы хотите внести свой вклад, сделайте форк и отправьте запрос на слияние, чтобы отправить свои изменения. :D

<img width="930" height="1056" alt="image" src="https://github.com/user-attachments/assets/da493d67-cde1-4ded-bf7e-af62d14dc016" />


# 📦 Установка
Требования будут установлены автоматически.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 Ручная установка
    скачайте последнюю версию с: https://github.com/alfredredbird/tookie-osint/releases.
    затем извлеките zip или tar.gz

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint




# 📦 Другие установки Linux
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 🖋 Скриптинг с помощью Tookie

Пожалуйста, смотрите [здесь](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie) для получения более подробной информации.



# 💻 Протестированные ОС

<table>
    <tr>
        <th>Операционная система</th>
        <th> Версия </th>
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

# 📖 Требования

Их много, лол

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️Поддерживаемые языки
(нам нужны переводчики 😭)
- [x] Английский
- [x] Итальянский
- [x] Иврит
- [x] Испанский
- [x] Французский
- [x] Арабский
- [x] Немецкий
- [x] Хинди
- [x] Русский
- [x] Португальский
- [X] Индонезийский
- [X] Финский
- [X] Китайский традиционный
- [x] Китайский упрощенный
- [x] Японский
- [x] Фарси

# 📕 Предстоящие функции
 (Это отличные первые выпуски :D)
- [ ] Поиск в Tor (в бета-версии)
- [X] Веб-интерфейс (в бета-версии)
- [X] Веб-скрапер
- [X] OSINT по номеру телефона
- [X] Пользовательские плагины
- [ ] Подробные отчеты (в бета-версии)
- [ ] OSINT по электронной почте (в бета-версии)
- [x] CSV
- [ ] Брутфорс URL
- [ ] Графический интерфейс
- [ ] Более точные результаты (в бета-версии)
- [ ] Автоматически открывать обнаруженные URL
- [ ] Веб-перехватчики
- [x] Режим без головы
- [x] Автоматизация

# 🍿 Витрина
Tookie-osint имеет широкий спектр возможностей для использования.
Двойной ввод -h показывает меню помощи.

![изображение](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ Нужна помощь?
Ознакомьтесь с https://github.com/alfredredbird/tookie-osint/issues или WiKi для получения помощи.
Все еще нужна помощь? Свяжитесь с нами и сервером Discord ниже :D

# 🤔 Не можете найти искомый веб-сайт?
Сделайте запрос на слияние или отчет об ошибке с сайтом, и мы его добавим. :D

# 📗 Информация:

<table>
    <tr>
        <th>Вики</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Релизы</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Участники</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Статьи
О нашем инструменте было написано несколько статей. Не стесняйтесь их проверить :D Эти статьи принадлежат их уважаемым владельцам.
<table>
    <tr>
        <th>Хабр</th>
        <th>https://habr.com/ru/news/757502/</th>
    </tr>
 <tr>
        <th>Хабр</th>
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
        <th>интернет-разведка</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Учебники по Kali Linux</th>
        <th>https://kalilinuxtutorials.com/tookie-osint/</th>
    </tr>
    <tr>
        <th>Hacks.gr</th>
        <th>https://en.hacks.gr/tookie-osint-ergaleio-sullogis-kai-analysis-dimosion-dedomenon/
    </th>
        <tr>
        <th>Джей Джей Галлего</th>
        <th>https://medium.com/cyberscribers-exploring-cybersecurity/osint-for-nicknames-tookie-osint-1364a3c87acf</th>
    </tr>
    </tr>



</table>

# 🎬 Учебные пособия

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 Контакты

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Другие инструменты

Другие инструменты в парке:
- Bibi-Bird (бета): https://github.com/alfredredbird/Bibi-Bird


# 🤝 Партнерство
Хотите сотрудничать с проектом tookie-osint? Не стесняйтесь обращаться к нам.


Партнеры:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT