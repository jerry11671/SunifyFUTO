from django.urls import path
from .views import *

urlpatterns = [
    path('', predictView.as_view(), name='predict'),
]