import requests; import pandas as pd; from bs4 import BeautifulSoup;
page = 1; max_page = 274; buku_toko_muslim = []; no = 0
while page < max_page:
    res = requests.get(f'https://toko-muslim.com/category/lihat-semua-buku/page/{str(page)}/')
    soup = BeautifulSoup(res.text, 'html.parser')
    article = soup.find_all('article', class_='group')
    for data in article:
        no += 1
        title = data.find('h2', class_='post-title entry-title').find('a').text
        link = data.find('h2', class_='post-title entry-title').find('a').get('href')
        summary =  data.find('div', class_='entry-summary').text.strip()
        print(no, title, link, summary)
        buku_toko_muslim.append({
            'no': no,
            'title': title,
            'summary': summary,
            'link': link,
        })
    page += 1
df = pd.DataFrame(buku_toko_muslim)
df.to_csv(f'data_csv/buku_toko_muslim-{no}.csv', index=False)
df.to_excel(f'data_excel/buku_toko_muslim-{no}.xlsx', index=False)
df.to_json(f'data_json/buku_toko_muslim-{no}.json', orient='records')

print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')