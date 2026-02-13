from rest_framework import serializers
from . models import User
from . models import Profile
from . utils import SendMail



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number','gender','profile_pix','name']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True)
    email = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = Profile
        fields = ['username','name','phone_number','gender','profile_pix','password','confirm_password','email']

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError("Passwords do not match.")
            return data
        
        def create(self, validated_data):
            username = validated_data.pop('email')
            email = validated_data.pop('email')
            password = validated_data.pop('password')

            user = User.objects.create(username=username, email=email, password=password)

            profile = Profile.objects.create(
                user = user,
                name = validated_data['name'] ,
                phone_number = validated_data['phone_number'],
                gender = validated_data['gender'],
                profile_pix = validated_data['profile_pix']
            )
            # SendMail()
            return profile.name