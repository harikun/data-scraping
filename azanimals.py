import json; import time; import requests; import pandas as pd; from bs4 import BeautifulSoup
start_time = time.time()
url = 'https://a-z-animals.com/animals/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
no = 0; animal_list = []
list_item = soup.find_all('li', {'class': 'list-item'})
for i in list_item:
    no += 1
    animal_list.append({
        'no': no,
        'animal': i.text,
        'link': i.find('a').get('href')
    })
with open('data_json/azanimals.json', 'w') as f:
    json.dump(animal_list, f, indent=4)
df = pd.DataFrame(animal_list)
df.to_csv('data_csv/azanimals.csv', index=False)
df.to_excel('data_excel/azanimals.xlsx', index=False)
print("--- %s seconds ---" % (time.time() - start_time))