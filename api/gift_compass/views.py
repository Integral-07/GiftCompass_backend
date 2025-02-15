from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializer import TestSerializer, PageListSerializer, PageSerializer
from .models import Test, Page
from .authentication import CustomJWTAuthentication

class TestView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):

        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    

class PageListView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        pages = Page.objects.filter(owner=request.auth['user_id'])
        #page_infos = []
        #for page in pages:
        #    page_info = {
        #        'uuid': page.uuid,
        #        'title': page.title,
        #        'published': page.published,
        #    }
        #    page_infos.append(page_info)

        serializer = PageListSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PageDetailView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []#IsAuthenticated]

    def get(self, request, page_id):

        page = get_object_or_404(Page, uuid=page_id)
        serializer = PageSerializer(page)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    """
    ユーザログイン処理

    Args:
        APIViews(class): rest_framework.viewsのAPIViewを受け取る
    """

    #認証クラスの指定
    authentication_classes = [JWTAuthentication]

    #アクセス許可の指定
    permission_classes = []

    def post(self, request):

        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access = serializer.validated_data.get("access", None)
        refresh = serializer.validated_data.get("refresh", None)

        if access:
            response = Response(status=status.HTTP_200_OK)
            max_age = settings.COOKIE_TIME
            response.set_cookie('access', access, httponly=True, max_age=max_age)
            response.set_cookie('refresh', refresh, httponly=True, max_age=max_age)

            return response
        
        return Response({'errMsg': "User authentization failed"}, status=status.HTTP_401_UNAUTHORIZED)
    
class RetryView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def post(self, request):
        request.data['refersh'] = request.META.get('HTTP_REFRESH_TOKEN')
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access = serializer.validated_data.get("access", None)
        refresh = serializer.validated_data.get("refresh", None)
        if access:
            response = Response(status=status.HTTP_200_OK)
            max_age = settings.COOKIE_TIME
            response.set_cookie('access', access, httponly=True, max_age=max_age)
            response.set_cookie('refresh', refresh, httponly=True, max_age=max_age)
            
            return response
        
        return Response({'errMsg': 'User Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        
        return response