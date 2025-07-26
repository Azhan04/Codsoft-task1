def chatbot():

    rules = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm a chatbot, so I don't have feelings, but thanks for asking!",
        "what is your name": "My name is ChatBot.",
        "what do you do": "I can answer some basic questions based on predefined rules.",
        "goodbye": "Goodbye! Have a great day!",
        "exit": "Thanks For Chatting. Goodbye!"
    }

    print("Chatbot: Hello! Type 'exit' to end our conversation.")

    while True:
        user_input = input("You: ").lower() 

        if user_input == "exit":
            print("Chatbot: Thanks For Chatting. Goodbye!")
            break

        response_found = False  

        for pattern, response in rules.items():
            if pattern in user_input:
                print("Chatbot:", response)
                response_found = True
                break  

        if not response_found:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase it please?")

chatbot()