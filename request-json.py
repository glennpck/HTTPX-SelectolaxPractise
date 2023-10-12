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

url = "https://blackwells.co.uk/bookshop/search/?keyword=eighty+six"

base_url = "https://blackwells.co.uk"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
for book in parse.css("li.search-result__item "):
    div_check = book.css("a.product-name")
    book_title = ''
    for node in div_check:
        try:
            validateValue = node.attributes['itemprop']
            book_title = node.text()
            print(book_title)
        except KeyError:
            pass
    booktest = Book(
        isbn = book.css_first("a.btn").attributes['data-isbn'],
        title = book_title,
        author = book.css_first("p.product-author").text(),
        cover = base_url + str(book.css_first("img").attributes['src']),
        type = "Paperback",
        price = book.css_first("li.product-price--current").text().strip(),
        url = base_url + str(book.css_first("a.product-name").attributes["href"])
    )
    print(booktest.title)
    print(booktest.author)
    print(booktest.cover)
    print(booktest.price)
    print(booktest.url)
    print("")