import traceback
from flask import current_app

from src.models.users import User


class UsersController:
    def __init__(self):
        pass

    def get_user(self, user_id):
        try:
            #TODO: Fill this method
            pass

        except Exception as e:
            current_app.logger.debug(traceback.format_exc())
            raise e


