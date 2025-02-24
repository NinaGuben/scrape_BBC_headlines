import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code != 200:
    print("Error: {response.status_code} - {response.text}")
else:
    print("Website information accessible")
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2", class_= "sc-8ea7699c-3 dhclWg")
    for headline in headlines:
     print(headline.get_text())
     print("........................")



