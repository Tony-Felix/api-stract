from flask import Blueprint, jsonify, request
from src.models.ad_table_model import AdTableModel

# import csv
# from io import StringIO

Ad_table_controller = Blueprint("platform_controller", __name__)


# Aqui você poderia integrar com a API da Stract ou outra fonte de dados.
class AdTableController:
    @staticmethod
    def create_ad_table(plataforma):
        platforms_dic = AdTableController.get_platform(plataforma)

        list_acounts_platform = AdTableController.get_accounts(plataforma, platforms_dic)

        fields = AdTableController.get_fields(plataforma)

        return [platforms_dic, list_acounts_platform, fields]

    @staticmethod
    def get_platform(plataforma):
        platforms_data = AdTableModel.get_platforms()

        if "platforms" not in platforms_data:
            return jsonify({"error": "Erro ao obter plataformas"}), 500

        platforms = platforms_data["platforms"]

        # Buscar pela plataforma no valor (em vez da chave)
        platforms_dic = {plat["text"]: plat["value"] for plat in platforms}

        if plataforma not in platforms_dic:
            return jsonify({"error": f"Plataforma '{plataforma}' não encontrada na lista de plataformas: {platforms_dic}"}), 404

        return platforms_dic

    @staticmethod
    def get_accounts(plataforma, platforms_dic):
        """Obtém as contas de uma plataforma específica."""

        accounts_platform = AdTableModel.get_accounts(plataforma, platforms_dic)

        if not accounts_platform:
            return jsonify({"error": "Erro ao obter contas"}), 500

        return accounts_platform

    @staticmethod
    def get_fields(plataforma):
        platforms_dic = AdTableController.get_platform(plataforma)
        fields = AdTableModel.get_fields(plataforma, platforms_dic)
        return fields
    
    @staticmethod
    def get_insights(plataforma):
        platforms_dic = AdTableController.get_platform(plataforma)
        fields = AdTableModel.get_fields(plataforma, platforms_dic)
        platforms_dic = AdTableController.get_platform(plataforma)
        accounts = AdTableController.get_accounts(plataforma, platforms_dic)

        insights = AdTableModel.get_insights(plataforma, platforms_dic, fields, accounts)

        return insights


Ad_table_controller.add_url_rule(
    "/<plataforma>", "get_table", AdTableController.create_ad_table
)
