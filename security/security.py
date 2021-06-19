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
    running = True

    while running:
        try:
            value = float(input(prompt))
        except ValueError:
            print("[-] The amount entered must be a float or an integer, try again...")
        else:
            if not value:
                print("[-] The value entered cannot be 0, try again...")
            elif value < 0:
                print("[-] The value entered cannot be a negative value, please try adding a positive value")

            else:
                running = False
    return value


