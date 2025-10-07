# clg Assignment AI/ML 
# Q1.To design a simple rule-based chatbot in Python that responds to user greetings and basic queries. 

# choice = input("Enter 1 to start chatting: ")
# if choice == "1":
#     user_input = input("You: ").lower()
#     if "hello" in user_input or "hi" in user_input:
#         print("Bot: Hello! How can I help you?")
#     elif "how are you" in user_input:
#         print("Bot: I'm fine, thank you! How are you?")
#     elif "bye" in user_input:
#         print("Bot: Goodbye! Have a nice day!")
#     else:
#         print("Bot: I'm not sure how to respond to that.")

# Q2.To implement a reflex agent in Python that decides whether to carry an umbrella or a water bottle.
# print("Menu:")
# print("1. Exit")
# print("2. Weather decision")
# choice = input("Enter your choice (1 or 2): ")
# if choice == "1":
#     print("Exiting...")
# elif choice == "2":
#     weather = input("Enter today's weather: ").lower()
#     if "rain" in weather:
#         print("Agent: Take an umbrella")
#     else:
#         print("Agent: Carry a water bottle")
# else:
#     print("Invalid choice!")

# Q3.To build a calculator that performs arithmetic operations based on user commands.
# ANS.
# choice = input("Enter Your choice : ")
# if choice == "3":
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     op = input("Enter operation (+, -, *, /): ")
#     if op == "+":
#         print("Result:", a + b)
#     elif op == "-":
#         print("Result:", a - b)
#     elif op == "*":
#         print("Result:", a * b)
#     elif op == "/":
#         if b != 0:
#             print("Result:", a / b)
#         else:
#             print("Error: Division by zero")
#     else:
#         print("Invalid operation")

# Q4.To detect the user’s mood based on given text input using keyword matching.
# Ans.
# print("Menu:")
# print("1. Exit")
# print("2. Weather decision")
# print("3. (Reserved)")
# print("4. Mood detection")

# choice = input("Enter your choice (1-4): ")
# if choice == "1":
#     print("Exiting...")
# elif choice == "2":
#     weather = input("Enter today's weather: ").lower()
#     if "rain" in weather:
#         print("Agent: Take an umbrella")
#     else:
#         print("Agent: Carry a water bottle")
# elif choice == "4":
#     text = input("Enter a sentence about your feelings: ").lower()
#     if "happy" in text or "good" in text or "great" in text or "awesome" in text:
#         print("Mood: You seem Happy")
#     elif "sad" in text or "bad" in text or "upset" in text or "unhappy" in text:
#         print("Mood: You seem Sad")
#     elif "angry" in text or "mad" in text or "furious" in text:
#         print("Mood: You seem Angry")
#     else:
#         print("Mood not detected")
# else:
#     print("Invalid choice!")


# Q5.To classify a message as spam or not spam based on keywords.
# ANS.

print("Menu:")
print("1. Exit")
print("2. Weather decision")
print("3. (Reserved)")
print("4. Mood detection")
print("5. Spam classification")

choice = input("Enter your choice (1-5): ")
if choice == "1":
    print("Exiting...")

elif choice == "2":
    weather = input("Enter today's weather: ").lower()
    if "rain" in weather:
        print("Agent: Take an umbrella")
    else:
        print("Agent: Carry a water bottle")

elif choice == "4":
    text = input("Enter a sentence about your feelings: ").lower()
    if "happy" in text or "good" in text or "great" in text or "awesome" in text:
        print("Mood: You seem Happy")
    elif "sad" in text or "bad" in text or "upset" in text or "unhappy" in text:
        print("Mood: You seem Sad")
    elif "angry" in text or "mad" in text or "furious" in text:
        print("Mood: You seem Angry")
    else:
        print("Mood not detected")

# elif choice == "5":
#     message = input("Enter a message: ").lower()
#     if ("win" in message or "free" in message or "lottery" in message or
#         "prize" in message or "money" in message or "click here" in message):
#         print("Classification: Spam Message")
#     else:
#         print("Classification: Not Spam")

# else:
#     print("Invalid choice!")

