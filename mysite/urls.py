from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("documentation/", include("documentation.urls")),
    path("admin/", admin.site.urls),
]
