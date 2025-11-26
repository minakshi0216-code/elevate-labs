# Simple Rule-Based Chatbot using if-else
#by Minakshi
print("chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")
    
    elif "name" in user:
        print("Chatbot: I am a rule-based chatbot created using Python.")
    
    elif "help" in user:
        print("Chatbot: I can answer basic questions. Try saying hello or ask my name.")
    
    elif "weather" in user:
        print("Chatbot: I cannot check weather, but I hope it's nice where you are!")
    
    elif user == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I didn't understand that.")