from security.security import get_valid_input, Validation


class Login(object):

    @classmethod
    def get_staff_login_credentials(cls):
        """"""
        return cls._get_login_details(prompt="Enter staff login ID: ")

    @classmethod
    def get_admin_login_credentials(cls):
        return cls._get_login_details(prompt="Enter the admin login ID: ")

    @classmethod
    def _get_login_details(cls, prompt):
        login_id = get_valid_input(prompt)
        password = get_valid_input("Enter the password: ")
        return login_id, password

    @classmethod
    def validate_login_details(cls, login_id, password):
        return True if Validation.validate_password(login_id, password) else False



