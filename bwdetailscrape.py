import httpx
from selectolax.parser import HTMLParser

def get_title(item):
    print(item.css_first("img").attributes)


url = "https://blackwells.co.uk/bookshop/product/9781974740581"

base_url = "https://blackwells.co.uk"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
page = parse.css("div.container--50")

desc = page[1].css("div")
print(desc[2])

# author_list = page[0].css("p.product__author > a")
# for node in author_list:
#     print(node.text(strip=True, deep=False))

# plist = page[1].css("p")
# if page[1].css_first("font"):
#     print(page[1].css_first("font").text(strip=True, deep=False))
# elif len(plist) == 1:
#     print(plist[0].text(deep=False, strip=True))
# elif len(plist) == 2:
#     print(plist[0].text(deep=False, strip=True))
# else:
#     print(plist[1].text(strip=True, deep=False))