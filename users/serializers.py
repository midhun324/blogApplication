from rest_framework import serializers
from .models import CustomUser

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'phone_number', 'address', 'date_of_birth', 'gender', 'profile_picture']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
            profile_picture=validated_data['profile_picture'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
