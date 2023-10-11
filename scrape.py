import httpx
from selectolax.parser import HTMLParser

from dataclasses import dataclass, asdict

@dataclass
class Product:
    image: str
    title: str
    price: str
    num_sold: str

def get_html():
    url = f'https://shopee.sg/search?keyword=nike'
    resp = httpx.get(url)
    return HTMLParser(resp.text)

def parse_products(html):
    products = html.css('div.VTjd7p whIxGK')
    results = []
    for item in products:
        text_title = item.css_first("div.ie3A+n bM+7UW Cve6sh").text()
        print(text_title)
        new_item = Product(
            image=item.css_first("img._7DTxhh tWoeMk").text(),
            title=item.css_first("div.ie3A+n bM+7UW Cve6sh").text(),
            price=item.css_first("span.ZEgDH9").text(),
            num_sold=item.css_first("div.r6HknA uEPGHT").text()
        )
        results.append(asdict(new_item))

    return results

def main():
    html = get_html()
    print(html)
    res = parse_products(html)
    ##print(res)

if __name__ == "__main__":
    main()