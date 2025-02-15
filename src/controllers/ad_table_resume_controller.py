from flask import Blueprint
from src.controllers.ad_table_controller import AdTableController
from src.models.ad_table_resume_model import AdTableResumeModel


ad_table_resume_controller = Blueprint("ad_table_resume_controller", __name__)


class AdTableResumeController:
    @staticmethod
    async def create_ad_table_resume(plataforma):
        if plataforma == "favicon.ico":
            raise ValueError("plataforma contem favicon.ico")

        try:
            table = await AdTableController.create_ad_table(plataforma)

            resume_table = await AdTableResumeController.get_resume_table(
                table)
            return resume_table
        except Exception as e:
            return f"Erro ao processar a solicitação: {str(e)}"

    @staticmethod
    async def get_resume_table(table):
        resume_table = await AdTableResumeModel.get_resume_table(table)
        return resume_table


ad_table_resume_controller.add_url_rule(
    "/<string:plataforma>/resumo", "get_table_resume", 
    AdTableResumeController.create_ad_table_resume
)
