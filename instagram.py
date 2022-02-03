import requests
import json
from bs4 import BeautifulSoup

short_code = input('Enter short code: ')
url = 'https://www.instagram.com/graphql/query/?'
variables = {
      'shortcode': short_code,
      'first': 24,
}
params={
      'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
      'variables': variables

}

res = requests.get(url, params=params)
print(res.status_code)

# error 429 - too many requests I think it's because of the api limit it. new instagram policy i thinks

