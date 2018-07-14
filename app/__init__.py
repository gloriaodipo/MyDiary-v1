from flask import Flask
from flask_restful import Api

from ..config import app_config

def create_app(config_name):
    '''Method to create a flask app depending on the configuration passed'''

    app = Flask(__name__)
    api=Api(app)

    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    from app.resources.user_resource import UserSignupAPI, UserLoginAPI
    from app.resources.entries_resource import Entry_API

    api.add_resource(UserSignupAPI, '/api/v1/user/signup')
    api.add_resource(UserLoginAPI, '/api/v1/user/login')
    api.add_resource(Entry_API, '/api/v1/entries', '/api/v1/entries/<int:id>')

    return app
