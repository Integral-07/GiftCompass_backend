from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", views.LoginView.as_view()),
    path("retry/", views.RetryView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("page_list/", views.PageListView.as_view()),
    path("page_view/<page_id>/", views.PageDetailView.as_view()),
    path("page_save/<page_id>/", views.SavePageView().as_view()),
    path("page_answer/<page_id>/", views.AnswerPageView.as_view()),
    path("page_answer_preview/<page_id>/", views.AnswerPreview().as_view()),
    path("test/", views.TestView.as_view()),
]