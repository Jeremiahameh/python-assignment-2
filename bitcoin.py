import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "4e3a5018f7db48c84f768479e0b3c03fa16558ae693eeaf22ffd56fc21a73082"

try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    response.raise_for_status()

    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("Unable to retrieve Bitcoin price")

amount = bitcoins * price

print(f"${amount:,.4f}")
