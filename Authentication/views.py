from django.shortcuts import render
from rest_framework.views import APIView

from Authentication.services import CreateUserService, UserService


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        return CreateUserService(request=request).post_view()


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        return UserService(request=request, kwargs=kwargs).get_view()

    def post(self, request, *args, **kwargs):
        return UserService(request=request, kwargs=kwargs).post_view()
