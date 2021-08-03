from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as UserDTO
from .main.controller.experience_controller import api as ExperienceDTO

blueprint = Blueprint('api',__name__)
api = Api(blueprint, title='dev_connector',version='1.1',description='dev_connector_api')
api.add_namespace(UserDTO)
api.add_namespace((ExperienceDTO))
