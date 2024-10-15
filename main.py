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

# name = input()
name = "고라파덕화구이"
tagline = "KR1"
puuid = lol.get_summoner_info(name, tagline)['puuid']
print(puuid)
info = lol.get_account_info(puuid)
print(info)
gamename, tagline = info["gameName"], info["tagLine"]


login_data = {
    'q': gamename,
    'region': tagline
}

# 웹드라이버 설정
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
url = f'https://www.op.gg/summoners/kr/{login_data["q"]}-{login_data["region"]}/champions'

print(url)
# 사이트 접속
driver.get(url)

total_count = opgg.total_game_count(driver)
print(total_count)

driver.close()

# game_log= lol.get_every_game_logs(puuid)
# print(game_log)

# average = lol.get_average_game_time(game_log)
# print(average)

# print(1800 * total_count / 60 / 60)

print(f"{name}... 롤 안 했으면... {int((1800 * total_count / 60 / 60) * 9860)}원을 벌었을 것이다.")

print(f"실행 시간: {time.time() - start}")