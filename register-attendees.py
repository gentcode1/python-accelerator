# Task 1:
# Scenario-Based Weekly Lab Challenge
# Real-World Use Case: Event Registration System
#
# You’ve been hired by a local event management company to build a lightweight 
# Command Line Interface (CLI) tool. This tool must:
#
# Accept attendee registration data (name, age, ticket type)
# Classify them into seating zones based on business rules
# Store the data and generate useful summaries (e.g., how many VIPs, how 
# many youths, etc.)
# This simulates client-facing backend logic like you'd build for admin dashboards or 
# CRM integrations.
#
# Requirements:
# Input Handling: Use input() to collect data from users.
# Data Types: Ensure correct data types (e.g., age as integer, ticket type as
# string).
# Conditional Logic: Use if/elif/else to classify attendees into zones.
# Data Storage: Use lists and dictionaries to store attendee information.
# Output: Print summaries and confirmations to the console.
# Error Handling: Implement basic error handling for invalid inputs.
#
# Sub-Labs / Challenges
# 🔹 Sub-Lab 1: Basic Input and Type Handling
# Focus: Collect attendee details
# Task: Prompt the user to input name, age, and ticket type (VIP or Regular)
# Expected Outcome: Data correctly stored with proper types
# Test Case:
#  Input: John, 28, VIP → Output: Attendee Registered
# 🔹 Sub-Lab 2: Conditional Logic
# Focus: Assign seating zone based on business rules
# Rules Example:
# oUnder 18 = Youth Zone
# o18+ and ticket type is Regular = Standard Zone
# oAny age and ticket type is VIP = VIP Zone
# Expected Outcome: User is placed in correct zone using if/elif/else
# Test Case:
#  Input: Age = 16, Ticket = Regular → Output: Youth Zone
# 🔹 Sub-Lab 3: Modular Function Design
# Focus: Break the logic into reusable functions

# Tasks:
# get_attendee_info()
# assign_zone(age, ticket_type)
# store_attendee(data)
# print_summary()

# Expected Outcome: Organized, reusable codebase

# Test Case:
#  Calling get_attendee_info() returns a dictionary:
#  {'name': 'Alice', 'age': 22, 'ticket': 'VIP'}
# 🔹 Sub-Lab 4: Using Data Structures
# Focus: Store and manage multiple attendee records
# Task: Use a list of dictionaries to store data
# Bonus: Generate summaries such as:
# oNumber of attendees per zone
# oAverage age of attendees
# Expected Outcome: Able to iterate over and summarize stored records
# Test Case:
#  Input: 5 attendees with varying ages and ticket types
#  Output: Total VIP attendees: 5, Youth: 2, Average age: 26.4
# Key Takeaways
# Python syntax must be clean and consistently indented
# Variables should be descriptive and appropriately typed
# Using input() and type() effectively enables robust CLI apps
# Conditional logic controls how programs respond dynamically
# Functions provide modularity, clarity, and testability
# Lists and dictionaries are vital tools for storing and working with data 





attendees = []

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if not name or not all(c.isalpha() or c.isspace() for c in name):
            print("Name must contain only letters and spaces. Please enter a valid name.")
        else:
            return name

def get_valid_age():
    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            if age >= 0:
                return age
            else:
                print("Age cannot be negative.")
        else:
            print("Invalid input for age. Please enter a valid number.")

def get_valid_ticket_type():
    while True:
        ticket_type = input("Enter ticket type (VIP/Regular): ").strip()
        if ticket_type.lower() == "vip" or ticket_type.lower() == "regular":
            return ticket_type.capitalize() if ticket_type.lower() == "regular" else "VIP"
        else:
            print("Invalid ticket type. Please enter VIP or Regular.")

def get_attendee_info():
    name = get_valid_name()
    age = get_valid_age()
    ticket_type = get_valid_ticket_type()
    return name, age, ticket_type
    

def assign_zone(age, ticket_type):
    if age < 18:
        return "Youth Zone"
    elif age >= 18 and ticket_type == "Regular":
        return "Regular Zone"
    else:
        return "VIP Zone"

def store_attendee_info(attendee):
    attendee["zone"] = assign_zone(attendee["age"], attendee["ticket"])
    attendees.append(attendee)
   
def print_summary():
    print("\nSummary of registered attendees:")
    if not attendees:
        print("No attendees registered.")
    else:
        for attendee in attendees:
            print(f" Name: {attendee['name']}, Age: {attendee['age']}, Zone: {attendee['zone']}")
        print(f"\nThank you for registering! Total attendees: {len(attendees)}.")

def main():
    print("Welcome to the Event Registration System!")
    while True:
        name, age, ticket_type = get_attendee_info()
        attendee = {"name": name, "age": age, "ticket": ticket_type}
        store_attendee_info(attendee)
        print(f"{attendee['name']} registered in {attendee['zone']}.")
        more = input("Register another attendee? (y/n): ").strip().lower()
        if more != 'y':
            break
    print_summary()
    print("\nGoodbye!")

main()