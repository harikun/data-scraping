import requests; import pandas as pd; from bs4 import BeautifulSoup;
res = requests.get('https://p2k.unkris.ac.id/id3/1-3073-2962/Daftar-Pulau-Di-Indonesia_26963_p2k-unkris.html')
soup = BeautifulSoup(res.text, 'html.parser')
content = soup.find_all('li', class_='p296b2cq1')
list_island = []; no = 0
for island in content[:2058]:
    no += 1
    try:
        name = island.contents[0].get_text().replace('(', '').replace(')', '')
    except:
        name = island.find('a').get_text()
    print(no, name)
    list_island.append({'no': no, 'name': name})
df = pd.DataFrame(list_island)
df.to_excel('data_excel/p2kunkris_pulau_{no}.xlsx', index=False)
print('Support Hari on karyakarsa: https://karyakarsa.com/ciptosuhari')