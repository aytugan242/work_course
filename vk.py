import requests
import json
# получение токена из VK
def get_token_url(client_id):
    URL = 'https://oauth.vk.com/authorize'
    params = {
        'client_id' : client_id,
        'display' : 'page',
        'scope' : 'photos',
        'response_type' : 'token',
        'v' : '5.101'
    }
    token_url = requests.get(URL, params)
    return token_url.url

# Получение из ВК картинок (фото из профиля - profile)
token = 'vk1.a.ecrUoHKMwO3s6Tx3b-kxnmIsvyJ52GVhy9UlsC2czZ2m4ic0EHp1qjrVCzlMBWKnJKfMjk7AaQB-TBVhEXWLJVHVHVr1MHsp4dnVSauPCSh1VuC98P58CdlRmVD32XhluYhkdDLZVs1kYDZnt_21_BUDuTLYxuxQn8qp9tpaHfukAOZR16eIdiJXwj_AZtc9'
class VKClient:
    API_BASE_URL = 'https://api.vk.com/method'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.154'
        }
    def get_profile_photos(self):
        params = self.get_common_params()
        params.update({'owner_id': self.user_id, 'album_id': 'profile', 'extended': 1})
        res = requests.get(f'{self.API_BASE_URL}/photos.get', params=params)
        return res.json()

# Создание объекта и получение данных по картинкам, token ограничен по времени
# Запись данных по ВК в файл vk_images.json

if __name__ == "__main__":
    vl_cl = VKClient(token, '7567539')
    photos = vl_cl.get_profile_photos()

    with open('vk_image.json', 'w') as f:
        f.write(json.dumps(photos))

