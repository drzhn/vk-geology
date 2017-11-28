import json
import requests
from time import sleep

post = ""
friends = []
communities = []
with open('data.txt', 'r') as outfile:
    print(json.load(outfile)['post'])