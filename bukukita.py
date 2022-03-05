import requests; from bs4 import BeautifulSoup; import pandas as pd
page = 1; max_page = 8; buku_kita_populer = []; no = 0
while page <= max_page:
    res = requests.get(f'https://www.bukukita.com/katalogbukuatribut.php?page={str(page)}&atrId=3')
    soup = BeautifulSoup(res.text, 'html.parser')
    product = soup.find_all('div', class_='product-preview')
    for item in product:
        no += 1
        cover = item.find('img').get('src')
        title = item.find('div', class_='product-preview__info__title').find('a').text
        author = item.find('div', class_='product-preview__info__title').find('div', class_='ellipsis').contents[4].replace('oleh', '').replace('', '').strip()
        price = item.find('div', class_='price-box__new').text.replace('Rp', '').replace('\n', '').strip()
        link = item.find('div', class_='product-preview__info__title').find('a').get('href')
        buku_kita_populer.append({
            'no': no,
            'title': title,
            'author': author,
            'price': price,
            'link': link,
            'cover': cover,
        })
        print(buku_kita_populer)
    page += 1
df = pd.DataFrame(buku_kita_populer)
df.to_csv(f'data_csv/buku_kita_populer-{no}.csv', index=False)
df.to_excel(f'data_excel/buku_kita_populer-{no}.xlsx', index=False)
df.to_json(f'data_json/buku_kita_populer-{no}.json', orient='records')

print('\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')