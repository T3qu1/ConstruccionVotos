from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS# para que no genere errores de CORS al hacer peticiones

from backend.blueprints.task_blueprint import task_blueprint

app = Flask(__name__)

app.register_blueprint(task_blueprint)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    app.run(debug=True)