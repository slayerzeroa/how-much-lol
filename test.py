import requests
from bs4 import BeautifulSoup
import os
import sys

sys.path.append('api')

import utils

from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

import numpy as np

import api.lol_api as lol
import api.opgg_api as opgg
import time


start = time.time()

gameName = '고라파덕화구이'
tagLine = "KR1"

puuid = lol.get_summoner_info(gameName, tagLine)['puuid']

# print(puuid)

champion_id = lol.get_played_champion_id(puuid)

# print(champion_id)

total_championPoints = lol.get_every_championPoints(puuid)

print(total_championPoints)
print(total_championPoints/600)

# print("소환사 정보를 가져오는데 걸린 시간: ", time.time() - start)