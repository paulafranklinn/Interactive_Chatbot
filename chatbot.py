import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Carregar variáveis de ambiente de um arquivo .env
load_dotenv()
# SITE PARA CONSEGUIR A KEY = https://console.groq.com/keys

groq_api_key = "coloque_a_groq_api_key_aqui"
os.environ["GROQ_API_KEY"] = groq_api_key

# Inicializar o chatbot
chat = ChatGroq(model="llama-3.1-70b-versatile")

print("Chatbot interativo. Digite 'sair' para encerrar a conversa.")

while True:
    # Solicitar uma entrada do usuário
    pergunta = input("Você: ")
    
    # Verificar se o usuário deseja sair
    if pergunta.lower() == 'sair':
        print("Encerrando o chat.")
        break
    
    # Enviar a pergunta e obter resposta
    resposta = chat.invoke(pergunta)
    
    # Exibir a resposta do chatbot
    print("Chatbot:", resposta)
