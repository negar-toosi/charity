from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address
    """
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        # Filter users by matching username or email
        users = user_model._default_manager.filter(
            Q(**{user_model.USERNAME_FIELD: username}) | Q(email__iexact=username)
        )

        # Test whether any matched user has the provided password
        for user in users:
            if user.check_password(password):
                return user  # Return the user object upon successful authentication

        # If no users matched or password didn't match, return None
        return None
