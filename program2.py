import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    countriesname = soup.find_all('h3', class_='country-name')
    type(countriesname)
    for name in countriesname:
        print(name.text.strip())


        