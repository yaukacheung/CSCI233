# pip install requests

import requests
from datetime import datetime, timezone

# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3"


def get_crypto_price(coin_id):
    """Fetch cryptocurrency price from CoinGecko."""

    url = f"{API_URL}/simple/price"

    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_last_updated_at": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        if coin_id not in data or "usd" not in data[coin_id]:
            print("Cryptocurrency not found.")
            return

        price = data[coin_id]["usd"]

        # Get timestamp
        timestamp = data[coin_id].get("last_updated_at")

        if timestamp:
            updated = datetime.fromtimestamp(
                timestamp, timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S UTC")
        else:
            updated = "Timestamp unavailable"

        print(f"\n{coin_id.upper()}")
        print(f"Price: ${price:,.2f}")
        print(f"Last Updated: {updated}")

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")


# Main program
def main():

    print("===== CRYPTO TRACKER =====")

    # Default cryptocurrencies
    coins = ["bitcoin", "ethereum", "dogecoin"]

    print("\nCurrent Cryptocurrency Prices:")

    for coin in coins:
        get_crypto_price(coin)

    # User search challenge
    while True:
        print("\n===== SEARCH CRYPTO =====")

        coin_name = input(
            "Enter a cryptocurrency name (or 'exit' to quit): "
        ).strip().lower()

        if coin_name == "exit":
            print("Thank you for using Crypto Tracker!")
            break

        if not coin_name:
            print("Please enter a cryptocurrency name.")
            continue

        get_crypto_price(coin_name)


# Run program
if __name__ == "__main__":
    main()
