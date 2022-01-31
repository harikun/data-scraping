import requests
import json

url = 'https://www.instagram.com/graphql/query'
variables = {
 "id":"3173171436",
 "first":12
}
query_hash =  '8c2a529969ee035a5063f2fc8602a0fd'
params = {
   'query_hash': query_hash,
   'variables': json.dumps(variables)
}

res = requests.get(url, params=params).json()
print(res)