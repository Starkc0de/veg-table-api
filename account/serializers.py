from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util
import random as r


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'mobile', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'mobile': {'required': False},
            'name': {'required': False},
            'email': {'required': False}
        }

    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         print(User)
    #         raise serializers.ValidationError("This email already exists!.")
    #     return value   
         
    # def validate_mobile(self, value):
    #     if User.objects.filter(mobile=value).exists():
    #         raise serializers.ValidationError('This mobile already exists')
    #     return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email', 'otp']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            otp=""
            for i in range(4):
                otp+=str(r.randint(1,9))
            # d = { 'otp': otp }    
            # print(d)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/user/reset/'+ uid +'/'+token
            print('Password Reset Link', link)
            # Send EMail
            body = f'Click Following Link to Reset Your Password {otp}' + link
            data = {
                'subject': 'Reset Your Password',
                'body': body,
                'to_email': user.email               
            }
            Util.send_email(data)
            user.otp = otp
            user.save()
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')   

class OTPVerifySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    otp = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['email', 'otp'] 
        extra_kwargs = {
            'email': {'write_only': True},
            'otp': {'required': False}
        }
                   

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError(
                    "Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError(
                    'Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not Valid or Expired')