from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/gift_compass/", include("api.gift_compass.urls"))
]
