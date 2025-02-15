import csv
import io
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
                response = await client.get(
                    url, headers=headers, timeout=90.0
                )

            if response.status_code == 200:
                data = response.json()
                if "platforms" not in data:
                    raise ValueError(
                        "A chave 'platforms' não foi encontrada."
                    )
                return data
        except httpx.RequestError as exc:
            raise Exception(f"Erro de requisição: {exc}")
            return None

    @staticmethod
    async def get_accounts(plataforma, platforms_dic):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        if plataforma not in platforms_dic:
            raise ValueError(
                f"Erro: Não foi possível encontrar a plataforma '{plataforma}'"
            )

        single_value_platform = platforms_dic.get(plataforma, None)
        if not single_value_platform:
            raise Exception("Error. plataforma não encontrada")
        accounts_list = []
        page = 1
        total_pages = None

        async with httpx.AsyncClient() as client:
            while total_pages is None or page <= total_pages:
                url = (
                    f"{API_URL}/accounts?platform={single_value_platform}"
                    f"&page={page}"
                )
                headers = {"Authorization": f"Bearer {API_TOKEN}"}

                try:
                    response = await client.get(
                        url, headers=headers, timeout=90.0
                    )

                    if response.status_code != 200:
                        raise Exception(
                            f"Erro na requisição: {response.status_code}"
                        )

                    accounts = response.json()
                    accounts_list.extend(accounts.get("accounts", []))

                    if "pagination" not in accounts:
                        break

                    if total_pages is None:
                        total_pages = accounts.get("pagination").get(
                            "total", 1
                        )

                    page += 1
                except httpx.ConnectTimeout:
                    raise Exception("Erro: Timeout.")
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
                url = (
                    f"{API_URL}/fields?platform={single_value_platform}"
                    f"&page={page}"
                )
                headers = {"Authorization": f"Bearer {API_TOKEN}"}
                try:
                    response = await client.get(
                        url, headers=headers, timeout=90.0
                    )

                    if response.status_code != 200:
                        raise Exception(
                            f"Erro na requisição: {response.status_code}"
                        )

                    data = response.json()
                    if not data:
                        raise Exception("A resposta da API está vazia.")

                    fields = data.get("fields")

                    if not fields:
                        raise Exception(
                            "O campo 'fields' não foi encontrado na resposta."
                        )

                    fields_list.extend(fields)

                    if "pagination" not in data:
                        break

                    if total_pages is None:
                        total_pages = data.get("pagination").get("total", 1)

                    page += 1

                except httpx.ConnectTimeout:
                    raise Exception(
                        "Erro: Timeout ao tentar acessar o endpoint."
                    )
                except Exception as e:
                    raise Exception(f"Erro inesperado: {e}")

        if not fields_list:
            raise Exception("Nenhum campo foi retornado da API.")

        return fields_list

    @staticmethod
    async def get_insights(plataforma, platforms_dic, accounts, fields):
        if not API_URL or not API_TOKEN:
            raise ValueError("URL ou Token não encontrado no ambiente")

        single_value_platform = platforms_dic[plataforma]
        fields_str = ",".join(field["value"] for field in fields)

        insights_list = []
        for user in accounts:
            USER_TOKEN, id, name = user["token"], user["id"], user["name"]

            url = (
                f"{API_URL}/insights?platform={single_value_platform}"
                f"&account={id}&token={USER_TOKEN}&fields={fields_str}"
            )

            headers = {"Authorization": f"Bearer {API_TOKEN}"}

            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, timeout=90.0)
                if response.status_code != 200:
                    raise Exception(f"Erro ao obter insights da conta {id}")
                insights_data = response.json()

                if not isinstance(insights_data, dict) or \
                        "insights" not in insights_data:
                    raise ValueError(f"Resposta da API inválida: esperado uma "
                                     f"lista, mas recebeu {insights_data}")

                for data in insights_data["insights"]:
                    data.pop("id", None)
                    data["account_name"] = name
                    data["platform"] = plataforma

                    insights_list.append(data)

        csv_table = await AdTableModel.create_csv(insights_list)
        return csv_table

    @staticmethod
    async def create_csv(lista_data):
        output = io.StringIO()
        fieldnames = list(lista_data[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(lista_data)

        return output.getvalue()
