import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://minecraftitemids.com/types')
soup = BeautifulSoup(r.content, 'html.parser')

base_selector = 'body > div.container.container-monetize > div > div:nth-child(2) > div > div'
divs = soup.select(base_selector)
hrefs = [div.select_one('div > a').get('href') for div in divs]

names = []
ids = []

for href in hrefs:
    r = requests.get(f'https://minecraftitemids.com{href}')
    soup = BeautifulSoup(r.content, 'html.parser')

    base_selector = 'body > div.container.container-monetize > div > div.rd-filter > div.rd-filter__container > div > table > tbody > tr'
    rows = soup.select(base_selector)

    names.extend([row.select_one('td:nth-child(2) > a').text for row in rows])
    ids.extend([row.select_one('td:nth-child(3) > div > span').text for row in rows])

data = [{'block_name': name, 'block_id': id} for name, id in zip(names, ids)]
json_data = json.dumps(data, indent=2)
with open('minecraft_items.json', 'w') as f:
    f.write(json_data)

print(json_data)