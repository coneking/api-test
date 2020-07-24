from flask import jsonify, make_response
from . import errors

@errors.app_errorhandler(404)
def handle_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
