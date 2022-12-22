from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users', views.read_users, name="users"), # lists all users info
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path('user/<str:username>',views.get_user,name='viewuser'),
]
