import requests; import pandas as pd; from bs4 import BeautifulSoup; import time
start_time = time.time()

def get_formula(max_page):
    url_rekap_formula = 'https://pestisida.id/simpes_app/rekap_formula_nama.php?'
    url_rekap_komoditas = 'https://pestisida.id/simpes_app/rekap_komoditas_formula.php?'
    page = 1
    pestisida_list = []
    while page < max_page:
        params = {
        # 's_kategori': s_kategori,
        # 'rekap_formula_nama1Page': page
        'rekap_komoditas_formula1Page': page
        }
        res = requests.get(url_rekap_komoditas, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        tr = soup.find_all('tr', class_='Row')
        for td in tr:
            no = td.find('td', {'style' : 'TEXT-ALIGN: left'}).text.strip()
            tujuan = td.find('td').find_next_sibling('td').text
            kategori = td.find('td').find_next_sibling('td').find_next_sibling('td').text
            merek = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text

            merek_dagang = td.find('td').find_next_sibling('td').contents[0].text.replace('(Ekspor)', '').replace('(ekspor)', '').strip()
            bahan_aktif = td.find('td').find_next_sibling('td').contents[3].text.strip()
            deskripsi_singkat = td.find('td').find_next_sibling('td').contents[6].text.strip()
            cara_pemakaian = td.find('td').find_next_sibling('td').find_next_sibling('td').text.strip()
            perusahaan = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[0].text.strip()
            jenis_izin = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[4].text.strip()
            tanggal_akhir_izin = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[6].text.strip()
            no_pendaftaran = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').contents[8].text.strip()
            pestisida_list.append({
                'no': no,
                'merek dagang': merek,
                'tujuan': tujuan,
                'kategori': kategori,
                # 'bahan aktif': bahan_aktif,
                # 'deskrispi': deskripsi_singkat,
                # 'pembuat': perusahaan,
            })
            print(no)
        page += 1
    df = pd.DataFrame(pestisida_list)
    df.to_csv(f'data_csv/pestisida_komoditas_{no}.csv', index=False)
    df.to_excel(f'data_excel/pestisida_komoditas_{no}.xlsx', index=False)
    df.to_json(f'data_json/pestisida_komoditas_{no}.json', orient='records')
#s_kategori yang tersedia ['umum', 'teknis', 'ekspor']
get_formula(32)
print("--- %s seconds ---" % (time.time() - start_time))
