import requests

def scan_urls(urls, keywords, use_tor=False):
    session = requests.Session()

    if use_tor:
        # Route traffic through Tor SOCKS5 proxy
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

    for url in urls:
        print(f"\nScanning {url}")
        try:
            response = session.get(url, timeout=25)
            found = [kw for kw in keywords if kw.lower() in response.text.lower()]
            if found:
                print(f"[OK] Found keywords on {url}: {', '.join(found)}")
            else:
                print(f"[OK] No keywords found on {url}")
        except Exception as e:
            print(f"[ERROR] Could not access {url} — {e}")

def main():
    urls = [
        "http://darkfailenbsdla5mal2mxn2uz66od5vtzd5qozslagrfzachha3f3id.onion/",
        "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/",
        "http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/"
    ]

    keywords = ["meth", "cocaine", "national", "fentanyl", "drug", "weapon", "terror", "darkweb"]
    scan_urls(urls, keywords, use_tor=True)

if __name__ == "__main__":
    main()
