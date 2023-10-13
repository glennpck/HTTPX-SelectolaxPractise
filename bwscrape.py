import httpx
from selectolax.parser import HTMLParser

class Book:
    def __init__(self, isbn, title, desc, author, cover, type, pb_date, price, url):
        self.isbn = isbn
        self.title = title
        self.desc = desc
        self.author = author
        self.cover = cover
        self.type = type
        self.pb_date = pb_date
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
        except KeyError:
            pass

    pd_check = book.css("p.product-format > span")
    print(pd_check[0].text())
    print(pd_check[1].text())
    pb_date = ""
    type = ""

    # for i in range (len(p_check)):
    #     if i == 0:
    #         type = p_check[i].text()
    #     else:
    #         pb_date = p_check[i].text()
        

    # booktest = Book(
    #     isbn = book.css_first("a.btn").attributes['data-isbn'],
    #     title = book_title,
    #     desc = "testing",
    #     author = book.css_first("p.product-author").text(),
    #     cover = base_url + str(book.css_first("img").attributes['src']),
    #     type = type,
    #     pb_date = pb_date,
    #     price = book.css_first("li.product-price--current").text().strip(),
    #     url = base_url + str(book.css_first("a.product-name").attributes["href"])
    # )
    # print(booktest.title)
    # print(booktest.author)
    # print(booktest.cover)
    # print(booktest.price)
    # print(booktest.url)
    # print(booktest.type)
    # print("")