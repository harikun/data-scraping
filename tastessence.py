import pandas
import requests; from bs4 import BeautifulSoup; import time; import pandas as pd
start_time = time.time()
res = requests.get('https://tastessence.com/beer-brands-list')
soup = BeautifulSoup(res.content, 'html.parser')
li = soup.find_all('li')[8:1166]
no = 0; beer_list = []
for i in li:
    no += 1
    print(no, i.text)
    beer_list.append({ 'no': no, 'name': i.text })
df = pd.DataFrame(beer_list)
df.to_csv(f'data_csv/tastessence_beer_{no}.csv', index=False)
df.to_excel(f'data_excel/tastessence_beer_{no}.xlsx', index=False)
df.to_json(f'data_json/tastessence_beer_{no}.json', orient='records')
print("--- %s seconds ---" % (time.time() - start_time))

print(f'\n Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')
print(f'\n Support Hari on paypal: https://www.paypal.com/paypalme/ciptosuhari')