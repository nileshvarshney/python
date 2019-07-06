from bs4 import BeautifulSoup
import urllib3

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string) # The Dormouse's story 
print(soup.title.parent.name) # head
print(soup.head.parent.name)  # html

print(soup.p['class'])
print(soup.p.string)

print(soup.a['class'])

print('*'*80)
print(soup.find_all('p'))

print('*'*120)
print(soup.find(id="link3"))

# find all URLs
print('*'*120)
for link in soup.find_all("a"):
    print(link.get("href"))

# get all text
print('*'*120)
print(soup.get_text())