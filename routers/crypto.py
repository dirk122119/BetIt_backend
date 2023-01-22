from fastapi import APIRouter

router=APIRouter()
@router.get("/crypto", tags=["crypto"])
def crypto_index():
    return {"crypto index"}

@router.get("/crypto/{username}", tags=["crypto"])
async def read_user(username: str):
    return {"crypto": username}

