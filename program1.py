# Import requests so we can make HTTP/HTTPS requests (get web pages)
import requests
# Import Beautiful Soup 4 for HTML parsing
from bs4 import BeautifulSoup

# Use the "get method" to get the URL with the requests library
r = requests.get("https://scrapethissite.com/pages/simple")

# Use Beautiful Soup 4 to parse the response HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Print out the parsed HTML of the page
#print(soup)

print(soup.find('title'))


countries = soup.find_all('div', 'country')
#print(countries)


for text_only in countries:
	print(text_only.text.strip())


"""
for country in countries:
	name = country.find('h3').text.strip()
	capital = country.find('span', 'country-capital').text.strip()
	population = country.find('span', 'country-population').text.strip()
	area = country.find('span', 'country-area').text.strip()
	print("{} has a capital city of {}, a population of {} and an area of {}".format(name, capital, population, area))
"""