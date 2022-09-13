from django.urls import path
from .views import home, hash

urlpatterns = [
    path('', home, name='home'),
    path('hash/<str:hash>', hash, name="hash"),
]