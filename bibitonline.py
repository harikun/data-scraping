import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
start_time = time.time()
daftar_bunga = [];
def get_flowers():
    url = 'https://bibitonline.com/artikel/kumpulan-nama-bunga-lengkap-dari-a-z-beserta-gambar-dan-penjelasannya'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    figcaption = soup.find_all('figcaption')
    no = 0
    for i in figcaption:
        no += 1
        daftar_bunga.append({ 'no': no, 'nama bunga': i.text })
        df = pd.DataFrame(daftar_bunga)
    df.to_csv(f'data_csv/bunga_{no}.csv', index=False)
    df.to_excel(f'data_excel/bunga_{no}.xlsx', index=False)
    df.to_json(f'data_json/bunga_{no}.json', orient='records')
# get_flowers()

daftar_bibit_benih_tanaman = []
def get_bibit_benih_tanaman():
    page = 1; no = 0
    url = 'https://bibitonline.com/kategori/benih-bibit-tanaman/page/'
    while page <= 86:
        res = requests.get(url + str(page))
        soup = BeautifulSoup(res.text, 'html.parser')
        box_text_products = soup.find_all('div', class_='box-text box-text-products')
        for i in box_text_products:
            no += 1
            product_link = i.find('p', class_='product-title').find('a')['href']
            product_title = i.find('p', class_='product-title').text
            product_price = int(i.find('span', class_='woocommerce-Price-amount amount').text.replace('Rp', '').replace('.', '').replace('&nbps;', ''))
            print(no, product_price)
            daftar_bibit_benih_tanaman.append({ 'no': no, 'product link': product_link, 'product title': product_title, 'product price': product_price })
        page += 1
    df = pd.DataFrame(daftar_bibit_benih_tanaman)
    df.to_csv(f'data_csv/bunga_{no}.csv', index=False)
    df.to_excel(f'data_excel/bunga_{no}.xlsx', index=False)
    df.to_json(f'data_json/bunga_{no}.json', orient='records')

get_bibit_benih_tanaman()
print("--- %s seconds ---" % (time.time() - start_time))


