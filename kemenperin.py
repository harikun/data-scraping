import json
import requests
from bs4 import BeautifulSoup

url = 'https://kemenperin.go.id/direktori-perusahaan?'
page = 1
params = {
 "hal": page,
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())