import requests
from quote_api import QuoteAPI
import os
from dotenv import load_dotenv


def main():
    load_dotenv(r"C:\Coding\.env")
    # Consider storing your API key securely
    api_key = os.getenv("API_NINJAS_KEY")
    quote_api = QuoteAPI(api_key)
    
    category = input("Enter the category (e.g., motivation, happiness): ").lower().strip()
    
    if not category:
        print("Please enter a valid category.")
        return
    
    quotes_list = quote_api.get_quotes(category)
    if quotes_list:
        for index, quote in enumerate(quotes_list, start=1):
            print(f"Quote {index}:")
            print(quote)
    else:
        print("No quotes found.")

if __name__ == "__main__":
    main()
