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

def parse_products(html):
    products = html.css('div.product')
    results = []
    for item in products:
        new_item = Product(
            manufacturer=item.css_first("span.title__manufacturer").text(),
            title=item.css_first("span.title__name").text(),
            price=item.css_first("div.product__price").text().strip()
        )
        results.append(asdict(new_item))

    return results

def main():
    for i in range(1, 4):
        html = get_html(i)
        res = parse_products(html)
        print(res)

if __name__ == "__main__":
    main()