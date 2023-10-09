import requests

url = "https://partner.shopeemobile.com/api/v2/product/search_item?&attribute_status=2&item_name=apple&offset=0&page_size=10"

payload={}
headers = {

}

response = requests.request("GET",url,headers=headers, data=payload, allow_redirects=False)

print(response.text)