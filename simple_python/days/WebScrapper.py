import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/trivia-champion-books"
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# get class elements 
tier_headlines = soup.select(".dd-header-headline")

stripped_tiers = [ tier.text.strip() for tier in  tier_headlines]
# print(stripped_tiers)


# # data structure format
# tiers = {
#     "tier1": {
#         "price"     : 500,
#         "product"   : ["Name 1","Name 2"] 
#     },
#     "tier2": {
#         "price"     : 500,
#         "product"   : ["Name 1","Name 2"] 
#     }
# }

# # General Format
# for tiername, tierinfo in tiers.items():
#     print(tiername.upper())
#     print('Price at ',tierinfo['price'])
#     print('Product',', '.join(tierinfo['product']))
#     print("\n\n")

# Products
products = soup.select(".dd-image-box-caption")
product_lists = [ tier.text.strip() for tier in  products]

# Get rid of 'Support Charity', ''
price_list = [name.split()[1] for name in stripped_tiers if name.startswith("Pay")]
\
tiers = soup.select(".main-content-row")
for tier in  tiers:
    if tier.select(".dd-header-headline"):
        headlines = tier.select(".dd-header-headline")
        tier_names = [headline.text.strip() for headline in headlines]
        if len(tier_names) > 1:
            tier_names = []
            break
        else:
            if tier.select(".dd-image-box-caption"):
                titles = tier.select(".dd-image-box-caption")
                product_names = [title.text.strip() for title in titles]

    print(tier_names)
    print(product_names)
