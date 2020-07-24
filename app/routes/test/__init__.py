from flask import Blueprint, Flask

test = Blueprint('test', __name__)

from .test import *
