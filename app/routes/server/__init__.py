from flask import Blueprint, Flask

server = Blueprint('server', __name__)

from .server import *
