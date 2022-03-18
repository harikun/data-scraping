import requests; import pandas as pd; from bs4 import BeautifulSoup;
page = 1; no = 0; max_page = 85; daftar_produk_pria = []; base_url = 'https://voila.id'
while page < max_page:
    res = requests.get(f'https://voila.id/collections/men?page={str(page)}')
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find_all('div', {'class': 'boost-pfs-filter-product-item-inner'})
    for product in content:
        no += 1
        name = product.find('a', {'class': 'boost-pfs-filter-product-item-title'}).get_text()
        link_product = base_url + product.find('a', {'class': 'boost-pfs-filter-product-item-title'})['href']
        try:
            price = product.find('span', {'class': 'boost-pfs-filter-product-item-sale-price'}).get_text().replace('IDR', '').replace(',', '.').strip()
        except:
            price = product.find('span', {'class': 'boost-pfs-filter-product-item-regular-price'}).get_text().replace('IDR', '').replace(',', '.').strip()
        vendor = product.find('a', {'class': 'product-vendor'}).get_text()
        print(no, name)
        daftar_produk_pria.append({
            'no': no,
            'product name': name,
            'price': price,
            'vendor': vendor,
            'link': link_product
        })
    page += 1
df = pd.DataFrame(daftar_produk_pria)
df.to_excel(f'data_excel/viola_daftar_produk_pria_{no}.xlsx', index=False)
df.to_csv(f'data_csv/viola_daftar_produk_pria_{no}.csv', index=False)
df.to_json(f'data_json/viola_daftar_produk_pria-{no}.json', orient='records')
print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')