from rest_framework import serializers

from users.models import CustomUser
from .models import BlogPost



class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author','image']  # include author if necessary
        read_only_fields = ['author']



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'first_name', 'last_name', 'phone_number', 'address', 'bio']

    def update(self, instance, validated_data):
        # Update fields based on the incoming data
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.bio = validated_data.get('bio', instance.bio)


        instance.save()
        return instance