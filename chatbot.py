import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from a .env file
load_dotenv()
groq_api_key = "insert_your_groq_api_key_here"
os.environ["GROQ_API_KEY"] = groq_api_key

# Initialize the chatbot
chat = ChatGroq(model="llama-3.1-70b-versatile")

print("Interactive chatbot. Type 'exit' to end the conversation.")

while True:
    # Prompt the user for input
    question = input("You: ")
    
    # Check if the user wants to exit
    if question.lower() == 'exit':
        print("Ending the chat.")
        break
    
    # Send the question and get the response
    response = chat.invoke(question)
    
    # Display the chatbot's response
    print("Chatbot:", response)

