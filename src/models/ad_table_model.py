import requests
from config import API_URL, API_TOKEN


class AdTableModel:
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
            return data
        
    @staticmethod
    def get_accounts(platform, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        single_value_platform = platforms_dic[platform]
        url = f"{API_URL}/accounts?platform={single_value_platform}"

        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        response = requests.get(url, headers=headers)
        print(response.json())
        return response.json() if response.status_code == 200 else {}

    @staticmethod
    def get_fields(plataforma, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        single_value_platform = platforms_dic[plataforma]
        url = f"{API_URL}/fields?platform={single_value_platform}"

        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {}

    @staticmethod
    def get_insights(plataforma, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        single_value_platform = platforms_dic[plataforma]
        url = f"{API_URL}/insights?platform={single_value_platform}&account={account}&token={API_TOKEN}&fields={fields_str}"
        # fields = ["field1", "field2", "field3"]  # Lista de campos
        # Convertendo a lista de campos para uma string separada por vírgula
        # fields_str = ",".join(fields)

        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {}

# if __name__ == "__main__":
#     PlatformModel.get_accounts("facebook")