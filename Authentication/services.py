from django.http import JsonResponse
from Authentication.constants import USER_CREATED, USER_DOES_NOT_EXIST, USER_UPDATED, YOU_CAN_NOT_UPDATE
from Authentication.models import CustomUser
from Authentication.serializers import UserSerializer


class CreateUserService:
    def __init__(self, request):
        self.request = request

    def post_view(self):
        data = self.request.data
        serialized_user = UserSerializer(data=data)
        if serialized_user.is_valid():
            user = serialized_user.save()
            msg = USER_CREATED.format(username=user.username, id=user.id)
            return JsonResponse({"msg": msg, 'data': serialized_user.data}, status=201)
        return JsonResponse(serialized_user.errors, status=400)


class UserService:
    def __init__(self, request, kwargs):
        self.request = request
        self.kwargs = kwargs

    def get_view(self):
        user_instance = CustomUser.get_user(
            kwargs={"id": self.kwargs.get('id')})
        if user_instance:
            user_serialized = UserSerializer(user_instance)
            return JsonResponse(user_serialized.data, status=200, safe=False)
        return JsonResponse({"msg": USER_DOES_NOT_EXIST.format(id=self.kwargs.get('id'))}, status=400, safe=False)

    def post_view(self):
        data = self.request.data
        user_instance = CustomUser.get_user(
            kwargs={"id": self.kwargs.get('id')})
        if not user_instance:
            return JsonResponse({"msg": USER_DOES_NOT_EXIST.format(id=self.kwargs.get('id')) + YOU_CAN_NOT_UPDATE}, status=400, safe=False)
        serialized_user = UserSerializer(
            instance=user_instance, data=data, partial=True)
        if serialized_user.is_valid():
            user = serialized_user.save()
            msg = USER_UPDATED.format(username=user.username)
            return JsonResponse({"msg": msg, 'data': serialized_user.data}, status=200)
        return JsonResponse(serialized_user.errors, status=400)
