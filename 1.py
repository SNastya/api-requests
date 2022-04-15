from socket import timeout
import requests
import json
import pandas as pd
import openpyxl

#Задача 2
#1
res = requests.get('https://itunes.apple.com/lookup?id=518462', )
print(res.json())

#2
print(res.status_code)

#3
print(res.url)

#4
amg_artist_id = res.json().get('results')[0].get('amgArtistId')
print(amg_artist_id)

#Задача 3

#1
albums = requests.post('https://itunes.apple.com/lookup', data = {'amgArtistId': amg_artist_id, 'entity' : 'album', 'limit' : 100}, timeout = 60)
print(albums.json())

#2

print(albums.json().get('resultCount'))

#3
#первая запись содержит информацию об артисте, а далее 100 записей альбомов

#Задача 4
#1
data1 = albums.json().get('results')[1:31]
data2 = albums.json().get('results')[31:]
print(len(data1))
print(len(data2))

#2
df1 = pd.DataFrame(data1)
print(df1)

path = 'ds-intro/13_api/homework/data/'

df1.to_excel(path + '30_albums.xlsx', 'albums')

#3
df2 = pd.DataFrame(data2)
print(df2)

df2.to_csv(path + '70_albums.csv', sep ='\t')
