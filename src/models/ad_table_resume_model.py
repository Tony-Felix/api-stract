import io
import csv
from collections import defaultdict


class AdTableResumeModel:
    @staticmethod
    async def get_resume_table(table):
        reader = csv.DictReader(table.splitlines())
        grouped_data = defaultdict(list)
        print(table)

        # Agrupa os dados pelo nome da conta
        for row in reader:
            account_name = row["account_name"]
            grouped_data[account_name].append(row)

        result = []

        for account_name, rows in grouped_data.items():
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
                if "cpc" not in row:
                    if "spend" in row:
                        aggregated_row["cpc"] = float(row["spend"]) / int(
                            row["clicks"])
                    else:
                        aggregated_row["cpc"] = ""
                else:
                    aggregated_row["cpc"] += float(row["cpc"])
                print(aggregated_row)

            result.append(aggregated_row)

        csv_resume = await AdTableResumeModel.create_csv(result)
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

            insights_list.append(data)
        writer.writerows(insights_list)

        return output.getvalue()
