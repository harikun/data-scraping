import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
start_time = time.time()

def get_formula(s_kategori, max_page):
    url_rekap_formula = 'https://pestisida.id/simpes_app/rekap_formula_nama.php?'
    page = 1
    pestisida_list = []
    while page < max_page:
        params = {
        's_kategori': s_kategori,
        'rekap_formula_nama1Page': page
        }
        res = requests.get(url_rekap_formula, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        tr = soup.find_all('tr', class_='Row')
        for td in tr:
            no = td.find('td', {'style' : 'TEXT-ALIGN: right'}).text
            merek_dagang = td.find('td').find_next_sibling('td').contents[0].text.replace('(Umum)', '').replace('(umum)', '').strip()
            bahan_aktif = td.find('td').find_next_sibling('td').contents[3].text.strip()
            deskripsi_singkat = td.find('td').find_next_sibling('td').contents[6].text.strip()
            cara_pemakaian = td.find('td').find_next_sibling('td').find_next_sibling('td').text.strip()
            perusahaan = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[0].text.strip()
            jenis_izin = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[4].text.strip()
            tanggal_akhir_izin = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[6].text.strip()
            no_pendaftaran = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[8].text.strip()
            pestisida_list.append({
                'no': no,
                'merek dagang': merek_dagang,
                'cara pemakaian': cara_pemakaian,
                'pembuat': perusahaan,
            })
            print(no, merek_dagang)
        page += 1
    df = pd.DataFrame(pestisida_list)
    df.to_csv(f'data_csv/pestisida_{s_kategori}_{no}.csv', index=False)
    df.to_excel(f'data_excel/pestisida_{s_kategori}_{no}.xlsx', index=False)
    df.to_json(f'data_json/pestisida_{s_kategori}_{no}.json', orient='records')

get_formula('umum', 42)
print("--- %s seconds ---" % (time.time() - start_time))
