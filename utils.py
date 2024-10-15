# def read_api_key(path) -> str:
#     with open(path, "r") as f:
#         return f.readline().strip()

from dotenv import load_dotenv
import os


def load_api_keys() -> list:
    load_dotenv()

    # 환경 변수에서 값 가져오기
    LOL_API_LIST = os.getenv('LOL_API_LIST')

    # 쉼표로 구분된 문자열을 리스트로 변환
    LOL_API_LIST = LOL_API_LIST.split(',')

    return LOL_API_LIST

def read_api_keys(path) -> dict:
    with open(path, "r") as f:
        # 줄 바꿈 문자 제거
        return [line.strip() for line in f.readlines()]