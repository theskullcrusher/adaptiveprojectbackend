def get_user_name():
    try:
        auth_token = request.headers.get(app.auth_header_name, None)
    except:
        return None

    headers = { "content-type"          : "application/json",
                "X-Authorization-Token" : auth_token }

    try:
        active_user_json = requests.get( 'http://localhost:7285/userservice/uservalidation' ,
                                          headers = headers).json()
        user = active_user_json['responseData']['guid']
    except:
        return None

    return user

