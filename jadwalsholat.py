import os
import json
import requests
from bs4 import BeautifulSoup

url = 'http://jadwalsholat.pkpu.or.id/?'
params = {
    'id': '48',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
