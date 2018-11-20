#!/usr/bin/python3

# Program outputs all countries from the first page of http://example.webscraping.com/

def country_search(webscraping_page, country_value_start_index, country_tag, country_tag_size):
	"""Find and output names of countries"""

	country_tag_index = webscraping_page.find(country_tag, country_value_start_index)
	country_value_start_index = country_tag_index + country_tag_size
	country = ''
	for char in webscraping_page[country_value_start_index:]:
		if char != '<':
			country += char
		else:
			break
	country = country[10:]
	if country != '':
		print(country)
		country_search(webscraping_page, country_value_start_index, country_tag, country_tag_size)



from urllib.request import urlopen, Request
webscraping_url = 'http://example.webscraping.com/'

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
webscraping_request = Request(webscraping_url, headers=headers)
webscraping_page = urlopen(webscraping_request).read()
webscraping_page = webscraping_page.decode('utf-8')

# define country tag
country_tag = '/places/static/images/flags/'
country_tag_size = len(country_tag)
country_value_start_index = 0

country_search(webscraping_page, country_value_start_index, country_tag, country_tag_size)