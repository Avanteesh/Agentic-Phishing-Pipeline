import warnings
import requests
import pandas as pd
from os import path
from functools import lru_cache

PHISHTANK_DATASET = path.join("data", "verified_online.csv")

def check_phishtank(url: str):
    warnings.warn("API service unavailable!")
    response = requests.post(
        "http://checkurl.phishtank.com/checkurl/",
        data={"url": url,
            "format": "json",
        },
        headers={
            "User-Agent": "phishing-agent-pipeline/1.0"
        },
    )
    print("HEADERS:", response.headers)
    print("CONTENT TYPE:", response.headers.get("Content-Type"))
    print("TEXT:", response.text[:1000])
    if response.status_code == 200:
        data = response.json()
        if data["in_database"] == True:
            return True
    return False

@lru_cache(maxsize=1)
def load_phishtank_data():
    return pd.read_csv(PHISHTANK_DATASET)

def local_phishtank_search(url: str) -> bool:
    df = load_phishtank_data()
    return (df["url"] == url).any()
