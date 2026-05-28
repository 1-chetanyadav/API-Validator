
import json

def load_user_data():
    with open("user/user.json", 'r') as file:
        data = json.load(file)
    return data     