import requests
import re

def scrape_ahmia_urls():
    url = "https://ahmia.fi/"  # fixed URL
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("[*] Scraping .onion URLs from Ahmia...")

    try:
        response = requests.get(url, headers=headers)
        onion_links = re.findall(r'http://[a-zA-Z0-9]{16,56}\.onion', response.text)
        onion_links = list(set(onion_links))  # Remove duplicates

        with open("urls.txt", "w") as f:
            for link in onion_links:
                f.write(link + "\n")

        print(f"[DONE] Scraped and saved {len(onion_links)} .onion URLs to urls.txt")

    except Exception as e:
        print(f"[ERROR] Failed to scrape Ahmia: {e}")

if __name__ == "__main__":
    scrape_ahmia_urls()
