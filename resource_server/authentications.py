from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
import requests
from django.conf import settings
import jwt

class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed()

        data = {
            "token" : token
        }
        url = settings.INTROSPECTION_URL
        response = requests.post(url, data=data)
        user = None
        if response.status_code == 200:
            jwt_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = jwt_data.get('user_id')
        return (user, None)