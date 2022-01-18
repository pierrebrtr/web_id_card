from fastapi import FastAPI
from bs4 import BeautifulSoup
import urllib.request
import dateparser
from fastapi.middleware.cors import CORSMiddleware
from website_screenshot import screen_website

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "Hello world"


@app.get("/website/{website_url}")
async def read_item(website_url):
    screen_website(website_url)
    return {"website": website_url}