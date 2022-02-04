import json
import requests
from bs4 import BeautifulSoup

url = 'https://shopee.co.id/msigamingofficial?'
page = 0
params = {
 "page": page,
 "sortBy": "sales"
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
theme = soup.find('div',{'class': 'theme--ofs'})
print(theme)