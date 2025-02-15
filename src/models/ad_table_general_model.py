from src.controllers.ad_table_controller import AdTableController


class AdTableGeneralModel:
    @staticmethod
    async def create_ad_table_general(platforms):
        general_table = []
        for platform in platforms:
            print(platform)
            result = await AdTableController.create_ad_table(platform)
            general_table.append(result)

        print(general_table)
        return general_table
