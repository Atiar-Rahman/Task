from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import SignUpSerializer,SignInSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class SignUpAPIView(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message':'user signup successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SignInAPIView(APIView):
    def post(self,request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
            )
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


