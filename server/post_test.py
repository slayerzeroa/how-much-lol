import requests

# 엔드포인트 URL
url = "http://slayerzeroa.iptime.org:8000/playtime"

# 요청에 포함할 데이터
data = {
    "gameName": "고라파덕화구이",
    "tagLine": "KR1",
}

# data = {
#     "gameName": "치카치카양치중",
#     "tagLine": "ECGOD",
# }

# POST 요청 보내기
response = requests.post(url, json=data)

# 응답 확인
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)