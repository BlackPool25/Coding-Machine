import requests
import os
from dotenv import load_dotenv

class QuoteAPI:
    def __init__(self, api_key) -> None:
        self.api_url = 'https://api.api-ninjas.com/v1/quotes'
        self.headers = {'X-Api-Key': api_key}

    def get_quotes(self, category):
        try:
            response = requests.get(f'{self.api_url}?category={category}', headers=self.headers)
            if response.status_code == 200:
                quotes_data = response.json()
                if quotes_data:
                    return [f"By {quote['author']}: \n\n{quote['quote']}" for quote in quotes_data]
                else:
                    print(f"No quotes available for category '{category}'.")
            else:
                print(f"Failed to fetch quotes. Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")
        return []

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
