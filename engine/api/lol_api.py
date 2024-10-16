import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import requests
import utils
import time
import numpy as np


# # variable api_keys is a list of api keys
# api_keys = utils.read_api_keys("C:\\Users\\slaye\\VscodeProjects\\how-much-lol\\env\\api_key.txt")

api_keys = utils.load_api_keys()

headers = {"X-Riot-Token": api_keys[0]}

game_log_headers = {"X-Riot-Token": api_keys[0]}

def rotate_api_key():
    # queue로 구현
    global headers
    global api_keys
    key = api_keys.pop(0)
    api_keys.append(headers["X-Riot-Token"])
    headers["X-Riot-Token"] = key


def get_summoner_info(gameName: str, tagLine: str) -> dict:
    """소환사 정보를 가져오는 함수."""
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    
    try:
        response = requests.get(url, headers=headers)
        
        # 응답 상태 코드 체크
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.json()}")
            # rotate_api_key()  # 에러가 발생한 경우 API 키를 회전시킴
            return {"error": "Failed to fetch summoner info"}

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        # rotate_api_key()
        return {"error": str(e)}


def get_account_info(puuid: str) -> dict:
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    response = requests.get(url, headers=game_log_headers)
    # rotate_api_key()
    return response.json()

def get_game_logs(puuid: str, start: int=0, count:int=100) -> dict:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={start}&count={count}"
    response = requests.get(url, headers=game_log_headers)
    return response.json()

def get_game_info(match_id: str) -> dict:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=game_log_headers)
    # rotate_api_key()
    return response.json()

def get_game_duration(match_id: str) -> int:
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=headers)
    # rotate_api_key()
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
    response = requests.get(url, headers=headers)
    # rotate_api_key()
    return response.json()


def get_champions_mastery(encryptedPUUID: str) -> dict:
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}"
    response = requests.get(url, headers=headers)
    # rotate_api_key()
    return response.json()


def get_played_champion_id(puuid: str) -> list:
    mastery_list = get_champions_mastery(puuid)
    champion_id_list = []

    for mastery in mastery_list:
        champion_id_list.append(mastery['championId'])
    
    return champion_id_list


def get_every_championPoints(puuid: str) -> list:
    mastery_list = get_champions_mastery(puuid)
    champion_points = 0

    for mastery in mastery_list:
        champion_points += int(mastery['championPoints'])
    
    return champion_points



def get_playing_count(gameName:str, tagLine:str) -> int:
    # 한 판 당 대략 600점
    puuid = get_summoner_info(gameName, tagLine)['puuid']
    total_championPoints = get_every_championPoints(puuid)
    rotate_api_key()
    return total_championPoints/600


def get_playtime(gameName: str, tagLine: str, unit:str='minutes') -> int:
    playing_count = get_playing_count(gameName, tagLine)
    return round(playing_count*30)

# puuid = get_summoner_info("고라파덕화구이")["puuid"]
# # print(get_summoner_info("고라파덕화구이"))
# print(get_account_info(puuid))
# # print(puuid)
# # print(get_champions_played(puuid, "20"))

# url = f"https://asia.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
# response = requests.get(url, headers=headers)

# print(response.json())

# print(get_summoner_info("고라파덕화구이"))

# vd0-_FTK1nehRR26O3YbJgE8asX5bHbvn0y77vtJNw7TwHU