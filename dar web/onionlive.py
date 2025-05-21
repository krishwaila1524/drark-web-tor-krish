import requests
from bs4 import BeautifulSoup
import re

def scrape_onion_live_debug():
    url = "https://onion.live/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        all_links = set()
        # Find all href attributes on the page
        for a in soup.find_all("a", href=True):
            href = a['href']
            if ".onion" in href:
                all_links.add(href)

        print(f"Found {len(all_links)} .onion links:")
        for link in all_links:
            print(link)

    except Exception as e:
        print(f"Error scraping onion.live: {e}")

if __name__ == "__main__":
    scrape_onion_live_debug()
