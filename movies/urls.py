from django.urls import path
from .views import datagetter, recommendme

urlpatterns = [path("data", datagetter), path("recommend", recommendme)]
