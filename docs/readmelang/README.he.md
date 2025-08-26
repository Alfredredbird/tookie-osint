![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![תורמי GitHub](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![גודל קוד GitHub בבתים](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![פיצולים ב-GitHub](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![כוכבי מאגר GitHub](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![סגנון קוד: שחור](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![דיסקורד](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![הפעל ב-Repl.it](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (היינו צריכים למתג מחדש)

# 🔎 סקירה כללית
ל-Tookie-osint יש ממשק משתמש פשוט לשימוש והוא ממש פשוט.
הרעיון המרכזי של Tookie-osint הוא לגלות שמות משתמש המבוקשים מקלט.
Tookie-osint דומה לכלי שנקרא שרלוק. הוא מגלה את כל חשבונות המשתמשים באתרי אינטרנט שונים ו-Tookie-osint מצליח במשימה זו כמעט 80% מהזמן.
הכלי שלנו נוצר על ידי ועל ידי הקהילה וזמין לשימושך.
אני לא לוקח אחריות על כל פעולה זדונית ו/או אחריות שנגרמה על ידי הכלי שלי. :(
שימו לב ש-Tookie-osint נוצר כדי לעזור למתכנתים חדשים או לבודקי חדירות להיכנס לעולם ה-OSINT. המטרה הסופית שלי היא להפוך את Tookie-osint למושלם ככל האפשר ולהקל על מתכנתים חדשים להבין אותו. שימו לב גם ש-Tookie-osint מותאם לפייתון 3.12. אם ברצונך לתרום, צור פיצול ובצע בקשת משיכה כדי להגיש את השינויים שלך. :D

<img width="952" height="1300" alt="image" src="https://github.com/user-attachments/assets/fea15d7b-1e6d-44d7-b444-aefa56bcc6b2" />


# 📦 התקנה
הדרישות יותקנו אוטומטית.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint

# 📦 התקנה ידנית
    הורד את המהדורה האחרונה מ: https://github.com/alfredredbird/tookie-osint/releases.
    לאחר מכן חלץ את ה-zip או tar.gz

    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint


# 📦 התקנת Termux

    termux-setup-storage
    ln -s storage/downloads Downloads

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

# 📦 התקנות לינוקס אחרות
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 tookie-osint


# 🖋 סקריפטים עם Tookie

אנא עיין [כאן](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie) לפרטים נוספים.



# 💻 מערכות הפעלה שנבדקו

<table>
    <tr>
        <th>מערכת הפעלה</th>
        <th> גרסה </th>
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
        <td>אובונטו</td>
        <td>22.04/20.04 </td>
    </tr>
    <tr>
        <td>דביאן</td>
        <td>10.00 </td>
    </tr>
   <tr>
        <td>אלפיין</td>
        <td>3.10 </td>
    </tr>
  <tr>
        <td>פדורה</td>
        <td>v33</td>
    </tr>
  <tr>
        <td>Arch Linux</td>
        <td>2021.07.01</td>
    </tr>
  <tr>
        <td>מנג'רו</td>
        <td>21</td>
    </tr>
   <tr>
        <td>Void</td>
        <td>מהדורה מתגלגלת</td>
    </tr>
</table>

# 📖 דרישות

יש הרבה חחח

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️שפות נתמכות
(אנחנו צריכים מתרגמים 😭)
- [x] אנגלית
- [x] איטלקית
- [x] עברית
- [x] ספרדית
- [x] צרפתית
- [x] ערבית
- [x] גרמנית
- [x] הינדי
- [x] רוסית
- [x] פורטוגזית
- [X] אינדונזית
- [X] פינית
- [X] סינית מסורתית
- [x] סינית מפושטת
- [x] יפנית
- [x] פרסית

# 📕 תכונות עתידיות
 (הם נושאים ראשונים נהדרים :D)
- [ ] חיפוש ב-Tor (בבטא)
- [X] ממשק משתמש אינטרנטי (בבטא)
- [X] מגרד אינטרנט
- [X] OSINT של מספר טלפון
- [X] תוספים מותאמים אישית
- [ ] דוחות מפורטים (בבטא)
- [ ] OSINT בדוא"ל (בבטא)
- [x] CSV
- [ ] כוח גס של כתובות אתרים
- [ ] ממשק משתמש גרפי
- [ ] תוצאות מדויקות יותר (בבטא)
- [ ] פתיחה אוטומטית של כתובות אתרים שהתגלו
- [ ] Web Hooks
- [x] מצב ללא ראש
- [x] אוטומציה

# 🍿 תצוגה
ל-Tookie-osint יש מגוון רחב של אפשרויות לשימוש.
הקלדת -h פעמיים מציגה את תפריט העזרה.

![תמונה](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ זקוק לעזרה?
בדוק את https://github.com/alfredredbird/tookie-osint/issues או את ה-WiKi לקבלת עזרה.
עדיין זקוק לעזרה? צור קשר ושרת דיסקורד למטה :D

# 🤔 לא מוצא את האתר שאתה מחפש?
צור בקשת משיכה או דוח באג עם האתר ונוסיף אותו. :D

# 📗 מידע:

<table>
    <tr>
        <th>ויקי</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>מהדורות</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>תורמים</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 מאמרים
נכתבו מספר מאמרים על הכלי שלנו. אל תהסס לבדוק אותם :D מאמרים אלה שייכים לבעליהם המכובדים.
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

# 🎬 הדרכות

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 יצירת קשר

- טוויטר: https://twitter.com/alfredredbird1

# 🛠 כלים אחרים

כלים אחרים בצי:
- Bibi-Bird (בטא): https://github.com/alfredredbird/Bibi-Bird


# 🤝 שותפות
רוצה להיות שותף בפרויקט tookie-osint? אל תהסס לפנות אלינו.


שותפים:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT