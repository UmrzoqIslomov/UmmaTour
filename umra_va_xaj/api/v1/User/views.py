from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.User.serializer import UserSerializer
from base.helper import BearerToken
from umravaxajapp.models import AdminUser


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (BearerToken, )
    def post(self, requests, *args, **kwargs):
        data = requests.data
        try:
            user = AdminUser()
            user.username = data['username']
            user.name = data['name']
            user.set_password(data['password'])
            user.save()
        except Exception as e:
            return Response({"Error": f'{e}'})

        token = Token.objects.create(user=user)

        return Response({"success": token.key})


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data
        try:
            user = AdminUser.objects.get(username=data.get('username'))
        except:
            raise NotFound("User not found!")

        if not user.check_password(data.get('password')):
            raise AuthenticationFailed("Password not found!")

        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)

        return Response({"success": token.key})


class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def post(self, requests, *args, **kwargs):
        token = Token.objects.get(user=requests.user)
        token.delete()

        return Response({"success": "Token is delete!"})
