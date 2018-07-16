from flask import Flask
from flask_restful import Api

import config

def create_app(config_name):
    '''Method to create a flask app depending on the configuration passed'''

    app = Flask(__name__)
    api=Api(app)

    app.config.from_object(config.app_config[config_name])
    app.url_map.strict_slashes = False

    from app.resources.user_resource import SignupResource, LoginResource
    from app.resources.entries_resource import EntryResource

    api.add_resource(SignupResource, '/api/v1/user/signup')

    api.add_resource(LoginResource, '/api/v1/user/login')
    api.add_resource(EntryResource, '/api/v1/user/entry', '/api/v1/user/entries')
    
    return app
