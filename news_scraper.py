#created by Minakshi
import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

try:
    # Step 1: Fetch HTML from the URL
    response = requests.get(url)
    response.raise_for_status()   # Check for errors

    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract headlines (BBC uses h2)
    headlines = soup.find_all("h2")

    # Step 4: Save headlines into a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("Top News Headlines:\n\n")

        for h in headlines:
            title = h.get_text().strip()
            if title:
                file.write("- " + title + "\n")

    print("Headlines scraped successfully and saved to headlines.txt")

except Exception as e:
    print("Error occurred:", e)