from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", views.LoginView.as_view()),
    path("retry/", views.RetryView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("test/", views.TestView.as_view()),
]