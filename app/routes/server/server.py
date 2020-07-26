from flask import jsonify
import time
from . import server

@server.route('/server-status')
def index():
    return jsonify({'status': 'running'})

@server.route('/timeout')
def timeout():
    time.sleep(180)
    return jsonify({'time': 'So slow... more than 3 minutes'})
