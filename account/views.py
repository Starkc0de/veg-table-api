from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserRegistrationSerializer, OTPVerifySerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from account.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(generics.GenericAPIView):
    renderer_classes = [UserRenderer]
    serializer_class = UserRegistrationSerializer

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registration Successful','status':True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'Registration can not Successful','status':False }, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(generics.GenericAPIView):
    renderer_classes = [UserRenderer]
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Login Success', 'status':True}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']},'status':False}, status=status.HTTP_404_NOT_FOUND)


class UserChangePasswordView(generics.GenericAPIView):
    renderer_classes = [UserRenderer]
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully','status':True}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(generics.GenericAPIView):
    renderer_classes = [UserRenderer]
    serializer_class = SendPasswordResetEmailSerializer

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset link send. Please check your Email','status':True}, status=status.HTTP_200_OK)

class OTPVerify(generics.GenericAPIView):
    serializer_class = OTPVerifySerializer

    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = serializer.data['otp']
        if User.objects.filter(otp=otp).exists():
            User.objects.filter(otp=otp).update(is_active=True)
            return Response({'msg': 'Your OTP Verify','status':True}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Your OTP not Verify','status':False}, status=status.HTTP_200_OK)       


class UserPasswordResetView(generics.GenericAPIView):
    renderer_classes = [UserRenderer]
    serializer_class = UserPasswordResetSerializer

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully','status':True}, status=status.HTTP_200_OK)


class EditUserView(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated ]
    queryset = User.objects.all()     
    serializer_class = UserRegistrationSerializer

