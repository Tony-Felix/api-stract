from flask import Blueprint
from src.models.ad_table_model import AdTableModel


ad_table_controller = Blueprint("platform_controller", __name__)


class AdTableController:
    @staticmethod
    async def create_ad_table(plataforma):
        if plataforma == "favicon.ico":
            raise ValueError("plataforma contem favicon.ico")

        try:
            platforms_dic = await AdTableController.get_platform(plataforma)
            if plataforma not in platforms_dic:
                raise ValueError(f"{plataforma} não está na lista: {platforms_dic}")

            account_list = await AdTableController.get_accounts(
                plataforma, platforms_dic
            )
            fields = await AdTableController.get_fields(plataforma)
            insights = await AdTableController.get_insights(
                plataforma, platforms_dic, account_list, fields
            )
            return [insights]
        except Exception as e:
            return f"Erro ao processar a solicitação: {str(e)}"

    @staticmethod
    async def get_platform(plataforma):
        platforms_data = await AdTableModel.get_platforms()

        platforms = platforms_data.get("platforms")
        platforms_dic = {plat["text"]: plat["value"] for plat in platforms}

        if plataforma not in platforms_dic:
            raise ValueError(f"{plataforma} não esta na lista: {platforms_dic}")

        return platforms_dic

    @staticmethod
    async def get_accounts(plataforma, platforms_dic):
        accounts_platform = await AdTableModel.get_accounts(
            plataforma, platforms_dic
        )

        return accounts_platform

    @staticmethod
    async def get_fields(plataforma):
        platforms_dic = await AdTableController.get_platform(plataforma)
        fields = await AdTableModel.get_fields(plataforma, platforms_dic)
        return fields

    @staticmethod
    async def get_insights(plataforma, platforms_dic, accounts, fields):
        insights = await AdTableModel.get_insights(
            plataforma, platforms_dic, accounts, fields
        )

        return insights


ad_table_controller.add_url_rule(
    "/<string:plataforma>", "get_table", AdTableController.create_ad_table
)
