from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from .models import Account
from django.core.cache import BaseCache
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Account
from .email import sent_email_return_otp


# register
class UserRegisterViewset(viewsets.ViewSet):
    """ this method is used to create user side """

    def create(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

""" 
Already created a superuser 

use credentials : email : admin@gmail.com
                  pass : 12345
"""

class UserLoginView(APIView):
    """This method is used to login a user """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserLoginWithOtpView(APIView):
    """This method is used to login a user with OTP shared via Email and save the access token in the session."""

    def post(self, request):
        email = request.data.get('email')
        user = Account.objects.filter(email=email).first()

        if user:
            # Send email and get the OTP
            otp = sent_email_return_otp(email)

            # Save the OTP and user in the session
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            request.session.save()

            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User not found."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        otp = request.query_params.get('otp')
        stored_otp = request.session.get('otp')
        userid = request.session.get('user_id')

        if stored_otp == otp and userid:
            # Retrieve the user from the database
            user = Account.objects.get(id=userid)
            # If OTP is valid, generate a JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            # Remove the stored OTP and user_id from the session

            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid OTP'})