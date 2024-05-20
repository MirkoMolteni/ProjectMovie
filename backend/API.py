from key import TMDBKey
from key import TMDBReadAccessToken
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend/index.html", "r") as file:
        html = file.read()
    return HTMLResponse(content=html)
