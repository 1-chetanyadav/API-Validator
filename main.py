import sys
from user.data_loader import load_user_data

from validators.auth_validator import validate_authorization, validate_authentication

from test_case.test_permission import build_batch_response

from response.response import build_response


def main():

    data = load_user_data()
    auth_response = validate_authentication(data)
    
    # print(f"data: {data}")
    
    if auth_response != 200:
        error_response = build_response(auth_response)
        print(f"Authentication Error: {error_response}")
        sys.exit()
        return
    
    role_permissions = validate_authorization(data)
    print(f"Permissions Found: {role_permissions}")
    response = build_batch_response(role_permissions)
    
    
    


if __name__ == "__main__":
    main()