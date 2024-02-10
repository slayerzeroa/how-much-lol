import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import requests
import utils
import time
import numpy as np

# variable api_keys is a list of api keys
api_keys = utils.read_api_keys("C:\\Users\\slaye\\VscodeProjects\\how-much-lol\\env\\api_key.txt")

header = {"X-Riot-Token": "RGAPI-782a547a-875e-4051-899d-13977f17db14"}

game_log_header = {"X-Riot-Token": "RGAPI-1ddd3e7c-f22c-4841-8580-1faad67684ef"}

def rotate_api_key():
    # queue로 구현
    global header
    global api_keys
    key = api_keys.pop(0)
    api_keys.append(header["X-Riot-Token"])
    header["X-Riot-Token"] = key


def get_summoner_info(summoner_name: str) -> dict:
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    response = requests.get(url, headers=game_log_header)
    rotate_api_key()
    return response.json()

def get_account_info(puuid: str) -> dict:
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    response = requests.get(url, headers=game_log_header)
    rotate_api_key()
    return response.json()

def get_game_logs(puuid: str, start: int, count:int=100) -> dict:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    response = requests.get(url, headers=game_log_header)
    return response.json()

def get_game_info(match_id: str) -> dict:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=game_log_header)
    rotate_api_key()
    return response.json()

def get_game_duration(match_id: str) -> int:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=header)
    rotate_api_key()
    return response.json()['info']['gameDuration']

def get_every_game_logs(puuid: str) -> list:
    start = 0
    count = 100
    game_logs = []
    while True:
        logs = get_game_logs(puuid, start, count)
        if len(logs) == 0:
            break
        game_logs += logs
        start += count
    return game_logs

def get_average_game_time(game_logs: list) -> list:
    game_times = []
    for game_log in game_logs:
        try:
            game_times.append(get_game_duration(game_log[:100]))
        except:
            print(game_log)
            break
        # time.sleep(2)
    return np.mean(game_times)


def get_champions_played(encryptedPUUID: str, championId: str) -> int:
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/by-champion/{championId}"
    response = requests.get(url, headers=header)
    rotate_api_key()
    return response.json()


# puuid = get_summoner_info("고라파덕화구이")["puuid"]
# # print(get_summoner_info("고라파덕화구이"))
# print(get_account_info(puuid))
# # print(puuid)
# # print(get_champions_played(puuid, "20"))

# url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
# response = requests.get(url, headers=header)

# print(response.json())