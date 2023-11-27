import json
import requests
from tqdm import tqdm
import time

with open('vk_image.json') as f:
    json_data = json.load(f)

count = json_data["response"]['count']
new_list = json_data["response"]['items']
# Название файлов в список (по датe загрузки, likes все нулевые)
name_file = []
# URL взяли самые большие по width * height
url_ = []

for row in new_list:
    name_file.append(row['date'])
    img_h_w = []
    img_url = []
    for i in range(count):
        img_h_w.append(row['sizes'][i]['height'] * row['sizes'][i]['width'])
        img_url.append(row['sizes'][i]['url'])
    url_.append(img_url[img_h_w.index(max(img_h_w))])

# Данные по Яндекс Диск Токен и папка, значение Токена удалили, для текста нужно добавить
token = ''
folder = 'vk_foto'
class Ya:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    url_f = 'https://cloud-api.yandex.net/v1/disk/resources'
    def __init__(self, token, folder):
        self.token = token
        self.folder = folder
    headers = {'Authorization': token}
    params_f = {'path': f'{folder}'}
    def post_photos(self):
        for i, n in zip(name_file, url_):
            params = {'path': f'{folder}/{i}',
                      'url': n,
                      'overwrite': 'false'}
            resp = requests.post(self.url, headers=self.headers, params=params)
        return resp.json()
    def folder_photos(self):
        resp = requests.put(self.url_f, headers=self.headers, params=self.params_f)
        return resp.json()

if __name__ == "__main__":
    ya_post = Ya(token, folder)
    fold = ya_post.folder_photos()
    photos = ya_post.post_photos()
    for i in tqdm(photos):
        time.sleep(1)


