from fastapi import APIRouter
import requests
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

router=APIRouter()
@router.get("/crypto", tags=["crypto"])
def crypto_index():
    return {"crypto index"}

@router.get("/crypto/top7_search", tags=["crypto"])
async def top7_search():
    res = requests.get('https://api.coingecko.com/api/v3/search/trending')

    return res.json()

