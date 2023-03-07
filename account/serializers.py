from rest_framework import serializers
from django.contrib.auth.models import User



# class RegisterAPISerializers(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

    # def validate_username(self, value):
    #     if value == 'admin':
    #         raise serializers.ValidationError('username cant be admin')
    #     return value
    
#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError('password is invaled')
#         return data

class RegisterAPISerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {"write_only":True}}

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
    
    # def update(self, instance, validated_data):
    #     del validated_data['password2']
    #     return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin')
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password is invaled')
        return data
    

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"