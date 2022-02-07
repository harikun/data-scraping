import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://lelang.go.id/kantor/64/KPKNL-Surabaya.html?'
params = {
 "no-cache":"1lTG8ja9oDnCRp7S0Uvf",
 "page":"1"
}

res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())