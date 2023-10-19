import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_url = "https://api.exchangeratesapi.io/v1/latest?access_key={}".format(os.get_env("EXCHANGE_RATES_KEY"))

r = requests.get(api_url)

data = r.json()
print(data)