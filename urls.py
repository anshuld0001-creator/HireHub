from django.urls import path,include
from.import views

urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",views.loginView,name="login"),
    path("logout/",views.logoutView,name="logout")
    
]