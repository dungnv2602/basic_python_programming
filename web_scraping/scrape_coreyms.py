from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

pattern = re.compile(r'\/(\w+)\?')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']

    matched = pattern.search(vid_src)

    if matched:
        vid_id = matched.group(1)
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    else:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
