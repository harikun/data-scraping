import requests; from bs4 import BeautifulSoup; import pandas as pd
page =1; max_page = 20; buku_kita_softcover = []; no = 0; base_url = 'http://www.bukabuku.com'
while page <= max_page:
    res = requests.get(f'http://www.bukabuku.com/browses/index/dept:book/cid:44/format:Soft%20Cover/page:{str(page)}')
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find_all('div', class_='content')
    for item in content:
        no += 1
        title = item.find('span', class_='product_list_title').find('a').text
        author = item.find('div', class_='product_author text_smaller').text.replace('oleh', '').strip()
        try:
            price = int(item.find('span', class_='price').text.replace('Rp.', '').replace('.', '').strip())
            status_product = item.find('span', class_='product_status_orange').text.strip()
        except:
            price = ''
            status_product = 'Stock tidak tersedia'
        link = base_url + item.find('span', class_='product_list_title').find('a').get('href')
        print(no,title, price, status_product)
        buku_kita_softcover.append({ 'no': no, 'title': title, 'author': author, 'price': price, 'status_product': status_product, 'link': link})
    page += 1
df = pd.DataFrame(buku_kita_softcover)
df.to_csv(f'data_csv/buku_kita_softcover-{no}.csv', index=False)
df.to_excel(f'data_excel/buku_kita_softcover-{no}.xlsx', index=False)
df.to_json(f'data_json/buku_kita_softcover-{no}.json', orient='records')
print('\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')