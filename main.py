from fastapi import FastAPI,Request
import uvicorn
from routers import crypto
from page import home
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(crypto.router)
app.include_router(home.router)
templates = Jinja2Templates(directory="templates/")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
