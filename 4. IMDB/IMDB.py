import requests
from bs4 import BeautifulSoup
import csv

headers = {'Accept-Language': 'en-US'}
website = requests.get('https://www.imdb.com/title/tt0770828/', headers=headers)
soup = BeautifulSoup(website.text, 'html.parser')
title = soup.select_one('.title_wrapper > h1').contents[0].strip()
runtime = soup.select_one('time').text.strip()
plot = soup.select_one('.summary_text').text.strip()
rating = soup.find(attrs={'itemprop': 'ratingValue'}).text
rating_count = soup.find(attrs={'itemprop': 'ratingCount'}).text
cast_list = soup.select('.cast_list tr')[1:5]
cast = ''
for item in cast_list:
	cast += item.select('td')[1].text.strip() + ', '
print(f'{title}\n{runtime}\n{plot}\n{rating}\n{rating_count}\n{cast}')