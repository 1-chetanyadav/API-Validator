response = {
    200 : "Success",
    401 : "Unauthorized User",
    403 : "Permission Forbidden",
    404 : "User not found"
    }

def build_response(status_code):
    return response.get(status_code, "Unknown status code")