response = {
    200 : {"message": "Success"},
    401 : {"message": "Unauthorized User"},
    403 : {"message": "Permission Forbidden"},
    404 : {"message": "User not found"}
    }

def build_response(status_code):
    response_data = response.get(status_code)
    return {
            "status_code": status_code,
            "data": response_data
            }

