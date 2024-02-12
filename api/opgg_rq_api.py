import requests
from bs4 import BeautifulSoup as bs
import json

# 세션 열기
session = requests.Session()

headers = {'Accept-Language': 'ko_KR,en;q=0.8',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
          'Content-type': 'application/json'} 

params = {
    'q':"고라파덕화구이",
    'region':"kr"
}


def get_summoner_data(session, headers, params):
    # 소환사 정보 받아오기
    url = 'https://www.op.gg/en_US/summoners/search'

    r = session.post(url, headers=headers, params=params)

    # if r.status_code == 200:
    #     print('Logged in')
    # else:
    #     print('Failed to login')

    soup = bs(r.text, 'html.parser')
    my_script = soup.script
    my_dict = json.loads(my_script.text[24:-9])
    # print(soup.find_all('script')[-1])

    target = soup.find_all('script')[-1].text
    target_dict = json.loads(target)

    target_dict_1 = target_dict['props']
    target_dict_2 = target_dict_1['pageProps']
    target_dict_3 = target_dict_2['games']
    target_dict_4 = target_dict_3['data']
    target_dict_5 = target_dict_4[0]

    mydata = target_dict_5['myData']
    summoner_id = mydata['summoner']['summoner_id']
    game_region = my_dict['game_region']
    # vd0-_FTK1nehRR26O3YbJgE8asX5bHbvn0y77vtJNw7TwHU

    return game_region, summoner_id

def get_game_count(game_region, summoner_id, season_id):
    api_url = f"https://www.op.gg/api/v1.0/internal/bypass/summoners/{game_region}/{summoner_id}/most-champions/rank/"

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Content-type': 'application/json; charset=utf-8'} 

    data = {'game_type':'RANKED',
            'season_id':f'{season_id}'}

    r2 = session.get(api_url, headers=header, params=data)

    my_game = json.loads(r2.text)
    return(int(my_game['data']['play']))



game_region, summoner_id = get_summoner_data(session, headers, params)

count = 0
for i in range(1, 100, 2):
    try:
        count += get_game_count(game_region, summoner_id, i)
    except:
        pass

print(count * 1800 / 60 / 60 * 9860)