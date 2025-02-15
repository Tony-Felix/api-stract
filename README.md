# API Stract

Descrição: API voltada a captura e manipulação dos dados das plataformas de ADS, retornando um CSV formatado para melhor manipulação e criação de apresentações legíveis para os usuários.


Passos para Usar a API:

1°- Rodar o comando "pip install -r requirements.txt" no terminal para instalar as dependências.(Sem as aspas). (a instalação pode ser feita em um ambiente virtual)

2°- criar .env na raiz do projeto com essas variaveis:
API_TOKEN=seu_token_aqui
API_URL=https://sidebar.stract.to/api

3°- criar config.py na raiz do projeto com esse codigo:
import os
def load_env():
    with open(".env", "r") as en:
        for line in en:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

load_env()
API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")


4°- Rodar o comando "python app.py" (Sem as aspas)
Rotas da API:
Legenda: "plataforma" é um parâmetro STRING que representa o nome da plataforma de interesse do usuário.

exemplo de plataformas: meta_ads, ga4, tiktok_insights
1°- "/{{plataforma}}"
exemplo: /Facebook Ads
2°- "/{{plataforma}}/resumo"
exemplo: /Google Analytics/resumo
3°- "/geral"
4°- "/geral/resumo"