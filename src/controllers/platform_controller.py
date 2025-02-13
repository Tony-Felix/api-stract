from flask import Blueprint, jsonify, request
from src.models.platform_model import PlatformModel

# import csv
# from io import StringIO

platform_controller = Blueprint("platform_controller", __name__)


# Aqui você poderia integrar com a API da Stract ou outra fonte de dados.
class TableController:
    @staticmethod
    def get_platform(plataforma):
        print(f"o que tem em plataformasdsdsdsd, {plataforma}")
        """Obtém as plataformas disponíveis."""
        # Chamando o Model para obter as plataformas
        platforms_data = PlatformModel.get_platforms()

        if "platforms" not in platforms_data:
            return jsonify({"error": "Erro ao obter plataformas"}), 500

        platforms = platforms_data["platforms"]

        # Buscar pela plataforma no valor (em vez da chave)
        platform_names = [platform["text"] for platform in platforms]

        if plataforma not in platform_names:
            return jsonify({"error": f"Plataforma '{plataforma}' não encontrada na lista de plataformas: {platform_names}"}), 404
        # Retorna as plataformas disponíveis
        lista_acounts_data = TableController.get_accounts(plataforma, platforms)

        return lista_acounts_data

    @staticmethod
    def get_accounts(plataforma, platforms):
        """Obtém as contas de uma plataforma específica."""
        # Obtém as contas da plataforma
        accounts_data = PlatformModel.get_accounts(plataforma, platforms)

        if not accounts_data:
            return jsonify({"error": "Erro ao obter contas"}), 500

        # Retorna as contas da plataforma
        return accounts_data


# Definindo a rota para a plataforma dinâmica
platform_controller.add_url_rule(
    "/<plataforma>", "get_platform", TableController.get_platform
)
# platform_controller.add_url_rule("/<plataforma>", "get_table", TableController.get_table)

# Simulação de dados para a plataforma fornecida (você deve integrar com a API aqui)
# Exemplo de dados, que você substituiria com uma chamada real à API
# if plataforma == "Facebook":
#     data = [
#         {
#             "Platform": "Facebook",
#             "Ad Name": "Some Ad",
#             "Clicks": 10,
#             "Impressions": 100,
#         },
#         {
#             "Platform": "Facebook",
#             "Ad Name": "Other Ad",
#             "Clicks": 20,
#             "Impressions": 200,
#         },
#     ]
# elif plataforma == "YouTube":
#     data = [
#         {
#             "Platform": "YouTube",
#             "Ad Name": "One More Ad",
#             "Clicks": 5,
#             "Impressions": 50,
#         }
#     ]
# else:
#     data = []

# # Gerando o CSV com os dados simulados
# csv_output = StringIO()
# fieldnames = ["Platform", "Ad Name", "Clicks", "Impressions"]
# writer = csv.DictWriter(csv_output, fieldnames=fieldnames)

# writer.writeheader()
# for row in data:
#     writer.writerow(row)

# csv_output.seek(0)
