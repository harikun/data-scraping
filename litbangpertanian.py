import json; import requests; import pandas as pd; from bs4 import BeautifulSoup; import urllib3

url_varieatas = 'https://www.litbang.pertanian.go.id/varietas/'
p = 1
params = { 'p': p }
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass
res = requests.get(url_varieatas, params=params, verify=False)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
