from trivia_api import TriviaAPI
import os
from dotenv import load_dotenv


def main():
    load_dotenv(r'C:\Coding\.env')
    api_key = os.getenv('API_NINJAS_KEY')
    trivia_api = TriviaAPI(api_key)
    category = input("Enter category: ").strip().lower()

    if not category:
        print("Enter a valid category.")
        return
    
    question_list = trivia_api.get_trivia(category)
    if question_list:
        score = trivia_api.ask_question(question_list)
        print(f"Your final score is {score}")
    
    else:
        print("No trivia found")
    

if __name__ == "__main__":
    main()

