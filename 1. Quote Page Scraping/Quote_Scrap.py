import requests
from bs4 import BeautifulSoup

page = 1
next_button = True
while next_button:
    website = requests.get('https://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
    next_button = soup.select_one('.next > a')
    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tag')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text)
        print("***********************************************************")
    print('Scraped Page' + str(page))
    page += 1