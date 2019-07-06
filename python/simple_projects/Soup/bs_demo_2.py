from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("https://timesofindia.indiatimes.com/")

soup = BeautifulSoup(page,'html.parser')
print(soup.prettify())
#
# print(soup.find_all('a').title)
