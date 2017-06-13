import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup

# Technics.
url="https://www.amazon.com/Monitors-Computers-Accessories/b/?node=1292115011"

# Indian musical instruments.
#url="http://www.amazon.in/b/ref=sv_in-mi_5?ie=UTF8&node=4581270031"

# add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

response_ = requests.get(url, headers=headers)
soup_ = BeautifulSoup(response_.text, 'html.parser')

product_links = (tag.get('href') for tag in soup_.select('.s-result-item .s-access-detail-page'))

def get_product_info(url):
    data = dict()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    data["link"] = soup.find(rel="canonical").get("href")
    data["name"] = soup.find("h1").text.strip()
    data["price"] = soup.find(id="priceblock_ourprice").text if soup.find(id="priceblock_ourprice") else None
    data["img_main"] = soup.find(id="landingImage").get("data-old-hires")

    return data

products_data = []
for link in product_links:
    if not link.startswith('http'):
        continue
    print('Parse ' + link)
    products_data.append(get_product_info(link))
    time.sleep(1)

pprint(products_data)
