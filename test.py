# тестовый файл, в проекте не нужен

import requests
from time import sleep

# payload = {'user_id': '170900699', 'order': 'name', 'count': '100', 'offset':'0', 'fields': 'uid'}
# r = requests.get('https://api.vk.com/method/friends.get', params=payload)
# print(r.json()['response'])
# i = 0
# ret = []
# for i in range(5):
#     payload = {'user_id': '170900699', 'order': 'name', 'count':'100', 'offset':i*100, 'fields':'uid'}
#     r = requests.get('https://api.vk.com/method/friends.get', params=payload)
#     users = r.json()['response']
#     for user in users:
#         ret.append(user['user_id'])
#     sleep(0.5)
#
# print(len(ret))

# token = 'a88996d7729f9031fb5a29bccb29b8e04f725cd51dc4c6fbd4a85fa5252c79815017a9513b001b3ed414a'
# payload = {'owner_id': '170900699', 'filter': 'all', 'count':'1', 'offset':'0','access_token':token}
# r = requests.get('https://api.vk.com/method/wall.get', params=payload)
# for m in r.json()['response']:
#     if type(m) is dict:
#         print(m['text'])

import json

settings = {'token':'19a1340b24c586ce15fbb97c0f1ed38037d7f2d88ba3e0883356216f7ce465d4c17e99c72e8341a62794a',
            'user_id':170900699,
            'post_id':790}
payload = {'user_id': str(settings['user_id']), 'count': 1000, 'offset': 0,  'access_token': settings['token']}
r = requests.get('https://api.vk.com/method/groups.get', params=payload)
print(len(r.json()['response']))