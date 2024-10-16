from fastapi import FastAPI
from pydantic import BaseModel

import os
import sys
sys.path.append('engine/api')

from engine.api import lol_api as lol

app = FastAPI()

# 입력 데이터 모델 정의
class PlaytimeRequest(BaseModel):
    gameName: str
    tagLine: str
    unit: str = 'minutes'

@app.post("/playtime")
async def calculate_playtime(request: PlaytimeRequest):
    playtime = lol.get_playtime(request.gameName, request.tagLine, request.unit)
    return {"playtime": playtime}
