![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![مشارکت‌کنندگان گیت‌هاب](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![اندازه کد گیت‌هاب بر حسب بایت](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![فورک‌های گیت‌هاب](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![ستاره‌های مخزن گیت‌هاب](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![سبک کد: سیاه](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![دیسکورد](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![اجرا در Repl.it](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (مجبور شدیم برند خود را تغییر دهیم)

# 🔎 نمای کلی
Tookie-osint دارای یک رابط کاربری ساده برای استفاده است و واقعاً ساده است.
ایده اصلی Tookie-osint کشف نام‌های کاربری است که از یک ورودی درخواست می‌شوند.
Tookie-osint شبیه به ابزاری به نام شرلوک است. این ابزار تمام حساب‌های کاربری را در وب‌سایت‌های مختلف کشف می‌کند و Tookie-osint تقریباً در 80٪ موارد در این کار موفق است.
ابزار ما توسط من و جامعه ایجاد شده است و برای استفاده شما در دسترس است.
من هیچ مسئولیتی در قبال هرگونه اقدام مخرب و/یا مسئولیتی که توسط ابزار من ایجاد شود، بر عهده نمی‌گیرم. :(
لطفاً توجه داشته باشید که Tookie-osint برای کمک به برنامه نویسان جدید یا آزمایشگران نفوذ برای ورود به دنیای OSINT ایجاد شده است. هدف نهایی من این است که Tookie-osint را تا حد امکان کامل کنم و درک آن را برای برنامه نویسان جدید آسان کنم. همچنین توجه داشته باشید که Tookie-osint برای پایتون 3.12 بهینه شده است. اگر می‌خواهید مشارکت کنید، یک فورک ایجاد کنید و یک درخواست کشش برای ارسال تغییرات خود ایجاد کنید. :D

<img width="930" height="1056" alt="image" src="https://github.com/user-attachments/assets/da493d67-cde1-4ded-bf7e-af62d14dc016" />


# 📦 نصب
نیازمندی‌ها به طور خودکار نصب می‌شوند.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 نصب دستی
    آخرین نسخه را از اینجا دانلود کنید: https://github.com/alfredredbird/tookie-osint/releases.
    سپس فایل zip یا tar.gz را استخراج کنید

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint




# 📦 سایر نصب‌های لینوکس
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 🖋 اسکریپت‌نویسی با Tookie

لطفاً برای جزئیات بیشتر به [اینجا](https://github.com/Alfredredbird/tookie-osint/wiki/Scripting-Tookie) مراجعه کنید.



# 💻 سیستم عامل‌های آزمایش شده

<table>
    <tr>
        <th>سیستم عامل</th>
        <th> نسخه </th>
    </tr>
    <tr>
        <td>MacOS</td>
        <td> Monterey 12.6.7 </td>
    </tr>
    <tr>
        <td>ویندوز</td>
        <td>11/10</td>
    </tr>
 <tr>
        <td>Termux</td>
        <td>0.118.0</td>
    </tr>
    <tr>
        <td>کالی لینوکس</td>
        <td> Rolling / Sana</td>
    </tr>
    <tr>
        <td>سیستم عامل پارروت</td>
        <td>3.1 </td>
    </tr>
    <tr>
        <td>اوبونتو</td>
        <td>22.04/20.04 </td>
    </tr>
    <tr>
        <td>دبیان</td>
        <td>10.00 </td>
    </tr>
   <tr>
        <td>آلپاین</td>
        <td>3.10 </td>
    </tr>
  <tr>
        <td>فدورا</td>
        <td>v33</td>
    </tr>
  <tr>
        <td>آرچ لینوکس</td>
        <td>2021.07.01</td>
    </tr>
  <tr>
        <td>مانجارو</td>
        <td>21</td>
    </tr>
   <tr>
        <td>Void</td>
        <td>نسخه غلطان</td>
    </tr>
</table>

# 📖 نیازمندی‌ها

خیلی زیاده خخخ

- colorama
- requests
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography

# 🗣️زبان‌های پشتیبانی شده
(به مترجم نیاز داریم 😭)
- [x] انگلیسی
- [x] ایتالیایی
- [x] عبری
- [x] اسپانیایی
- [x] فرانسوی
- [x] عربی
- [x] آلمانی
- [x] هندی
- [x] روسی
- [x] پرتغالی
- [X] اندونزیایی
- [X] فنلاندی
- [X] چینی سنتی
- [x] چینی ساده شده
- [x] ژاپنی
- [x] فارسی

# 📕 ویژگی‌های آینده
 (آنها مسائل اولیه عالی هستند :D)
- [ ] جستجوی Tor (در نسخه بتا)
- [X] رابط کاربری وب (در نسخه بتا)
- [X] وب اسکرپر
- [X] شماره تلفن OSINT
- [X] افزونه‌های سفارشی
- [ ] گزارش‌های دقیق (در نسخه بتا)
- [ ] ایمیل OSINT (در نسخه بتا)
- [x] CSV
- [ ] حملات جستجوی فراگیر URL
- [ ] رابط کاربری گرافیکی
- [ ] نتایج دقیق‌تر (در نسخه بتا)
- [ ] باز کردن خودکار URL‌های کشف شده
- [ ] وب هوک
- [x] حالت بدون سر
- [x] اتوماسیون

# 🍿 ویترین
Tookie-osint طیف گسترده‌ای از گزینه‌ها را برای استفاده دارد.
تایپ کردن -h دو بار منوی راهنما را نشان می‌دهد.

![تصویر](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


# ⁉️ به کمک نیاز دارید؟
برای راهنمایی به https://github.com/alfredredbird/tookie-osint/issues یا WiKi مراجعه کنید.
هنوز به کمک نیاز دارید؟ تماس و سرور دیسکورد در زیر :D

# 🤔 وب‌سایتی را که به دنبال آن هستید پیدا نمی‌کنید؟
یک درخواست کشش یا گزارش اشکال با سایت ایجاد کنید و ما آن را اضافه خواهیم کرد. :D

# 📗 اطلاعات:

<table>
    <tr>
        <th>ویکی</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>نسخه‌ها</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>مشارکت‌کنندگان</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 مقالات
چندین مقاله در مورد ابزار ما نوشته شده است. با خیال راحت آنها را بررسی کنید :D این مقالات متعلق به صاحبان محترم آنها است.
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
        <th>اطلاعات اینترنتی</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>آموزش‌های کالی لینوکس</th>
        <th>https://kalilinuxtutorials.com/tookie-osint/</th>
    </tr>
    <tr>
        <th>Hacks.gr</th>
        <th>https://en.hacks.gr/tookie-osint-ergaleio-sullogis-kai-analysis-dimosion-dedomenon/
    </th>
        <tr>
        <th>جی جی گالگو</th>
        <th>https://medium.com/cyberscribers-exploring-cybersecurity/osint-for-nicknames-tookie-osint-1364a3c87acf</th>
    </tr>
    </tr>



</table>

# 🎬 آموزش‌ها

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
# 📘 تماس

- توییتر: https://twitter.com/alfredredbird1

# 🛠 سایر ابزارها

سایر ابزارهای موجود در ناوگان:
- Bibi-Bird (بتا): https://github.com/alfredredbird/Bibi-Bird


# 🤝 مشارکت
آیا می‌خواهید با پروژه tookie-osint شریک شوید؟ با خیال راحت تماس بگیرید.


شرکا:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT