import asyncio
import httpx
from config import API_URL, API_TOKEN


class AdTableModel:
    @staticmethod
    async def get_platforms():
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        url = f"{API_URL}/platforms"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, timeout=90.0)

            if response.status_code == 200:
                data = response.json()
                if "platforms" not in data:
                    raise ValueError("A chave 'platforms' não foi encontrada na resposta da API.")
                return data
        except httpx.RequestError as exc:
            print(f"Erro de requisição: {exc}")
            return None

    @staticmethod
    async def get_accounts(plataforma, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        if plataforma not in platforms_dic:
            raise ValueError(f"Erro: Não foi possível encontrar a plataforma '{plataforma}")

        single_value_platform = platforms_dic.get(plataforma, None)
        if not single_value_platform:
            return print("Error. plataforma não encontrada")
        accounts_list = []  # Lista para armazenar todas as contas
        page = 1  # Começa na primeira página
        total_pages = None  # Inicialmente desconhecido

        async with httpx.AsyncClient() as client:
            while total_pages is None or page <= total_pages:
                url = f"{API_URL}/accounts?platform={single_value_platform}&page={page}"
                headers = {"Authorization": f"Bearer {API_TOKEN}"}

                try:
                    response = await client.get(url, headers=headers, timeout=90.0)

                    if response.status_code != 200:
                        raise Exception(f"Erro na requisição: {response.status_code}")

                    accounts = response.json()
                    accounts_list.extend(accounts.get("accounts", []))

                    if total_pages is None:
                        total_pages = accounts.get("pagination").get("total", 1)

                    page += 1

                except httpx.ConnectTimeout:
                    raise Exception("Erro: Timeout ao tentar acessar o endpoint.")
                except Exception as e:
                    raise Exception(f"Erro inesperado: {e}")

        if not accounts_list:
            raise Exception("Nenhuma conta foi retornada da API.")
        return accounts_list

    @staticmethod
    async def get_fields(plataforma, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        single_value_platform = platforms_dic.get(plataforma)

        fields_list = []
        page = 1
        total_pages = None

        async with httpx.AsyncClient() as client:
            while total_pages is None or page <= total_pages:
                url = f"{API_URL}/fields?platform={single_value_platform}&page={page}"
                headers = {"Authorization": f"Bearer {API_TOKEN}"}
                try:
                    response = await client.get(url, headers=headers, timeout=90.0)

                    if response.status_code != 200:
                        raise Exception(f"Erro na requisição: {response.status_code}")
                    
                    data = response.json()
                    print(f"testa data antes de dar problema, {data}")
                    if not data:  # Verifique se a resposta está vazia
                        raise Exception("A resposta da API está vazia.")
                    
                    fields = data.get("fields")

                    if not fields:
                        raise Exception("O campo 'fields' não foi encontrado na resposta.")

                    fields_list.extend(fields)

                    if total_pages is None:
                        total_pages = data.get("pagination").get("total", 1)

                    page += 1

                except httpx.ConnectTimeout:
                    raise Exception("Erro: Timeout ao tentar acessar o endpoint.")
                except Exception as e:
                    raise Exception(f"Erro inesperado: {e}")

        if not fields_list:
            raise Exception("Nenhum campo foi retornado da API.")

        return fields_list

    @staticmethod
    async def get_insights(plataforma, platforms_dic, accounts, fields):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        # single_value_platform = platforms_dic[plataforma]
        # fields_str = ",".join(field["value"] for field in fields)

        return "em produção"
    #     "pagination": {
    #   "current": 1,
    #   "total": 3

        # url = f"{API_URL}/insights?platform={single_value_platform}&account
        # ={account}&token={USER_TOKEN}&fields={fields_str}"
        # # fields = ["field1", "field2", "field3"]  # Lista de campos
        # # Convertendo a lista de campos para uma string separada por vírgula
        # # fields_str = ",".join(fields)

        # headers = {"Authorization": f"Bearer {API_TOKEN}"}

        # response = requests.get(url, headers=headers)
        # return response.json() if response.status_code == 200 else {}


# if __name__ == "__main__":
#     AdTableModel.get_insights("facebook Ad", )