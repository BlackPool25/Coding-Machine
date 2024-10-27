import requests

class TriviaAPI:
    def __init__(self, api_key) -> None:
        self.trivia_url = 'https://api.api-ninjas.com/v1/trivia'
        
        self.headers = {'X-Api-Key': api_key}

    def get_trivia(self, category):
        try:
            response = requests.get(f"{self.trivia_url}?category={category}", headers = self.headers)
            if response.status_code == 200:
                trivia_data = response.json()
                if trivia_data:
                    return trivia_data
                else:
                    print(f"No trivia available for category '{category}'.")
            else:
              print(f"Failed to fetch trivia. Status Code: {response.status_code}") 
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")
        return []

    def ask_question(self, questions):
        score = 0
        for individual_question in questions:
            question = individual_question["question"]
            answer = individual_question["answer"].lower()
            num = questions.index(individual_question) + 1
            print(f"Question {num}: ")
            print(question)
            user_answer = input("Your answer: ").lower().strip()
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        return score
