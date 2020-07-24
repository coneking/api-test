from flask import Flask
import json, os, requests
from routes import *
from routes.test import test
from routes.errors import errors
from routes.server import server

app = Flask(__name__)

# Registro de rutas
app.register_blueprint(errors)
app.register_blueprint(test, url_prefix='/api/v1/test')
app.register_blueprint(server, url_prefix='/api/v1/server')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
