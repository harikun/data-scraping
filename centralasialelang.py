import requests; import pandas as pd; from bs4 import BeautifulSoup
res = requests.get('https://www.centralasialelang.com/properti.php?idC=all&idBk=all&idJ=all&idK=all&idS=all&cari=Cari')
soup = BeautifulSoup(res.text, 'html.parser')
