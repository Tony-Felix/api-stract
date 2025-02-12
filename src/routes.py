from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

api_token = os.getenv('API_TOKEN')
print(api_token)  # Exemplo de uso do token
