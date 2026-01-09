import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print("URL RECEIVED:", url)

    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch Wikipedia page, status={response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    paragraphs = soup.select("p")
    text = "\n".join(p.get_text() for p in paragraphs[:20])

    if not text.strip():
        raise Exception("Wikipedia page has no readable content")

    sections = [h.get_text(strip=True) for h in soup.select("h2 span.mw-headline")]

    return title, text, sections
