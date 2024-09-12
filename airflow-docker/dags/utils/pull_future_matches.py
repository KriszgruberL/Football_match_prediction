from datetime import datetime
import logging
from bs4 import BeautifulSoup
import requests
import os 
import pandas as pd
import re 

url = "https://www.walfoot.be/belgique/jupiler-pro-league/calendrier"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": f"{url}",
}
        
response = requests.get(f"{url}", headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    weeks = soup.find_all("a", id=re.compile(r"^calendar_matchday_"))

    for week in weeks:
        print (week)
    