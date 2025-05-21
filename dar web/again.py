import requests
from bs4 import BeautifulSoup
import time

# Set Tor proxy (Tor must be running)
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Scrape .onion links from Ahmia
def get_onion_links_from_ahmia(pages=3):
    onion_links = set()
    for page in range(1, pages + 1):
        print(f"[+] Scraping Ahmia page {page}")
        url = f"https://ahmia.fi/search/?q=.onion&page={page}"
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            results = soup.find_all('a', href=True)
            for link in results:
                href = link['href']
                if ".onion" in href:
                    onion_links.add(href.strip('/'))
            time.sleep(2)
        except Exception as e:
            print(f"[!] Error scraping page {page}: {e}")
    return list(onion_links)

# Check if onion site is live via Tor
def is_site_live(url):
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.status_code == 200
    except:
        return False

# Main logic
def main():
    onion_links = get_onion_links_from_ahmia(pages=5)  # You can change page count
    print(f"[!] Total links found: {len(onion_links)}")
    
    live_sites = []
    for link in onion_links:
        if not link.startswith("http"):
            link = "http://" + link
        print(f"[*] Checking: {link}")
        if is_site_live(link):
            print(f"[LIVE] {link}")
            live_sites.append(link)
        else:
            print(f"[DEAD] {
