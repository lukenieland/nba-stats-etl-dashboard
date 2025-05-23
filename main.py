import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
import os

url_format = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"
years = list(range(2000,2026))
dfs = []

#creates stats folder if it does not exist
os.makedirs("stats", exist_ok=True)

#scrapes html files for specified years
for year in years:
    url = url_format.format(year)
    data = requests.get(url)

    with open("stats/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)

#parses basketball reference html
for year in years:
    with open("stats/{}.html".format(year), encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")
    stat_table = soup.find(id="per_game_stats")
    stat = pd.read_html(StringIO(str(stat_table)))[0]
    stat["Year"] = year
    dfs.append(stat)

#creates csv file
stats = pd.concat(dfs)
stats.to_csv("stats.csv")
