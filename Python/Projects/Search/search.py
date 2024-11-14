import requests
import os
from search_art import logo


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    

def google_search(query, num_results=10):
    # Define the base URL for Google's custom search API
    api_url = "https://www.googleapis.com/customsearch/v1"

    # Replace with your actual API key and search engine ID
    api_key = "AIzaSyBAnd1qz1sJJkzVENHLHAaQ9DWk2qXoM48"
    cx = "f5c78193512d04765"

    # Parameters for the search request
    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": num_results
    }

    # Send the request to the API
    response = requests.get(api_url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        results = response.json()
        items = results.get("items", [])
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item['title']}")
            print(f"   Link: {item['link']}")
            print(f"   Snippet: {item['snippet']}")
            print()
    else:
        print("Failed to retrieve results:", response.status_code, response.text)

# Example usage
clear()
print(logo)
search_term = input("Enter search query: ")
google_search(search_term)
