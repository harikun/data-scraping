import time
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
china = '1'; vietnam = '3'; korea = '4'
url = "http://www.bkipm.kkp.go.id/bkipmnew/upifn/index/"

def importir_terdaftar():
    res = requests.get(url + china)
    soup = BeautifulSoup(res.text, 'html.parser')
    importir_list = []
    no = 1
    table = soup.find('table', {'class': 'table_upi'})
    tr_upi_data = table.find_all('tr', {'class': 'upi_data'})
    for td in tr_upi_data:
        reg_number = td.find('td').text.strip()
        name_of_establishment = td.find('td').findNextSibling().text
        address = td.find('td').findNextSibling().findNextSibling().text.strip()
        products = td.find('td').findNextSibling().findNextSibling().findNextSibling().text.strip()
        importir_list.append({
            'no': no,
            'reg number': reg_number,
            'name of establishment': name_of_establishment,
            'address': address,
            'products': products
        })
        no += 1

    with open(f'data_json/bkipm_china_{no - 1}.json', 'w') as f:
        json.dump(importir_list, f, indent=4)

    df = pd.DataFrame(importir_list)
    df.to_csv(f'data_csv/bkipm_china_{no - 1}.csv', index=False)

    df = pd.DataFrame(importir_list)
    df.to_excel(f'data_excel/bkipm_china_{no - 1}.xlsx', index=False)

importir_terdaftar()

print("--- %s seconds ---" % (time.time() - start_time))