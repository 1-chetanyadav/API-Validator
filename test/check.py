with open("/user/user.json", 'r') as file:
    data = file.read()

from validator.auth_validator import validate_authorization


def check_permission(data):
    response = validate_authorization(data)
    if response != "Authentication successful":
        return response