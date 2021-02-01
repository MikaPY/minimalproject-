from django.urls import path
from .views import index, test, show

urlpatterns = [
    path('news/', index, name='Home'),
    path('test/', test, name='Test'),
    path('show/', show, name='show'),
]
