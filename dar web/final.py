import requests
import socket

# Function to check if Tor is running
def is_tor_running(host="127.0.0.1", port=9150):  # Use 9150 for Tor Browser
    try:
        with socket.create_connection((host, port), timeout=69):
            return True
    except:
        return False

# Function to scan URLs for keywords
def scan_urls(urls, keywords, use_tor=False):
    session = requests.Session()

    if use_tor:
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9150',   # For Tor Browser
            'https': 'socks5h://127.0.0.1:9150'
        }

    for url in urls:
        print(f"\n🔍 Scanning {url}")
        try:
            response = session.get(url, timeout=25)
            found = [kw for kw in keywords if kw.lower() in response.text.lower()]
            if found:
                print(f"[✅ FOUND] Keywords on {url}: {', '.join(found)}")
            else:
                print(f"[❌ NONE] No keywords found on {url}")
        except Exception as e:
            print(f"[🚫 ERROR] Could not access {url} — {e}")

# Main program
def main():
    if not is_tor_running():
        print("[ERROR] Tor is not running on port 9150. Start Tor Browser before running this tool.")
        return

    urls_input = input("🌐 Enter .onion URLs (comma-separated):\n>> ")
    urls = [u.strip() for u in urls_input.split(',') if u.strip()]

    keywords_input = input("🔑 Enter keywords to search (comma-separated):\n>> ")
    keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]

    if not urls or not keywords:
        print("[ERROR] You must enter at least one URL and one keyword.")
        return

    scan_urls(urls, keywords, use_tor=True)

if __name__ == "__main__":
    main()
