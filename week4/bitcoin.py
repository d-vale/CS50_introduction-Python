import sys
import requests

# CoinCap API key — replace with your own key from pro.coincap.io/dashboard
API_KEY = "YOUR_API_KEY_HERE"

def main():
    # Ensure the user provided exactly one command-line argument
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # Try to convert the argument to a float (number of Bitcoins to buy)
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Query the CoinCap API for the current Bitcoin price in USD
    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        )
        response.raise_for_status()
        data = response.json()
        # Extract the current price from the nested JSON response
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not retrieve Bitcoin price")

    # Calculate total cost and display it with 4 decimal places and comma separator
    total = n * price
    print(f"${total:,.4f}")

main()
