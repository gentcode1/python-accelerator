import random;
import datetime

questions = [
    "What is the primary goal of marketing analytics?",
    "Name three common metrics used in marketing analytics.",
    "How can customer segmentation improve marketing strategies?",
    "What role does data visualization play in marketing analytics?",
    "Explain the concept of A/B testing in marketing.",
    "What are some challenges faced in marketing analytics?",
    "How can predictive analytics be applied in marketing?",
    "What is the difference between descriptive and prescriptive analytics in marketing?",
    "How can social media analytics benefit marketing campaigns?",
    "What tools are commonly used for marketing analytics?"
]
def get_random_question():
    return random.choice(questions)

def get_valid_response(question):
    while True:
        response = input(f"{question}\nYour answer: ")
        if response.strip():
            return response
        print("Response cannot be empty. Please try again.")


def record_survey_response(question, response, filename="survey_responses.txt"):
   with open(filename, "a") as file:
       file.write(f"Q: {question}\n A: {response} at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
