from bs4 import BeautifulSoup
import requests

website = requests.get('https://coinmarketcap.com/currencies/lto-network/')

soup = BeautifulSoup(website.content, 'html.parser')

my_classes = soup.find(class_ = 'sc-16r8icm-0 fIhwvd')

for string in my_classes.strings:
    print(string)

 

