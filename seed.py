import os
import random
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinocards.settings')
django.setup()

from main.models import *
from accounts.models import ProfileType

# create cards
# with open('dino_list.txt') as f:
#     dinos = f.read().split()
#
#     # card rarity settings
#     rarity = [200, 500, 800, 1000]
#     index = 0
#     end_count = len(rarity) - 1
#
#     count = 1
#
#     for dino in dinos:
#         try:
#             res = requests.get(f'https://dinosaurpictures.org/{dino}-pictures', timeout=0.5)
#             soup = BeautifulSoup(res.content, 'html.parser')
#             img_containers = soup.select('.img-container')
#             img_url = img_containers[0].find_all('img')[0].get('src')
#             intro = soup.select('.intro')
#             description = intro[0].select('p')[0].getText()
#             Card.objects.create(
#                 name=dino,
#                 description=description,
#                 rarity_rate=rarity[index],
#                 image=img_url
#             )
#             if index == end_count:
#                 index = 0
#                 if end_count == 0:
#                     end_count = len(rarity) - 1
#                 else:
#                     end_count -= 1
#             else:
#                 index += 1
#
#             print(count)
#
#             # limit cards to 100
#             if count == 100:
#                 break
#             count += 1
#
#         except Exception as e:
#             print(dino, e, ' fail')

# create profile types
profile_types = [{'name': 'Tyrannosaurus Rex', 'img': 't-rex.png'},
                 {'name': 'Triceratops', 'img': 'triceratops.png'},
                 {'name': 'Velociraptor', 'img': 'velociraptor.png'},
                 {'name': 'Stegosaurus', 'img': 'stegosaurus.png'},
                 {'name': 'Spinosaurus', 'img': 'spinosaurus.png'},
                 {'name': 'Archaeopteryx', 'img': 'archaeopteryx.png'},
                 {'name': 'Brachiosaurus', 'img': 'brachiosaurus.png'},
                 {'name': 'Allosaurus', 'img': 'allosaurus.png'},
                 {'name': 'Apatosaurus', 'img': 'apatosaurus.png'},
                 {'name': 'Dilophosaurus', 'img': 'dilophosaurus.png'}]
#
for t in profile_types:
    ProfileType.objects.create(name=t['name'], img=t['img'])
