import httpx
from selectolax.parser import HTMLParser

class Book:
    def __init__(self, isbn, title, author, cover, type, price, url):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.cover = cover
        self.type = type
        self.price = price
        self.url = url

url = "https://wordery.com/search?term=eighty+six"

base_url = "https://wordery.com"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
for book in parse.css("li.o-book-list__book"):

    price = ''
    try:
        price = book.css_first("span.c-book__price").text().strip()
    except AttributeError:
        price = 'Unavailable'

    booktest = Book(
        isbn = book.css_first("div").attributes['data-isbn13'],
        title = book.css_first("a.c-book__title").text(),
        author = book.css_first("span > a").text(),
        cover = base_url + str(book.css_first("img").attributes['data-lz-src']),
        type = book.css_first("small.c-book__meta").text(),
        price = price,
        url = base_url + str(book.css_first("a").attributes["href"])
    )
    print(booktest.title)
    print(booktest.author)
    print(booktest.cover)
    print(booktest.price)
    print(booktest.url)
    print("")