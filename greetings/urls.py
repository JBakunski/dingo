from django.urls import path
from .views import welcome, greeting

urlpatterns = [
    path('', welcome),
    path('<name>', greeting),
]