import requests
from bs4 import BeautifulSoup
import os
import sys

sys.path.append('server/engine/api')

import utils

import numpy as np

import api.lol_api as lol
import time


start = time.time()

gameName = '고라파덕화구이'
tagLine = "KR1"

print(lol.get_playtime(gameName, tagLine))


gameName = '치카치카양치중'
tagLine = "ECGOD"

print(lol.get_playtime(gameName, tagLine))


# print(total_championPoints)
# print(total_championPoints/600)

print("소환사 정보를 가져오는데 걸린 시간: ", time.time() - start)