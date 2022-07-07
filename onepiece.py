import requests; import pandas as pd; from bs4 import BeautifulSoup;

url = "https://onepiece.fandom.com/id/wiki/Daftar_Karakter_Kanon"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

content = soup.find('div', class_='page-content')
table = content.find('table', class_='wikitable')
tbody = table.find('tbody')
no = 0; character_list = []
for td in tbody.findAll('tr')[1:]:
    no += 1
    name = td.find('td').find_next_sibling('td').text.strip()
    chapter = td.find('td').find_next_sibling('td').find_next_sibling('td').text.strip()
    episode = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
    try:
        year = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
        note = td.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip()
    except:
        note = ''
        year = ''
    print(no, name, chapter, episode, year, note)

    character_list.append({
        'no': no,
        'name': name,
        'chapter': chapter,
        'episode': episode,
        'year': year,
        'note': note
    })
df = pd.DataFrame(character_list)
df.to_excel(f'data_excel/one_piece_{no}.xlsx', index=False)

