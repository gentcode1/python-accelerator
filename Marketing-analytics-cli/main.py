# Scenario-Based Weekly Lab Challenge 
# -------------------------------------
# Problem Scenario: A marketing analytics team requests a CLI tool to conduct a simple 
# customer survey simulation. The tool will randomly choose a survey question, collect 
# responses from the user, validate them, and store results in a structured format. The code 
# must be modular, handle all unexpected input, and use built-in libraries like random, 
# datetime, and os for realistic context. 

# Sub-Labs / Challenges 
# 
# 
# 🔹 Sub-Lab 1: Modular Function Creation 
#
# • Focus: Break survey flow into multiple functions 
# • Task: Create functions for greeting, asking a question, and recording a response 
# • Outcome: Clear, callable logic for each action 
# • Test Case: User receives dynamic greeting and valid questions 

#   Sub-Lab 2: Handling Invalid Inputs
#  
# • Focus: Validate user responses 
# • Task: Handle cases where input is empty, out of range, or invalid 
# • Outcome: Robust response collection without crashes 
# • Test Case: Empty response triggers retry message  Sub-Lab 3: Using Built-in Modules 
# • Focus: Use random to pick survey questions; datetime to timestamp responses 
# • Task: Generate random question, store answer with timestamp 
# • Outcome: Realistic behavior simulating live survey systems 
# • Test Case: Output logs include timestamped entries 

#   Sub-Lab 4: Organizing Code with Modules 
# 
# • Focus: Split code across files using Python modules 
# • Task: Move functions into separate .py files and import them 
# • Outcome: Clean, maintainable codebase 
# • Test Case: main.py runs using imported functions

from user import get_user_greeting
from survey_utils import get_random_question, get_valid_response, record_survey_response

def main():
    print(get_user_greeting())
    
    question = get_random_question()
    response = get_valid_response(question)
    
    record_survey_response(question, response)
    print("Thank you for your response! It has been recorded.")

if __name__ == "__main__":
    main()