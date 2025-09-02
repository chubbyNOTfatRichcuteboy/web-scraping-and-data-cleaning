from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    "User-Agent":"PracticeScrapingArticles"
}

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table', class_="wikitable sortable")
table = tables[1]
th = table.find_all('th')
titles = [title.text.strip() for title in th]
df = pd.DataFrame(columns = titles)
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
print(df)
df.to_csv(r"C:\Users\ibobb\Desktop\Python\Books Scraper\fileoutput\Companies.csv", index=False)
