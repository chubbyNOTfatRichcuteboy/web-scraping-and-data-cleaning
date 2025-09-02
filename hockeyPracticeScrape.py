from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


url = "https://www.scrapethissite.com/pages/forms/?page_num=1"
hockeypage = requests.get(url)
soup = BeautifulSoup(hockeypage.text, 'html.parser')
table = soup.find('table')

# headers
headers = table.find_all('th')
headers = [header.text.strip() for header in headers]

# dataframe
df = pd.DataFrame(columns = headers)

# one page data points
# rows = table.find_all('tr')
# for row in rows[1:]:
#     data = row.find_all('td')
#     formatted = [dp.text.strip() for dp in data]
#     df.loc[len(df)] = formatted

# pagination data points
baseurl = "https://www.scrapethissite.com/pages/forms/?page_num="
pagenum = 1
while True:
    url = f"{baseurl}{pagenum}"
    print(f"Checking page {pagenum}...")
    hockeypage = requests.get(url)
    soup = BeautifulSoup(hockeypage.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    if len(rows) == 1:break
    
    for row in rows[1:]:
        data = row.find_all('td')
        formatted = [dp.text.strip() for dp in data]
        df.loc[len(df)] = formatted

    pagenum+=1
    time.sleep(0.25)

# print DataFrame and convert to INT
numeric_cols = ['Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
print(df)

# data analysis
print(df.isnull().sum())

#export csv
df.to_csv(r"C:\Users\ibobb\Desktop\Python\Books Scraper\fileoutput\HockeyStats.csv", index=False)