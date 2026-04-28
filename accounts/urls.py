from django.urls import path
from . import views # هنا بنقول له هات الوظائف من ملف views اللي جنبك

urlpatterns = [
    path('', views.home_view, name='home'),             # الرابط: /accounts/
    path('register/', views.register_view, name='register'), # الرابط: /accounts/register/
    path('login/', views.login_view, name='login'),       # الرابط: /accounts/login/
    path('logout/', views.logout_view, name='logout'),     # الرابط: /accounts/logout/
]