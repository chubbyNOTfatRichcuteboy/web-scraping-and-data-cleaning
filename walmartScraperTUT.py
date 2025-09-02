from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

HEADERS = {
    "accept":"*/*",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"en-US,en;q=0.9",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

# HEADERS = {
#     "accept":"application/json",
#     "accept-encoding":"gzip,deflate,br,ztsd",
#     "accept-language":"en-US",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
# }


def get_product_links(query, page_number=1):


    search_url = f"https://www.walmart.com/search?q={query}&page={page_number}"
    response = requests.get(search_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    product_links = []

    for link in links:
        if "/ip" in link['href']:
            if "https" in link['href']:
                full_url = link['href']
            else:
                full_url = "https://walmart.com" + link['href']
            product_links.append(full_url)


    print(product_links)
    return product_links

def extract_product_info(product_url):
    html = requests.get(product_url, headers=HEADERS).text


    soup = BeautifulSoup(html, 'html.parser')
    walmartjson = soup.find('script', id="__NEXT_DATA__")

    data = json.loads(walmartjson.string)
    initial_data = data["props"]["pageProps"]["initialData"]["data"]
    product_data = initial_data["product"]
    reviews_data = initial_data.get("reviews", {})

    product_info = {
        "price": product_data["priceInfo"]["currentPrice"]["price"],
        "review_count": reviews_data.get("totalReviewCount", 0),
        "item_id": product_data["usItemId"],
        "avg_rating": reviews_data.get("averageOverallRating", 0),
        "product_name": product_data["name"],
        "brand": product_data.get("brand", ""),
        "availability": product_data["availabilityStatus"],
        "short_description": product_data.get("shortDescription", "")
    }
    return product_info

# Turn json to pandas DF
def jsonToDF(file):
    products = []
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    product = json.loads(line)
                    products.append(product)
                except json.JSONDecodeError as e:
                    print(f"Error parsing line: {line}, error: {e}")
    
    df = pd.DataFrame(products)
    df = df.drop_duplicates(subset=['item_id'], keep='first')
    df = df.reset_index(drop=True)
    return df

# Clean DF
def cleanDF(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce')
    df['item_id'] = pd.to_numeric(df['item_id'], errors='coerce')
    df['avg_rating'] = pd.to_numeric(df['avg_rating'], errors='coerce')

    df['short_description'] = df['short_description'].str.replace('<[^<]+?>', '', regex=True)
    df['short_description'] = df['short_description'].str.replace('\n', '', regex=True)
    df['short_description'] = df['short_description'].str.strip()

    df['availability'] = df['availability'].astype('category')
    df['brand'] = df['brand'].astype('category')
    df.to_csv(r"C:\Users\ibobb\Desktop\Python\Books Scraper\fileoutput\Walmart.csv", index=False)
    return df



def main(query):
    OUTPUT_FILE = "product_info.json"
    with open(OUTPUT_FILE, 'w') as file:
        pagenum = 1
        while True:
            links = get_product_links(query, pagenum)
            if not links or pagenum > 9:
                break

            for link in links:
                try:
                    product_info = extract_product_info(link)
                    if product_info:
                        file.write(json.dumps(product_info)+"\n")
                except Exception as e:
                    print(f"Failed to process URL {link}, Error {e}")
            pagenum += 1
            print(f"Search page {pagenum}")

if __name__ == "__main__":
    query = input("what would you like to search on walmart? ")
    main(query)
    df = jsonToDF("product_info.jsonl")
    df = cleanDF(df)
    print(df.sort_values('price', ascending=False))
    pass

