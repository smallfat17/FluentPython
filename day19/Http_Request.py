import os
import time
import sys
from time import perf_counter
from lxml import etree

import requests

# BASE_URL = 'http://120.78.187.183/static/listGames/images/'

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

# GAMES = ['孤岛惊魂5', '圆环的记忆', '狄仁杰之锦蔷薇', 'ASCENDANCE', '蔚蓝Celeste', '黑暗中的便便', '锈湖：天堂岛', 'Golem Gates', '旅馆吸血鬼', '神使的裹尸布', 'Go Go Poncho!', '不可救药', '现金岛枪战', '虚梦的少女']
# POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
#             'MX PH VN ET EG DE IR TR CD FR').split()

POP20_CC = ('CN IN US ID BR PK NG BD RU JP').split()
def save_flag(data, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(data)

def show(game):
    print(game+ '\t', end='')
    sys.stdout.flush()

def get_flag(game):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=game.lower())
    res = requests.get(url)
    return res.content

def download_many(game_list):
    for game in game_list:
        image = get_flag(game)
        show(game)
        save_flag(image, game + '.gif')
    return len(list(game_list))

def main(download_many):
    p0 = perf_counter()
    count = download_many(POP20_CC)
    elasped = perf_counter() - p0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elasped))

if __name__ == '__main__':
    main(download_many)

