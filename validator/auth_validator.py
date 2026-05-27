permissions ={
    "admin": ["modify", "delete","view"], 
    "moderator": ["modify","view"], 
    "user": ["view"]
}

def validate_authentication(data):
    if "isActive" != True:
        return 401
    elif "tokens" not in data:
        return 401
    return "Authentication successful"
## or i can simply return 403 in error and 200 to show success

def validate_authorization(data):
    if permissions in permissions.get(data["roles"]):
        return 200
    else:
        return 403