import requests; from bs4 import BeautifulSoup; import pandas as pd;
res = requests.get('http://sigpjj.binamarga.pu.go.id/iyo/record/index/?data=57&_tog1149016d=all')
soup = BeautifulSoup(res.text, 'html.parser')
