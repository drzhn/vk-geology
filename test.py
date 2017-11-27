import requests
from time import sleep

# payload = {'user_id': '170900699', 'order': 'name', 'count': '100', 'offset':'0', 'fields': 'uid'}
# r = requests.get('https://api.vk.com/method/friends.get', params=payload)
# print(r.json()['response'])
i = 0
ret = []
for i in range(5):
    payload = {'user_id': '170900699', 'order': 'name', 'count':'100', 'offset':i*100, 'fields':'uid'}
    r = requests.get('https://api.vk.com/method/friends.get', params=payload)
    users = r.json()['response']
    for user in users:
        ret.append(user['user_id'])
    sleep(0.5)

print(len(ret))

# token = 'a88996d7729f9031fb5a29bccb29b8e04f725cd51dc4c6fbd4a85fa5252c79815017a9513b001b3ed414a'
# payload = {'owner_id': '170900699', 'filter': 'all', 'count':'1', 'offset':'0','access_token':token}
# r = requests.get('https://api.vk.com/method/wall.get', params=payload)
# for m in r.json()['response']:
#     if type(m) is dict:
#         print(m['text'])