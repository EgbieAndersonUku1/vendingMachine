from database.db_storage import passwords_db
from models.user import User


class UserDB(object):

    @classmethod
    def get_password_by_username(cls, username):
        user_data = passwords_db.get(username.lower())

        if user_data:
            return User(username=user_data["id"], password=user_data["password"])


