![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub contributors](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub forks](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub Repo stars](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Discord](https://img.shields.io/discord/1229923929959960616?logo=discord&color=%237289da&link=https%3A%2F%2Fdiscord.gg%2F2WvtfwQjVc)


[![Run on Repl.it](https://replit.com/badge/github/alfredredbird/tookie-osint)](https://replit.com/new/github/alfredredbird/tookie-osint)

# (We Had To Rebrand)

# 🔎 Overview 
Tookie-osint has a simple-to-use UI and is really straightforward. 
The main idea of Tookie-osint is to discover usernames that are requested from an input.
Tookie-osint is similar to the tool called Sherlock. It discovers all the user accounts across different websites and Tookie-osint is successful at this task almost 80% of the time.
Our tool was created by me and the community and is available for your use. 
I do not take responsibility for any malicious actions and/or responsibility caused by my tool. :(
Please note that Tookie-osint was created to help new programmers or pentesters get into the world of OSINT. My end term goal is to make Tookie-osint as perfect as I can and make it easy for new programmers to understand. Also take note that Tookie-osint is optimized for Python 3.12. If you want to contribute, make a fork and make a pull request to submit your changes. :D 

![image](https://github.com/Alfredredbird/tookie-osint/assets/105014217/380da10a-ff65-4137-a213-7bdd0dfdb9ed)


# 📦 Installation
The requirements will be automatically installed.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint

# 📦 Manual Install 
    download the latest release from: https://github.com/alfredredbird/tookie-osint/releases.
    then extract the zip or tar.gz
    
    cd tookie-osint && sudo pip3 install -r requirements.txt
    python3 tookie-osint


# 📦 Termux Install
    
    termux-setup-storage
    ln -s storage/downloads Downloads
    
    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint && pip3 install -r requirements.txt

    python3 tookie-osint

---

# 📦 Automate Tookie-OSINT using scripts or scheduling tools.

### Using a Bash Script
You can create a bash script to run Tookie-OSINT with predefined usernames and options. Here's an example:

1. **Create a Script**: Save the following script as `automate_tookie.sh`:

    ```bash
    #!/bin/bash

    # List of usernames to search
    usernames=("john_doe" "jane_doe" "example_user")

    # Loop through each username and run Tookie-OSINT
    for username in "${usernames[@]}"
    do
        echo "Searching for $username"
        python3 brib.py --username "$username" --site twitter,facebook
    done
    ```

2. **Make the Script Executable**:

    ```bash
    chmod +x automate_tookie.sh
    ```

3. **Run the Script**:

    ```bash
    ./automate_tookie.sh
    ```

### Using Cron Jobs (Linux/Mac)
You can schedule the script to run at specific intervals using cron jobs:

1. **Edit Crontab**:

    ```bash
    crontab -e
    ```

2. **Add a Cron Job**: Add the following line to run the script daily at midnight:

    ```bash
    0 0 * * * /path/to/automate_tookie.sh
    ```

### Using Task Scheduler (Windows)
For Windows, you can use Task Scheduler to automate the script:

1. **Create a Batch File**: Save the following as `automate_tookie.bat`:

    ```batch
    @echo off
    python C:\path\to\brib.py --username john_doe --site twitter,facebook
    python C:\path\to\brib.py --username jane_doe --site twitter,facebook
    ```

2. **Schedule the Task**:
    - Open Task Scheduler.
    - Create a new task.
    - Set the trigger to your desired schedule.
    - Set the action to run the batch file.

### Using Python Script
You can also automate it directly within a Python script:

```python
import os
import time

# List of usernames to search
usernames = ["john_doe", "jane_doe", "example_user"]

# Function to run Tookie-OSINT
def run_tookie(username):
    os.system(f"python3 brib.py --username {username} --site twitter,facebook")

# Loop through each username and run Tookie-OSINT
for username in usernames:
    print(f"Searching for {username}")
    run_tookie(username)
    time.sleep(10)  # Add delay if needed
```

You can schedule this Python script using cron jobs or Task Scheduler as described above.

These methods should help you automate Tookie-OSINT effectively.

---

# 📦 Running Tookie-OSINT in Headless Mode

1. **Install Tookie-OSINT**:
   First, ensure you have Tookie-OSINT installed. If not, follow these steps:

   ```bash
   git clone https://github.com/Alfredredbird/tookie-osint.git
   cd tookie-osint
   pip3 install -r requirements.txt
   ```

2. **Create a Configuration File**:
   You can create a configuration file to store your usernames and options. For example, create a file named `config.txt`:

   ```plaintext
   john_doe --site twitter,facebook
   jane_doe --site instagram,linkedin
   ```

3. **Modify the Script to Read from the Configuration File**:
   Create a Python script named `headless_tookie.py` to read from the configuration file and run Tookie-OSINT:

   ```python
   import os

   # Read the configuration file
   with open('config.txt', 'r') as file:
       lines = file.readlines()

   # Loop through each line in the configuration file
   for line in lines:
       username, options = line.strip().split(' ', 1)
       command = f"python3 brib.py --username {username} {options}"
       os.system(command)
   ```

4. **Run the Script**:
   Execute the script to run Tookie-OSINT in headless mode:

   ```bash
   python3 headless_tookie.py
   ```

### Example Configuration File
Here’s an example of what your `config.txt` might look like:

```plaintext
john_doe --site twitter,facebook
jane_doe --site instagram,linkedin
example_user --site github,reddit
```

### Automating with Cron Jobs (Linux/Mac) or Task Scheduler (Windows)
You can schedule the `headless_tookie.py` script to run at specific intervals using cron jobs or Task Scheduler:

- **Cron Job**:
  ```bash
  crontab -e
  ```

  Add the following line to run the script daily at midnight:
  ```bash
  0 0 * * * /usr/bin/python3 /path/to/headless_tookie.py
  ```

- **Task Scheduler**:
  - Open Task Scheduler.
  - Create a new task.
  - Set the trigger to your desired schedule.
  - Set the action to run the Python script.

This setup allows you to run Tookie-OSINT in headless mode, automating the process without manual intervention.

---

# 📦 Customizing Output Format

1. **Modify the Script**:
   Open the `brib.py` script (or the main script you are using) and locate the section where the results are printed or saved. You can customize this part to format the output as needed.

2. **Example: JSON Output**:
   If you want to output the results in JSON format, you can use the `json` module in Python. Here’s an example of how to modify the script:

   ```python
   import json

   # Example result data
   results = {
       "username": "john_doe",
       "sites": {
           "twitter": "https://twitter.com/john_doe",
           "facebook": "https://facebook.com/john_doe"
       }
   }

   # Convert results to JSON format
   json_output = json.dumps(results, indent=4)

   # Save to a file
   with open('results.json', 'w') as file:
       file.write(json_output)
   ```

3. **Example: CSV Output**:
   If you prefer CSV format, you can use the `csv` module. Here’s an example:

   ```python
   import csv

   # Example result data
   results = [
       {"username": "john_doe", "site": "twitter", "url": "https://twitter.com/john_doe"},
       {"username": "john_doe", "site": "facebook", "url": "https://facebook.com/john_doe"}
   ]

   # Define CSV file headers
   headers = ["username", "site", "url"]

   # Write results to CSV file
   with open('results.csv', 'w', newline='') as file:
       writer = csv.DictWriter(file, fieldnames=headers)
       writer.writeheader()
       writer.writerows(results)
   ```

4. **Example: HTML Output**:
   For HTML output, you can use basic HTML formatting. Here’s an example:

   ```python
   # Example result data
   results = {
       "username": "john_doe",
       "sites": {
           "twitter": "https://twitter.com/john_doe",
           "facebook": "https://facebook.com/john_doe"
       }
   }

   # Create HTML content
   html_content = f"""
   <html>
   <head><title>OSINT Results</title></head>
   <body>
       <h1>Results for {results['username']}</h1>
       <ul>
           <li>Twitter: <a href="{results['sites']['twitter']}">{results['sites']['twitter']}</a></li>
           <li>Facebook: <a href="{results['sites']['facebook']}">{results['sites']['facebook']}</a></li>
       </ul>
   </body>
   </html>
   """

   # Save to an HTML file
   with open('results.html', 'w') as file:
       file.write(html_content)
   ```

### Automating the Custom Output
You can integrate these modifications into your automation script to ensure the output is always in your desired format. For example, you can update the `headless_tookie.py` script to include the custom output formatting.

---

# 📦 Customizing Output for Specific Sites

1. **Identify the Additional Information**:
   Determine what extra details you want to include in the output for each social media site. For example, you might want to add follower counts, account creation dates, or specific metadata.

2. **Modify the Script**:
   Open the `brib.py` script (or the main script you are using) and locate the section where the results are processed. Add code to handle each site separately.

### Example: Customizing JSON Output for Specific Sites

Here’s an example of how to modify the script to customize the JSON output for Twitter, Facebook, and Instagram:

```python
import json
import datetime

# Example result data
results = {
    "username": "john_doe",
    "search_time": str(datetime.datetime.now()),
    "search_parameters": {
        "sites": ["twitter", "facebook", "instagram"]
    },
    "accounts_found": {
        "twitter": {
            "url": "https://twitter.com/john_doe",
            "followers": 1500,
            "account_creation_date": "2010-05-15"
        },
        "facebook": {
            "url": "https://facebook.com/john_doe",
            "friends": 300,
            "account_creation_date": "2009-08-20"
        },
        "instagram": {
            "url": "https://instagram.com/john_doe",
            "followers": 2000,
            "account_creation_date": "2012-03-10"
        }
    }
}

# Customizing output for specific sites
custom_output = {}

if "twitter" in results["accounts_found"]:
    custom_output["twitter"] = {
        "profile_url": results["accounts_found"]["twitter"]["url"],
        "followers_count": results["accounts_found"]["twitter"]["followers"],
        "created_on": results["accounts_found"]["twitter"]["account_creation_date"]
    }

if "facebook" in results["accounts_found"]:
    custom_output["facebook"] = {
        "profile_url": results["accounts_found"]["facebook"]["url"],
        "friends_count": results["accounts_found"]["facebook"]["friends"],
        "created_on": results["accounts_found"]["facebook"]["account_creation_date"]
    }

if "instagram" in results["accounts_found"]:
    custom_output["instagram"] = {
        "profile_url": results["accounts_found"]["instagram"]["url"],
        "followers_count": results["accounts_found"]["instagram"]["followers"],
        "created_on": results["accounts_found"]["instagram"]["account_creation_date"]
    }

# Convert custom output to JSON format
json_output = json.dumps(custom_output, indent=4)

# Save to a file
with open('custom_results.json', 'w') as file:
    file.write(json_output)
```

### Example: Customizing CSV Output for Specific Sites

If you prefer CSV format, you can customize the output for specific sites as follows:

```python
import csv

# Example result data
results = [
    {"username": "john_doe", "site": "twitter", "url": "https://twitter.com/john_doe", "followers": 1500, "account_creation_date": "2010-05-15"},
    {"username": "john_doe", "site": "facebook", "url": "https://facebook.com/john_doe", "friends": 300, "account_creation_date": "2009-08-20"},
    {"username": "john_doe", "site": "instagram", "url": "https://instagram.com/john_doe", "followers": 2000, "account_creation_date": "2012-03-10"}
]

# Define CSV file headers
headers = ["username", "site", "url", "followers/friends", "account_creation_date"]

# Write results to CSV file
with open('custom_results.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for result in results:
        if result["site"] == "twitter":
            writer.writerow({
                "username": result["username"],
                "site": result["site"],
                "url": result["url"],
                "followers/friends": result["followers"],
                "account_creation_date": result["account_creation_date"]
            })
        elif result["site"] == "facebook":
            writer.writerow({
                "username": result["username"],
                "site": result["site"],
                "url": result["url"],
                "followers/friends": result["friends"],
                "account_creation_date": result["account_creation_date"]
            })
        elif result["site"] == "instagram":
            writer.writerow({
                "username": result["username"],
                "site": result["site"],
                "url": result["url"],
                "followers/friends": result["followers"],
                "account_creation_date": result["account_creation_date"]
            })
```

### Automating the Custom Output

You can integrate these modifications into your automation script to ensure the output is always customized for specific sites. For example, update the `headless_tookie.py` script to include the custom output formatting.

---

# 📦 Adding Custom Tags or Labels

1. **Identify the Criteria**:
   Determine the criteria for adding custom tags or labels. For example, you might want to tag accounts with a high number of followers or accounts created before a certain date.

2. **Modify the Script**:
   Open the `brib.py` script (or the main script you are using) and locate the section where the results are processed. Add code to evaluate the criteria and assign tags or labels accordingly.

### Example: Adding Custom Tags in JSON Output

Here’s an example of how to modify the script to add custom tags based on follower count and account creation date:

```python
import json
import datetime

# Example result data
results = {
    "username": "john_doe",
    "search_time": str(datetime.datetime.now()),
    "search_parameters": {
        "sites": ["twitter", "facebook", "instagram"]
    },
    "accounts_found": {
        "twitter": {
            "url": "https://twitter.com/john_doe",
            "followers": 1500,
            "account_creation_date": "2010-05-15"
        },
        "facebook": {
            "url": "https://facebook.com/john_doe",
            "friends": 300,
            "account_creation_date": "2009-08-20"
        },
        "instagram": {
            "url": "https://instagram.com/john_doe",
            "followers": 2000,
            "account_creation_date": "2012-03-10"
        }
    }
}

# Customizing output with tags
custom_output = {}

for site, data in results["accounts_found"].items():
    tags = []
    if site == "twitter" and data["followers"] > 1000:
        tags.append("high_followers")
    if site == "facebook" and data["friends"] > 500:
        tags.append("popular")
    if datetime.datetime.strptime(data["account_creation_date"], "%Y-%m-%d") < datetime.datetime(2015, 1, 1):
        tags.append("veteran")

    custom_output[site] = {
        "profile_url": data["url"],
        "followers/friends": data.get("followers", data.get("friends")),
        "created_on": data["account_creation_date"],
        "tags": tags
    }

# Convert custom output to JSON format
json_output = json.dumps(custom_output, indent=4)

# Save to a file
with open('custom_results.json', 'w') as file:
    file.write(json_output)
```

### Example: Adding Custom Labels in CSV Output

If you prefer CSV format, you can customize the output to include labels as follows:

```python
import csv
import datetime

# Example result data
results = [
    {"username": "john_doe", "site": "twitter", "url": "https://twitter.com/john_doe", "followers": 1500, "account_creation_date": "2010-05-15"},
    {"username": "john_doe", "site": "facebook", "url": "https://facebook.com/john_doe", "friends": 300, "account_creation_date": "2009-08-20"},
    {"username": "john_doe", "site": "instagram", "url": "https://instagram.com/john_doe", "followers": 2000, "account_creation_date": "2012-03-10"}
]

# Define CSV file headers
headers = ["username", "site", "url", "followers/friends", "account_creation_date", "tags"]

# Write results to CSV file
with open('custom_results.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for result in results:
        tags = []
        if result["site"] == "twitter" and result["followers"] > 1000:
            tags.append("high_followers")
        if result["site"] == "facebook" and result["friends"] > 500:
            tags.append("popular")
        if datetime.datetime.strptime(result["account_creation_date"], "%Y-%m-%d") < datetime.datetime(2015, 1, 1):
            tags.append("veteran")

        writer.writerow({
            "username": result["username"],
            "site": result["site"],
            "url": result["url"],
            "followers/friends": result.get("followers", result.get("friends")),
            "account_creation_date": result["account_creation_date"],
            "tags": ", ".join(tags)
        })
```

### Automating the Custom Output

You can integrate these modifications into your automation script to ensure the output is always customized with tags or labels based on site-specific criteria. For example, update the `headless_tookie.py` script to include the custom output formatting.

---

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
- richconsole
- alive_progress
- torrequest
- tqdm
- bs4
- selenium
- cryptography
  
# 🗣️Supported Languages
(we need translators 😭)
- [x] English
- [x] Italian
- [x] Hebrew 
- [x] Spanish
- [x] French 
- [x] Arabic
- [x] German
- [x] Hindi
- [x] Russian
- [x] Portuguese

# 📕 Upcoming Features
 (They Are Great First Issues :D)
- [ ] Tor Searching (in beta)
- [X] WebUi (in beta)
- [X] Webscraper
- [X] Phone Number OSINT
- [X] Custom Plugins
- [ ] Detailed Reports (in beta)
- [x] CSV
- [x] JSON
- [x] HTML
- [ ] Url Brute Forcing
- [ ] GUI
- [ ] More Acurate Results (in beta)
- [ ] Auto Open Descovered URLs
- [ ] Web Hooks
- [x] Headless mode
- [x] Automation

# 🍿 Showcase
Tookie-osint has a wide variety of options to use.
Typing -h twice shows the help menu.

![image](https://github.com/Alfredredbird/tookie-osint/assets/105014217/7429b51c-e021-4bbb-8596-676240bce573)


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
    
  
  

 
</table>

# 🎬 Tutorials

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s

# 📘 Contact

- Twitter: https://twitter.com/alfredredbird1
- LinkedIn: https://www.linkedin.com/in/jeffrey-montanari-7178a1290/




# 🤝 Partnership
Want to partner with the tookie-osint project? Feel free to reach out.


Partners:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT
