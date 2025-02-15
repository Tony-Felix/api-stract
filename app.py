from flask import Flask
from src.controllers.root_controller import root_controller
from src.controllers.ad_table_controller import ad_table_controller
from src.controllers.ad_table_resume_controller import ad_table_resume_controller
from src.controllers.ad_table_general_controller import ad_table_general_controller

app = Flask(__name__)
app.register_blueprint(root_controller)
app.register_blueprint(ad_table_controller)
app.register_blueprint(ad_table_resume_controller)
app.register_blueprint(ad_table_general_controller)


if __name__ == "__main__":
    app.run(debug=True)
