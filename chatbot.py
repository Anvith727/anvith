def chatbot_response(user_input):
    # Converting user input to lower case for case-insensitive matching
    user_input = user_input.lower()
    
    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a chatbot created to assist you with your queries. You can call me ChatBot!"
    elif "help" in user_input:
        return "Sure! I can help you with information, answer your questions, or just have a chat. What do you need help with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("ChatBot: Hello! I am your assistant chatbot. Type 'bye' to end the conversation.")
    
    while True:
        # Taking input from the user
        user_input = input("You: ")
        
        # Getting the response from the chatbot
        response = chatbot_response(user_input)
        
        # Printing the chatbot's response
        print(f"ChatBot: {response}")
        
        # Ending the conversation if the user says 'bye'
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
