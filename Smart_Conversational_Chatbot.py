# ==============================
#      RULE-BASED CHATBOT
# ==============================

import datetime
import random

# Bot Introduction
print("=" * 45)
print("WELCOME TO SMART CHATBOT")
print("=" * 45)
print("Type 'bye' anytime to exit.\n")

# Random greeting responses
greetings = [
    "Hello!",
    "Hi there!",
    "Hey! Nice to meet you!"
]

# Random goodbye responses
goodbyes = [
    "Goodbye! Have a great day!",
    "See you soon!",
    "Bye! Take care!"
]

# Joke list
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "Why do Python programmers wear glasses? Because they can't C!"
]

while True:

    # Taking user input
    user = input("You: ").lower().strip()

    # Greeting
    if user in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    # Asking bot name
    elif "your name" in user:
        print("Bot: My name is SmartBot.")

    # Asking about chatbot
    elif "who are you" in user:
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    # Asking how are you
    elif "how are you" in user:
        print("Bot: I am doing great! Thanks for asking.")

    # Asking time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Asking date
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # Help command
    elif "help" in user:
        print("\nBot: I can respond to these commands:")
        print(" - hi / hello")
        print(" - your name")
        print(" - who are you")
        print(" - how are you")
        print(" - time")
        print(" - date")
        print(" - joke")
        print(" - bye\n")

    # Joke section
    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    # Simple math
    elif "2+2" in user:
        print("Bot: 2 + 2 = 4")

    # Asking favorite color
    elif "favorite color" in user:
        print("Bot: My favorite color is blue.")

    # Goodbye
    elif user == "bye":
        print("Bot:", random.choice(goodbyes))
        break

    # Empty input
    elif user == "":
        print("Bot: Please type something.")

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")


print("\nChat Ended Successfully!")