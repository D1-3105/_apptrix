from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self, validated_data):
        User = get_user_model()  # model
        user=User.objects.create_user(
            name=validated_data['name'],
            surname=validated_data['surname'],
            password=validated_data['password'],
            avatar=validated_data['avatar'],
            email=validated_data['email'],
            sex=validated_data['sex']
        )
        return user

    class Meta:
        model= get_user_model()
        fields= ('email','sex', 'name', 'surname', 'avatar', 'password')

