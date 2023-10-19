import httpx
from selectolax.parser import HTMLParser
from forex_python.converter import CurrencyRates
from decimal import Decimal

c = CurrencyRates(force_decimal=True)

class Book:
    def __init__(self, isbn, title, author, cover, type, price, url):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.cover = cover
        self.type = type
        self.price = price
        self.url = url

url = "https://wordery.com/spy-classroom-vol-2-light-novel-takemachi-9781975322427?cTrk=MjAxNDY5NzE2fDY1MzA5YTY0MmE4M2U6MTo0OjY1MzA4ZTgzMzU1Yzk1LjMzMTE0NjgwOmJiZTkyNjVi"

base_url = "https://wordery.com"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
page = parse.css_first("div.o-layout--huge")

price = "Unavailable on this platform"
print(page.css_first("strong.u-fs--ex").attributes)
usd_price = page.css_first("strong.u-fs--ex").text().replace("$", "")
print(usd_price)
price = c.convert('USD', 'SGD', float(usd_price.replace("$", "")))
print(price)