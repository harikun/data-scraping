from google_play_scraper import app; import pandas as pd;
import numpy as np
from google_play_scraper import Sort, reviews_all

reviews = reviews_all(
    'com.dafturn.mypertamina',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df = pd.DataFrame(np.array(reviews), columns=['review'])
df = df.join(pd.DataFrame(df.pop('review').tolist()))
df.head()
df.to_excel('data_excel/mypertamina.xlsx', index=False)
print('Successfully export my pertamina to excel file')