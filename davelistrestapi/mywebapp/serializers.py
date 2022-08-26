from rest_framework import serializers
from .models import Image, Message, listing

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Listing Serializer        
class listingserializer(serializers.ModelSerializer):
    class Meta:
        model=listing
        fields=('__all__')

# Image Serializer        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'property_id',
            'image'
        )
# Messages Serializer        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'sender',
            'receiver',
            'message',
        )