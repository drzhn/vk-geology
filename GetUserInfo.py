# по id пользователя найдем его первый пост, список друзей, выгрузим в json

import requests
import json
from time import sleep


def GetFriendsIds(user_id):
    users = ['users']
    i = 0
    count = 100  # качаем сразу по сто
    ret = []
    while users != []:
        payload = {'user_id': str(user_id), 'order': 'name', 'count': str(count), 'offset': i * count, 'fields': 'uid'}
        r = requests.get('https://api.vk.com/method/friends.get', params=payload)
        users = r.json()['response']
        for user in users:
            ret.append(user['user_id'])
        i += 1
        sleep(0.5)
    return ret

def GetUserFirstPost(user_id, token):
    payload = {'owner_id': str(user_id), 'filter': 'all', 'count':'1', 'offset':'0','access_token':token}
    r = requests.get('https://api.vk.com/method/wall.get', params=payload)
    for m in r.json()['response']:
        if type(m) is dict:
            return str(m['text'])

def SaveUserInfoToJson(user_id, token):
    data = {'friends':GetFriendsIds(user_id), 'first_post':GetUserFirstPost(user_id, token)}
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def GetUserInfoToJson():
    with open('data.txt', 'r') as outfile:
        print(json.load(outfile)['first_post'])

# SaveUserInfoToJson(170900699, 'a88996d7729f9031fb5a29bccb29b8e04f725cd51dc4c6fbd4a85fa5252c79815017a9513b001b3ed414a')
GetUserInfoToJson()