import requests; from bs4 import BeautifulSoup; import pandas as pd; import time
start_time = time.time()
page = 0; no = 0; data_lelang_bri = []
while page < 583:
    url = 'https://infolelang.bri.co.id/lelang/aset/' + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    card = soup.find_all('div', class_='col-sm-12 col-md-3 mt-5')
    for data in card:
        no += 1
        img = data.find('img')['src']
        link = data.find('a')['href']
        type = data.find('span', class_='card-title').text
        title = data.find('span', class_='card-title font-size-14 font-weight-bold text-uppercase').text
        location = data.find('span', class_='card-subtitle font-size-11 font-weight-normal font-rubik').text
        price = data.find('span', class_='card-subtitle font-size-18 font-weight-bold secondary-color').text
        print(no, price)
        data_lelang_bri.append({
            'no': no,
            'tautan': link,
            'gambar': img,
            'tipe': type,
            'judul': title,
            'lokasi': location,
            'harga': price
        })
    page += 1
df = pd.DataFrame(data_lelang_bri)
df.to_csv(f'data_csv/data_lelang_bri_{no}.csv', index=False)
df.to_excel(f'data_excel/data_lelang_bri_{no}.xlsx', index=False)
df.to_json(f'data_json/data_lelang_bri_{no}.json', orient='records')
print("--- %s seconds ---" % (time.time() - start_time))
