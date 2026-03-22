import requests
from bs4 import BeautifulSoup

def get_links(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all('a'):
        link = a.get('href')
        if link and "http" in link:
            links.append(link)

    return links[:10]