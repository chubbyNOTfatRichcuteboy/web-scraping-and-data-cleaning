from bs4 import BeautifulSoup
import requests, time, os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def webScrape():
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
    print("Finished checking")

    # print DataFrame and convert to INT
    numeric_cols = ['Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    print(df)
    # export csv
    df.to_csv(r"C:\Users\ibobb\Desktop\Python\Web Scraping\fileoutput\HockeyStats.csv", index=False)

# open csv to skip scraping for testing purposes
def openCSV():
    return(pd.read_csv('Web Scraping/fileoutput/HockeyStats.csv'))





# matplotlib
def plot(df):
    # # Vertical bar
    # team_win_percent = df.groupby('Team Name')['Win %'].mean()
    # plt.figure(figsize=(15, 10))
    # plt.subplot(2, 2, 1)
    # plt.bar(team_win_percent.index, team_win_percent.values, color='blue', alpha=0.7, edgecolor='black')
    # plt.title("Average Win Rate Per Team", fontsize=8)
    # plt.xlabel("Team", fontsize=8)
    # plt.ylabel("Average win rate", fontsize=8)
    # plt.xticks(rotation=90,ha='center',fontsize=6)

    # horizontal bar
    team_win_percent = df.groupby('Team Name')['Win %'].mean()
    sorted_teams = team_win_percent.sort_values(ascending=True)
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1)
    bars = plt.barh(range(len(sorted_teams)), sorted_teams.values, color='steelblue', alpha=0.7, edgecolor='black')
    plt.title("Average Win Rate Per Team", fontsize=8)
    plt.xlabel("Average Win Rate", fontsize=8)
    plt.ylabel("Team", fontsize=8)
    plt.yticks(range(len(sorted_teams)),sorted_teams.index, fontsize=8)


    plt.subplot(2, 2, 2)
    scatter = plt.scatter(df['Goals For (GF)'], df['Goals Against (GA)'], c=df['Win %'], cmap='RdYlGn', s=10, alpha=0.7)
    plt.xlabel("Goals For", fontsize=8)
    plt.ylabel("Goals Against", fontsize=8)
    plt.title("Team Performance: Offense vs Defense", fontsize=8)
    plt.colorbar(scatter, label='Win Percent')

    # for i, row in df.iterrows():
    #     if i % 20 == 0:
    #         annotatetext = f"{row['Team Name']} '{str(row['Year'])[-2:]}"
    #         plt.annotate(annotatetext, (df['Goals For (GF)'].iloc[i], df['Goals Against (GA)'].iloc[i]), xytext=(5,5), textcoords='offset points', fontsize=6,
    #         bbox=dict(boxstyle="round,pad=0.2", facecolor="white",alpha=0.4),
    #         arrowprops=dict(arrowstyle="->",color="black",lw=0.5))

    highestwinpercent = df.loc[df['Win %'].idxmax()]
    lowestwinpercent = df.loc[df['Win %'].idxmin()]
    mostgf = df.loc[df['Goals For (GF)'].idxmax()]
    leastgf = df.loc[df['Goals For (GF)'].idxmin()]
    mostga = df.loc[df['Goals Against (GA)'].idxmax()]
    leastga = df.loc[df['Goals Against (GA)'].idxmin()]

    poi = [highestwinpercent, lowestwinpercent, mostgf, leastgf, mostga, leastga]
    for point in poi:
        annotatetext = f"{point['Team Name']} '{str(point['Year'])[-2:]}"
        plt.annotate(annotatetext,
        (point['Goals For (GF)'], point['Goals Against (GA)']),
        xytext=(15,15),
        textcoords='offset points',
        arrowprops=dict(arrowstyle="->",color="black",lw=0.5))



    plt.subplot(2, 2, 3)
    showteams = ['San Jose Sharks', 'Edmonton Oilers', 'New York Rangers', 'Detroit Red Wings']
    for team in showteams:
        teamdata = df[df['Team Name'] == team]
        plt.plot(teamdata['Year'], teamdata['Wins'], marker='o', linewidth=1, label=team)
    plt.title("Team Wins vs Time", fontsize=12)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Wins', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)



    plt.subplot(2, 2, 4)
    count, bin_edges, patches = hist = plt.hist(df['Losses'], bins=32, edgecolor='black')
    cmap = plt.colormaps.get_cmap('coolwarm')
    norm = plt.Normalize(count.min(), count.max())
    for i, patch in enumerate(patches):
        patch.set_facecolor(cmap(norm(count[i])))
    plt.title("Single season losses frequency", fontsize=12)
    plt.xlabel("Single season losses", fontsize=12)
    plt.ylabel('How many times a loss total was achieved', fontsize=12)

    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca())
    cbar.set_label('Frequency Count', fontsize=10)




    plt.tight_layout()
    plt.show()





def main():
    # webScrape()
    df = openCSV()
    plot(df)

if __name__ == "__main__":
    main()

