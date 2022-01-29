import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/mobile-phones-338/iphones-1235/?'
site = 'https://id.carousell.com'
params = {
 'addRecent' : 'false',
 'canChangeKeyword' : 'false',
 'includeSuggestions' : 'false',
 'searchId': '687FqQ',
}
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
#scraping process
