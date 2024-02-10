# def read_api_key(path) -> str:
#     with open(path, "r") as f:
#         return f.readline().strip()
    

def read_api_keys(path) -> dict:
    with open(path, "r") as f:
        # 줄 바꿈 문자 제거
        return [line.strip() for line in f.readlines()]