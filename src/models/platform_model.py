import requests
from config import API_URL, API_TOKEN


class PlatformModel:
    @staticmethod
    def get_platforms():
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        url = f"{API_URL}/platforms"

        headers = {
            "Authorization": f"Bearer {API_TOKEN}"  # Adicionando o token na requisição
        }

        # Fazendo a requisição com o token de autenticação
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("Plataformas recebidas da API:", data)  # Debug para ver a resposta real
            return data
        
    @staticmethod
    def get_accounts(platform, platforms):
        """Obtém as contas para uma determinada plataforma."""
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")
        # preciso de chaves e valores aqui.
        values_platform = [platform["value"] for platform in platforms]
        print(values_platform[platform])
        url = f"{API_URL}/accounts?platform={platform}"
        print(f"Requisitando: {url}")

        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {}


# if __name__ == "__main__":
#     PlatformModel.get_accounts("facebook")