from datetime import datetime
import time
import json
import re
import requests
from bs4 import BeautifulSoup
import os

def report(urls,uname):
    # Ensure the reports directory exists
    if not os.path.exists('./reports'):
        os.makedirs('./reports')
    
    # Define the report file path
    report_file_path = f'./reports/{uname}.txt'

    with open(report_file_path, 'w', encoding='utf-8') as report_file:
        for url in urls:
            # Headers to mimic a browser request
            current_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
            device_type = "mobile"
            
            headers = {
                "User-Agent": "Your User Agent String",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Referer": "http://example.com",
                "Cache-Control": "max-age=0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Date": current_date,
                "Device-Type": device_type,
            }
            try:
             # Make a request to the website
             response = requests.get(url, headers=headers)

             # Check if the request was successful
             if response.status_code == 200 or response.status_code == 403:
                 # Parse the HTML content using BeautifulSoup
                 soup = BeautifulSoup(response.content, 'lxml')

                 if "facebook" in url:
                     title_tag = soup.find('title')
                     if title_tag:
                         title_text = title_tag.get_text(strip=True)
                         report_file.write(f"Username for Facebook: {title_text}\n")
                     else:
                         report_file.write(f"The specified <title> tag was not found for {url}.\n")

                 elif "instagram" in url:
                     title_tag = soup.find('title')
                     if title_tag:
                         title_text = title_tag.get_text(strip=True)
                         report_file.write(f"Username for Instagram: {title_text.replace('• Instagram photos and videos', '')}\n")
                     else:
                         report_file.write(f"The specified <title> tag was not found for {url}.\n")

                 elif "youtube" in url:
                     title_tag = soup.find('title')
                     if title_tag:
                         title_text = title_tag.get_text(strip=True)
                         report_file.write(f"Username for YouTube: {title_text.replace('- YouTube', '')}\n")
                     else:
                         report_file.write(f"The specified <title> tag was not found for {url}.\n")

                     script_tags = soup.find_all('script')
                     for script in script_tags:
                         if 'ytInitialData' in script.text:
                             json_str = re.search(r'ytInitialData\s*=\s*({.*?});', script.text).group(1)
                             data = json.loads(json_str)

                             try:
                                 subscriber_count = data['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']
                                 report_file.write(f"Subscriber Count: {subscriber_count}\n")
                             except KeyError:
                                 report_file.write("Subscriber count not found in the JSON data.\n")

                             try:
                                 videos_count = data['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']
                                 report_file.write(f"Videos Count: {videos_count}\n")
                             except KeyError:
                                 report_file.write("Videos count not found in the JSON data.\n")
                             break

                 elif "x" in url:
                     name_tag = soup.find('span', class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3')
                     handle_tag = soup.find('span', class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3')
                     if name_tag and handle_tag:
                         name_text = name_tag.get_text(strip=True)
                         handle_text = handle_tag.get_text(strip=True)
                         report_file.write(f"Twitter Name: {name_text}\n")
                         report_file.write(f"Twitter Handle: {handle_text}\n")
                     else:
                         report_file.write("The specified tags were not found for Twitter.\n")

                 if "twitch.tv" in url:
                     twitch_title_meta = soup.find('meta', attrs={'name': "twitter:title"})
                     if twitch_title_meta and 'content' in twitch_title_meta.attrs:
                         report_file.write(f"Twitch name: {twitch_title_meta['content'].replace('- Twitch', '')}\n")
                     else:
                         report_file.write(f"Could not find the specified twitter title tag for {url}.\n")
                     description_meta = soup.find('meta', attrs={'property': "og:description"})
                     if description_meta and 'content' in description_meta.attrs:
                         report_file.write(f"Twitch Bio: {description_meta['content']}\n")
                     else:
                         report_file.write(f"Could not find the specified meta description tag for {url}.\n")

             else:
                 report_file.write(f"Failed to retrieve the webpage. Status code: {response.status_code} for {url}\n")

             report_file.write("================\n")
            except Exception as e:
                print("Error occurred with this site, skipping.....")

def extract_urls(file_path):
    urls = []
    url_pattern = re.compile(r'https?://[^\s]+')  
    with open(file_path, 'r') as file:
        for line in file:
            match = url_pattern.search(line)
            if match:
                urls.append(match.group())
    
    return urls