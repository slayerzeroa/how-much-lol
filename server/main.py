from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import sys
sys.path.append('engine/api')

from engine.api import lol_api as lol

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://slayerzeroa.iptime.org:3000"],  # Next.js 애플리케이션의 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# 입력 데이터 모델 정의
class PlaytimeRequest(BaseModel):
    gameName: str
    tagLine: str
    unit: str = 'minutes'

@app.post("/playtime")
async def calculate_playtime(request: PlaytimeRequest):
    playtime = lol.get_playtime(request.gameName, request.tagLine, request.unit)
    return {"playtime": playtime}
