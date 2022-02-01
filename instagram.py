import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/graphql/query/?'
params={
      'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
      'variables': '{"shortcode":"CZY5GBaljKG","include_reel":true,"first":24}'
}
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)