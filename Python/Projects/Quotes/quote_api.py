import requests


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
