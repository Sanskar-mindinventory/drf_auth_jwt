import re
from django.contrib.auth.backends import AllowAllUsersModelBackend, BaseBackend
from django.contrib.auth import get_user_model
from Authentication.constants import EMAIL_PATTERN, INVALID_EMAIL_FORMAT

from regex_validations import RegexValidation

User = get_user_model()


class EmailOrUsernameModelBackend(AllowAllUsersModelBackend):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if RegexValidation(field_data=username, regex_pattern=EMAIL_PATTERN, error_message=INVALID_EMAIL_FORMAT).regex_auth_validator():
                user = User.get_user(kwargs={"email": username})
            else:
                user = User.get_user(kwargs={"username": username})
        except User.DoesNotExist:
            return None
        else:
            if user and user.check_password(password):
                return user
        return None


class EmailBackend(AllowAllUsersModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.get_user(kwargs={"email": username})
        except User.DoesNotExist:
            return None
        else:
            if user and user.check_password(password):
                return user
        return None
