from flask import Blueprint, jsonify


root_controller = Blueprint("root_controller", __name__)


class RootController:
    @staticmethod
    def get_info():
        response_data = {
            "Name": "Antonio Felix",
            "Email": "toni.felixx@gmail.com",
            "Linkedin": "https://www.linkedin.com/in/ant%C3%B4nio-f%C3%A9lix/"
        }
        return jsonify(response_data)


root_controller.add_url_rule("/", "get_info", RootController.get_info)
