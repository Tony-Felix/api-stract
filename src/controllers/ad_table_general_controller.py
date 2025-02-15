from flask import Blueprint
from src.models.ad_table_general_model import AdTableGeneralModel
from src.models.ad_table_model import AdTableModel


ad_table_general_controller = Blueprint(
    "ad_table_general_controller", __name__
)


class AdTableGeneralController:
    @staticmethod
    async def create_ad_table_general():
        try:
            platforms_data = await AdTableModel.get_platforms()
            platforms = platforms_data.get("platforms")

            platforms_list = [plat["text"] for plat in platforms]

            general_table = await AdTableGeneralModel.create_ad_table_general(
                platforms_list
            )

            return general_table
        except Exception as e:
            return f"Erro ao processar a solicitação: {str(e)}"


ad_table_general_controller.add_url_rule(
    "/geral",
    "get_table_general",
    AdTableGeneralController.create_ad_table_general
)
