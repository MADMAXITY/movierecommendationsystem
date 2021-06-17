from django.urls import path
from .views import datagetter, recommendme, index

urlpatterns = [
    path("data", datagetter),
    path("recommend", recommendme),
    path("", index),
]
