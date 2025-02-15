from flask import Blueprint
from src.controllers.ad_table_general_controller import (
    AdTableGeneralController
)
from src.models.ad_table_general_resume_model import AdTableGeneralResumeModel

ad_table_general_resume_controller = Blueprint(
    "ad_table_general_resume_controller", __name__)


class AdTableGeneralResumeController:
    @staticmethod
    async def create_ad_table_general_resume():
        try:
            general_table = await AdTableGeneralController.\
                create_ad_table_general()

            response = await AdTableGeneralResumeModel.\
                create_ad_table_general_resume(general_table)
            return response
        except Exception as e:
            return f"Erro ao processar a solicitação: {str(e)}"


ad_table_general_resume_controller.add_url_rule(
    "/geral/resumo", "get_table_general_resume",
    AdTableGeneralResumeController.create_ad_table_general_resume
)
