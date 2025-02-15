import csv
import io
from collections import defaultdict


class AdTableGeneralResumeModel:
    @staticmethod
    async def create_ad_table_general_resume(general_table):
        dados = []
        leitor_csv = csv.DictReader(general_table.splitlines())
        dados.extend(list(leitor_csv))

        grouped_data = defaultdict(list)

        # Agrupa os dados pelo nome da plataforma
        for row in dados:
            plataform_name = row["platform"]
            grouped_data[plataform_name].append(row)

        result = []

        for plataform_name, rows in grouped_data.items():
            aggregated_row = rows[0].copy()
            aggregated_row["clicks"] = 0
            aggregated_row["impressions"] = 0
            aggregated_row["spend"] = 0
            aggregated_row["cpc"] = 0

            # Soma os valores numéricos
            for row in rows:
                aggregated_row["clicks"] += int(row["clicks"])
                aggregated_row["impressions"] += int(row["impressions"])
                aggregated_row["spend"] += float(row["spend"])
                aggregated_row["cpc"] += float(row["cpc"])

            result.append(aggregated_row)

        csv_resume = await AdTableGeneralResumeModel.create_csv(result)
        return csv_resume

    @staticmethod
    async def create_csv(lista_data):
        output = io.StringIO()
        fieldnames = list(lista_data[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        insights_list = []

        for data in lista_data:
            data.pop("global_objective", None)
            data.pop("effective_status", None)
            data.pop("country", None)
            data.pop("ad_name", None)
            data.pop("account_name", None)

            insights_list.append(data)
        writer.writerows(insights_list)

        return output.getvalue()
