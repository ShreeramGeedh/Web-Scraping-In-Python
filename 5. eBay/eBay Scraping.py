import csv
import requests
from bs4 import BeautifulSoup
from decimal import Decimal

query = input('Enter product: ')
free_shipping = input('Enter free shipping: ')
max_price = Decimal(input('Enter maximum price: '))
for i in range(1, 5):
	website = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + query +'&_pgn=' + str(i)).text
	soup = BeautifulSoup(website, 'html.parser')
	items = soup.select('.srp-results .s-item')
	for item in items:
		title = item.h3.text
		price = item.select_one('.s-item__price').text
		shipping = item.select_one('.s-item__shipping').text
		price_decimal = Decimal(price.split(' to ')[0][1:])
		if price_decimal <= max_price:
			if free_shipping == 'y':
				if 'Free' in shipping:
					print(f'{title}\n{price}\n{shipping}')
					print('=================================')
			else:
				print(f'{title}\n{price}\n{shipping}')
				print('=================================')