from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_time_password_changed = models.BooleanField(default=False)
    is_two_fa = models.BooleanField(default=False)
    two_fa_email = models.BooleanField(default=False)
    two_fa_mobile = models.BooleanField(default=False)
    two_fa_authenticator = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    two_fa_expiry_time = models.DateTimeField(null=True, blank=True)

    @classmethod
    def create_custom_user(cls, kwargs):
        """
        create user with given kwargs
        """
        return cls.objects.create(**kwargs)

    @classmethod
    def get_user(cls, kwargs=None):
        """
        get user if kwargs, else get all users
        """
        return cls.objects.filter(**kwargs).first() if kwargs else cls.objects.filter()

    @classmethod
    def update_user(cls, user_id, kwargs):
        """
        Update user with details in kwargs and return user
        @param user_id: user id
        """
        cls.objects.filter(id=user_id).update(**kwargs)
        return cls.get_user(kwargs={'id': user_id})

    @classmethod
    def set_new_password(cls, user, password):
        """
        set user password
        @param user: user
        @param password: user password
        """
        user.set_password(password)
        user.save()
