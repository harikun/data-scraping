import requests; from bs4 import BeautifulSoup; import pandas as pd
page =1; max_page = 2; buku_kita_populer = []; no = 0; base_url = 'http://www.bukabuku.com'
res = requests.get(f'http://www.bukabuku.com/browses/index/dept:book/cid:44/format:Soft%20Cover/page:{str(page)}')
soup = BeautifulSoup(res.text, 'html.parser')
content = soup.find_all('div', class_='content')
for item in content:
    no += 1
    title = item.find('span', class_='product_list_title').find('a').text
    author = item.find('div', class_='product_author text_smaller').text.replace('oleh', '').strip()
    price = int(item.find('span', class_='price').text.replace('Rp.', '').replace('.', '').strip())
    status_product = item.find('span', class_='product_status_orange').text.strip()
    link = base_url + item.find('span', class_='product_list_title').find('a').get('href')
    print(no,title, price, status_product)
