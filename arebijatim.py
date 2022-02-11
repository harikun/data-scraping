import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://arebijatim.org/anggota'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

