# serializer that will check the password and password_confirmation fields match
# It will also need to hash the password.


from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

 # These fields are only for writing/posting
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        # Check the password and confirmation are the same
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        # Check the password is sensible
        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)


# We take the password and password_confirmation fields and check that they match. If not we send a validation error to the use
# We then use Django's built in validate_password method that checks the strength of the password. This is the same method used when creating a super user in the terminal. It ensures that passwords aren't too weak.
# Finally we hash the password using Django's in-built make_password function, and we store it back on the data object. This will become the serializer.data property and will ultimately get stored in the database.
