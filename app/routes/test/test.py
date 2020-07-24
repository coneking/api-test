from flask import Flask, request, jsonify, make_response
from . import test


# Metodo POST, duevuelve diccionario inyectado
@test.route('/post-test', methods=['POST'])
def get_info():
        content = request.json
        return jsonify(content)
