from REST_framework import status
from REST_framework import APIException

class NoAuthToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "No authentication token provided"
    default_code = "no_auth_token"

class InvalidAuthToken(APIException):
    statis_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "No authentication token provided"
    default_code = "no_auth_token"

class InvalidAuthToken(APIException):
    statis_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "User provided with the token is not a valid firebase user, it has no firebase UID "
    default_code = "no_firebase_uid"