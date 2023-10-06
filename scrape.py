import httpx
from selectolax.parser import HTMLParser

from dataclasses import dataclass, asdict

@dataclass
class Product:
    manufacturer: str
    title: str
    price: str

def get_html(page):
    url = f'https://www.thomann.de/intl/all-products-from-the-category-electric-guitars.html?ls=25&pg={page}'
    resp = httpx.get(url)
    return HTMLParser(resp.text)

def main():
    for i in range(1, 4):
        html = get_html(i)
        print(html.css_first("title").text())

if __name__ == "__main__":
    main()