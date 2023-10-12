import httpx
from selectolax.parser import HTMLParser

base_url = "https://blackwells.co.uk"

url = "https://wordery.com/search?term=Eighty+Six+Light+Novel"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
for book in parse.css("li.o-book-list__book"):
    print(book.css_first("a.c-book__title").text())