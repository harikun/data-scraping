import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

page = 0
url = 'https://www.indonesia-investments.com/id/bisnis/profil-perusahaan/item74?'
params ={
 "CompanyProfileModel_page": page
}
res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)