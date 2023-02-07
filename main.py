from fastapi import FastAPI,Request
import uvicorn
from app.routers import crypto,upload,us_stock
from app.page import home
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")
app.include_router(crypto.router)
app.include_router(us_stock.router)
app.include_router(upload.router)
app.include_router(home.router)
templates = Jinja2Templates(directory="templates/")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
