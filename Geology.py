import json
import requests
from time import sleep
from GetUserInfo import GetUserInfoFromJson, GetSettings, FindPostInWall

post = ""
friends = []
communities = []
userData = GetUserInfoFromJson()
settings = GetSettings()
friendsCount = len(userData['friends'])
groupsCount = len(userData['groups'])
firstWords = " ".join(userData['post'].replace("<br><br>", " ").split()[:4])  # первые четыре слова поста

print('Search in friends...')
friendsWithPostCount = 0
for user in userData['friends']:
    if (FindPostInWall(user, firstWords, userData['post'], settings['token'])):
        friendsWithPostCount += 1
        print("friend: ", user)

print('Search in groups...')
groupsWithPostCount = 0
for group in userData['groups']:
    if (FindPostInWall(-1 * group, firstWords, userData['post'], settings['token'])):
        groupsWithPostCount += 1
        print("group: ", -1 * group)

print("\nFriends with post: ", friendsWithPostCount)
print("Groups with post: ", groupsWithPostCount)
p = (
1 - (1 - float(groupsWithPostCount) / groupsCount) * ((1 - float(friendsWithPostCount) / friendsCount) ** friendsCount))
print("p =", p)
