from utils.get_user_token import decode_jwt_token


def get_role(token):
    print(token.split()[1])
    return decode_jwt_token(token.split()[1]).get('role', '')