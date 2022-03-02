import requests; import pandas as pd; from bs4 import BeautifulSoup;
no =0; page =1; max_page = 1306; daftar_properti_sewa = []
while page < max_page:
    res = requests.get(f'https://www.raywhite.co.id/sewa?page={str(page)}')
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find_all('div', {'class': 'card'})
    for properti in content[:15]:
        no += 1
        link = properti.find('a', {'class': 'item'})['href']
        price = properti.find('p', {'class': 'card-text'}).find_next_sibling('p', {'class': 'card-text'}).get_text()
        image = properti.find('img', {'class': 'card-img-top'})['src']
        name = properti.find('img', {'class': 'card-img-top'})['alt']
        print(no, name, price)
        daftar_properti_sewa.append({
            'no': no,
            'property name': name,
            'price': price,
            'link': link,
            'image': image
        })
    page += 1
df = pd.DataFrame(daftar_properti_sewa)
df.to_excel(f'data_excel/raywhite_daftar_properti_sewa_{no}.xlsx', index=False)
df.to_csv(f'data_csv/raywhite_daftar_properti_sewa_{no}.csv', index=False)
df.to_json(f'data_json/raywhite_daftar_properti_sewa-{no}.json', orient='records')
print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')

