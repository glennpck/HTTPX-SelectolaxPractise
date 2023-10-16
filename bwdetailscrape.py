import httpx
from selectolax.parser import HTMLParser


url = "https://blackwells.co.uk/bookshop/product/86-Eighty-Six-8-by-Asato-Asato-author-Shirabii-illustrator/9781975320768"

base_url = "https://blackwells.co.uk"

resp = httpx.get(url)
parse = HTMLParser(resp.text)
page = parse.css("div.container--50")

title_list = page[0].css_first("h1.product__name").text(strip=True, deep=False).split(" ")
title = ""
for word in title_list:
    if "\t" not in word:
        title += word

print(title)
# plist = page[1].css("p")
# if page[1].css_first("font"):
#     print(page[1].css_first("font").text(strip=True, deep=False))
# elif len(plist) == 1:
#     print(plist[0].text(deep=False, strip=True))
# elif len(plist) == 2:
#     print(plist[0].text(deep=False, strip=True))
# else:
#     print(plist[1].text(strip=True, deep=False))