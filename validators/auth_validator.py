import json
import os

from response.response import build_response

def validate_authentication(data):
    if data.get("isActive") != True:
        # print("User is not active")
        return 401
    
    elif data.get("tokens") not in data:
        # print("User's not token authenticated")
        return 401
    return 200


def validate_authorization(data):
    role_permissions = {}
    role_permissions = data.get("permissions", [])
    return role_permissions
    


