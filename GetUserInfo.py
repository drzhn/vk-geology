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


def GetGroupsIds(user_id, token):
    communities = []
    i = 0
    count = 100  # качаем сразу по сто
    ret = []
    while len(communities) != 1:
        payload = {'user_id': str(user_id), 'count': str(count), 'offset': i * count, 'access_token': token}
        r = requests.get('https://api.vk.com/method/groups.get', params=payload)
        communities = r.json()['response']
        ret = ret + communities[1:]
        i += 1
        sleep(0.5)
    return ret


def GetUserPost(user_id, post_id, token):
    payload = {'posts': str(user_id) + '_' + str(post_id), 'access_token': token}
    r = requests.get('https://api.vk.com/method/wall.getById', params=payload)
    for m in r.json()['response']:
        if type(m) is dict:
            return str(m['text'])

def FindPostInWall(owner_id, query, searchPost,  token):
    posts = []
    i = 0
    count = 20
    while len(posts) != 1:
        payload = {'owner_id': str(owner_id), 'count': str(count), 'offset': i*count, 'query': query, 'access_token': token}
        r = requests.get('https://api.vk.com/method/wall.search', params=payload)
        posts = r.json()['response']
        for post in posts[1:]:
            if post['text'] == searchPost:
                # print("FOUND!")
                return True
        i+=1
        sleep(0.5)
    return False

def SaveUserInfoToJson(user_id, post_id, token):
    data = {'friends': GetFriendsIds(user_id), 'groups': GetGroupsIds(user_id, token),
            'post': GetUserPost(user_id, post_id, token)}
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


def GetUserInfoFromJson():
    with open('data.txt', 'r') as outfile:
        ret = json.load(outfile)
        # print(ret['post'])
    return ret


def GetSettings():
    with open('settings.txt', 'r') as outfile:
        settings = json.load(outfile)
    return settings


# SaveUserInfoToJson(settings['user_id'], settings['post_id'], settings['token'])
GetUserInfoFromJson()



# GET ALL POSTS
# posts = ['users']
# i = 0
# count = 100  # качаем сразу по сто
# ret = []
# while posts != []:
#     payload = {'owner_id': str(group), 'count': str(count), 'offset': i * count, 'access_token': settings['token']}
#     r = requests.get('https://api.vk.com/method/wall.get', params=payload)
#     posts = r.json()['response']
#     # print(posts)
#     found = False
#     for post in posts:
#         if type(post) is dict:
#             print(post['text'])
#             if post['text'] == userData['post']:
#                 print('found!')
#                 found = True
#                 break
#     if found:
#         print(i*count)
#         break
#     i += 1
#     sleep(0.5)