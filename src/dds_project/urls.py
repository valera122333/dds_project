from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Приложение ДДС
    path("", include("dds.urls")),
]
