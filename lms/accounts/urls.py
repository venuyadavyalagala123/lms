from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login '),
    path('signup/', signup),
    path('logout/', userlogout),
]

