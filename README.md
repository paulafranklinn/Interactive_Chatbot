# Chatbot Interativo com Groq

Este projeto implementa um chatbot interativo utilizando a API do Groq e o modelo Llama 3.1. O chatbot permite que os usuários façam perguntas e recebam respostas em tempo real.

## Pré-requisitos

Antes de executar o código, certifique-se de ter o seguinte instalado:

### Pacotes Python

- `dotenv`
- `langchain_groq`

### Obtendo a chave da API do Groq

Para utilizar a API, você precisará de uma chave de API do Groq. Siga os passos abaixo para obtê-la:

1. **Cadastro e Login**: 
   - Acesse o [Groq Cloud Console](https://console.groq.com/playground) e crie sua conta. Após se registrar, faça o login.

2. **Navegação até a seção de API Keys**: 
   - Depois de entrar no console, vá até a seção **"API Keys"** onde você pode gerar novas chaves.

3. **Criação da API Key**: 
   - Clique em **"Create API Key"** e dê um nome descritivo à sua chave. 
   - **Importante**: Esta chave é exibida apenas uma vez, então salve-a em um local seguro, pois você não poderá vê-la novamente.

## Instalação

Você pode instalar os pacotes necessários utilizando o `pip`:

```bash
pip install python-dotenv langchain-groq
