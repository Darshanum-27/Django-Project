from django.contrib import admin
from django.urls import path
from Loginify import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SignUpPage/', views.SignUpView,name='signup'),
    path('', views.home),
    path('UpdateUser/<str:username>/', views.UpdateUser,name='UpdateUser'),
    path('LoginPage/', views.LoginPage,name='LoginPage'),
    path('AllUsers/', views.DisplayAllUsers,name='AllUsers'),
    path('DeleteUser/<str:email>/', views.DeleteUser,name='DeleteUser'),
    path('GetUserInfo/<str:email>/', views.GetUserInfo,name='GetUserInfo'),

]
