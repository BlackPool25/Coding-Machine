import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    user_input = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    inrresponse = requests.get("https://www.floatrates.com/daily/usd.json")
    price_dict = inrresponse.json()
    user_price = o["bpi"]["USD"]["rate_float"] * user_input * price_dict["inr"]["rate"]
    formatted_price = format(user_price, ",.4f", )
    print(f"{formatted_price} inr")
except requests.RequestException:
    pass