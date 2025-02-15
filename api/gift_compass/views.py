from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializer import TestSerializer, PageListSerializer, PageSerializer, AnswerSerializer
from .models import Test, Page, Choice, Content
from .authentication import CustomJWTAuthentication

class TestView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):

        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class SavePageView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, page_id):
        try:
            page = Page.objects.get(uuid=page_id)  # UUIDを使用してページを取得
        except Page.DoesNotExist:
            return Response({"error": "ページが見つかりません"}, status=status.HTTP_404_NOT_FOUND)

        # 既存のContentとChoiceを削除
        page.contents.all().delete()

        # 新しいContentとChoiceを保存
        data = request.data
        contents_data = data.pop('contents', [])
        page.title = data.get('title', page.title)
        page.template_id = data.get('template_id', page.template_id)
        page.save()
        
        i = 1
        for content_data in contents_data:
            choices_data = content_data.pop('choices', [])
            content = Content.objects.create(owner=page, number=i, **content_data)
            i += 1
            j = 1
            for choice_data in choices_data:
                Choice.objects.create(owner=content, number=j, **choice_data)
                j += 1

        # 更新されたPageのデータをシリアライズして返す
        serializer = PageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)



class AnswerPageView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, page_id):

        page = get_object_or_404(Page, uuid=page_id)
        serializer = PageSerializer(page)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, page_id):

        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PageListView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        pages = Page.objects.filter(owner=request.auth['user_id'])

        serializer = PageListSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PageDetailView(APIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

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