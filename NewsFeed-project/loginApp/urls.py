from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
]
