from flask import Flask
from src.controllers.root_controller import root_controller
from src.controllers.platform_controller import platform_controller

app = Flask(__name__)
app.register_blueprint(root_controller)
app.register_blueprint(platform_controller)

if __name__ == "__main__":
    app.run(debug=True)
