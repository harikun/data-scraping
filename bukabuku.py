import requests; from bs4 import BeautifulSoup; import pandas as pd
page =1; max_page = 2; buku_kita_populer = []; no = 0
res = requests.get(f'http://www.bukabuku.com/browses/index/dept:book/cid:44/format:Soft%20Cover/page:{str(page)}')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())