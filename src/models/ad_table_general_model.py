import csv
import io
from src.controllers.ad_table_controller import AdTableController


class AdTableGeneralModel:
    @staticmethod
    async def create_ad_table_general(platform_list):
        general_table = []
        for platform in platform_list:
            tabela_csv = await AdTableController.create_ad_table(platform)

            dicti_table = csv.DictReader(tabela_csv.splitlines())
            general_table.extend(list(dicti_table))

        result = []
        for row in general_table:
            if "cpc" not in row:
                if "cost_per_click" not in row:
                    if "spend" in row:
                        row["cpc"] = float(row["spend"]) / int(row["clicks"])
                    else:
                        row["cpc"] = ""
                        row["spend"] = ""
            result.append(row)

        response = await AdTableGeneralModel.create_csv(result)
        return response

    @staticmethod
    async def create_csv(lista_data):
        output = io.StringIO()
        fieldnames = list(lista_data[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerows(lista_data)
        return output.getvalue()
