from database.user_db import UserDB


class Validation(object):

    @staticmethod
    def validate_password(login_id, password):
        user = UserDB.get_password_by_username(login_id)
        return True if user and user.username.lower() == login_id.lower() and user.password == password else False


def get_valid_input(prompt):

    running = True
    response = None

    while running:
        response = input(prompt)
        if response:
            running = False
    return response


def get_valid_number(prompt):

    while True:
        try:
            resp = float(input(prompt))
        except ValueError:
            pass
        else:
            if not resp:
                print("[-] The value entered cannot be 0, try again...")
            else:
                return resp