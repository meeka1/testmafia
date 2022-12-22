from django.urls import path, include
from authentication import views

urlpatterns = [
    path('users', views.read_users, name="users"), # lists all users info
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path('getuser', views.get_user,name='getuser'),
    path('delete', views.delete_user, name='deleteuser'),
    # path("signout", views.signout, name="signout"),
]
