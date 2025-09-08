
# Q1.To design a simple rule-based chatbot in Python that responds to user greetings and basic queries. 
choice = input("Enter 1 to start chatting: ")
if choice == "1":
    user_input = input("You: ").lower()
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")
    elif "how are you" in user_input:
        print("Bot: I'm fine, thank you! How are you?")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day!")
    else:
        print("Bot: I'm not sure how to respond to that.")
