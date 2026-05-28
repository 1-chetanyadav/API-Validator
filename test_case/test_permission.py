
from response.response import build_response


# def check_permission(permissions):
#     test_case = build_batch_response(permissions)
    # delete_response = delete(permissions)
    # modify_response = modify(permissions)
    # view_response = view(permissions)
    
def build_batch_response(permissions):
    for permission in permissions:
        response_data = None
        if permission == "delete_product":
            # print("\n","delete permission found")
            delete_response = build_response(200)
            print(delete_response)

        
        elif permission == "modify_product":
            # print("\n","modify permission found")
            modify_response = build_response(200)
            print(modify_response)

        
        elif permission == "view_product":
            # print("\n","view permission found")
            view_response = build_response(200)
            print(view_response)
        else:
            print("\n","invalid permission")
            invalid_response = build_response(403)
            print(invalid_response)
    
def delete(permissions):
    if "delete_product" in permissions:
            return 200
    else:   
            return 403
    
def modify(permissions):
    if "modify_product" in permissions:
        return 200
    else:
        return 403

def view(permissions):
    if "view_product" in permissions:
        return 200
    else:
        return 403

    

    
# def delete_product(permissions):
#     if "delete_product" in permissions:
#         return 200
#     else:
#         return 403
    
# def modify_product(permissions):
#     if "modify_product" in permissions:
#         return 200
#     else:
#         return 403

# def view_product(permissions):
#     if "view_product" in permissions:
#         return 200
#     else:
#         return 403