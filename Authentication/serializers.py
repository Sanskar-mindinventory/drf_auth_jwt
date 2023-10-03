from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from Authentication.models import CustomUser
from regex_validations import RegexValidation
from Authentication.constants import EMAIL_PATTERN, INVALID_EMAIL_FORMAT, INVALID_PASSWORD_FORMAT, PASSWORD_PATTERN, USERNAME_PATTERN, INVALID_USERNAME_FORMAT


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def validate_email(self, email):
        return RegexValidation(field_data=email, regex_pattern=EMAIL_PATTERN, error_message=INVALID_EMAIL_FORMAT).regex_validator()

    def validate_username(self, username):
        return RegexValidation(field_data=username, regex_pattern=USERNAME_PATTERN, error_message=INVALID_USERNAME_FORMAT).regex_validator()

    def validate_password(self, password):
        return RegexValidation(field_data=password, regex_pattern=PASSWORD_PATTERN, error_message=INVALID_PASSWORD_FORMAT).regex_validator()

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.create_custom_user(kwargs=validated_data)

    def update(self, user_id, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        return CustomUser.update_user(user_id=user_id.id, kwargs=validated_data)

    def to_representation(self, instance):
        user_representation = super(
            UserSerializer, self).to_representation(instance=instance)
        user_representation.pop('password')
        user_representation.pop('groups')
        user_representation.pop('user_permissions')
        return user_representation
