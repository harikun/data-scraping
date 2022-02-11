import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
url = 'https://www.topendsports.com/sport/list/index.htm'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())

print("--- %s seconds ---" % (time.time() - start_time))