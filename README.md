# API Stract

Descrição: API voltada a captura e manipulação dos dados das plataformas de ADS, retornando um CSV formatado para melhor manipulação e criação de apresentações legíveis para os usuários.


Passos para Usar a API:

1°- Rodar o comando "pip install -r requirements.txt" no terminal para instalar as dependências.(Sem as aspas)
2°- Rodar o comando "python app.py" (Sem as aspas)

Rotas da API:
Legenda: "plataforma" é um parâmetro STRING que representa o nome da plataforma de interesse do usuário.

{'Facebook Ads': 'meta_ads', 'Google Analytics': 'ga4', 'TikTok': 'tiktok_insights'}
1°- "/{{plataforma}}"
exemplo: /Facebook Ads
2°- "/{{plataforma}}/resumo"
exemplo: /Google Analytics/resumo
3°- "/geral"
4°- "/geral/resumo"