from django.urls import path
from .views import *

urlpatterns = [    
    path('login/', log_in),
    path('logout/', log_out),
    path('signup/', sign_up),
]