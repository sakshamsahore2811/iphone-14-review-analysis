from bs4 import BeautifulSoup
import requests
import pandas as pd

# Read and store the URLs mentioned in the excel file to a list
df = pd.read_excel('urls.xlsx')
url = df['URLs'].values.tolist()

# Access each URL and copy their textual content to a text file
for i, url in enumerate(url, start=1):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    txt = soup.get_text()

    #Create text files to store the text data from each website
    filename = f"text_data_{i}.txt"
    filepath = f"E:\Data Science 143\Review Article Analysis --iphone 14\Text Data\{filename}" 
    with open(filepath, 'w', encoding="utf-8") as f:
        f.write(txt)
print("Done")
