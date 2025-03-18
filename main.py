import requests
from bs4 import BeautifulSoup
import time

def search_google(query):
    """Fetch search results from Google"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Accept-Language": "en-US,en;q=0.5"
    }

    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)

    # Check if Google blocked us
    if "Our systems have detected unusual traffic" in response.text:
        print("🔴 Google blocked the request! Switching to Bing...")
        return search_bing(query)

    # Parse the response
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for g in soup.select("div.tF2Cxc"):
        title = g.select_one("h3").text if g.select_one("h3") else "No title"
        link = g.select_one("a")["href"] if g.select_one("a") else "No link"
        results.append((title, link))

    return results if results else "No relevant results found."

def search_bing(query):
    """Fetch search results from Bing as a fallback"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Accept-Language": "en-US,en;q=0.5"
    }

    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for g in soup.select("li.b_algo"):
        title = g.select_one("h2").text if g.select_one("h2") else "No title"
        link = g.select_one("a")["href"] if g.select_one("a") else "No link"
        results.append((title, link))

    return results if results else "No relevant results found."

if __name__ == "__main__":
    while True:
        query = input("\nEnter your search query (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break

        print(f"\n🔍 Fetching results for: \"{query}\"\n")
        search_results = search_google(query)

        if isinstance(search_results, str):
            print("No relevant results found.")
        else:
            print("📌 Search Results:")
            for i, (title, link) in enumerate(search_results, start=1):
                print(f"{i}. {title}\n   🔗 {link}\n")

        time.sleep(1)  # Add delay to avoid getting blocked
