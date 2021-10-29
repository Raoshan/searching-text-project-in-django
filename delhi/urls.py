from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),   
    path('category/', views.category, name='category'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('job/', views.job, name='job'),
    path('companydetails/', views.companydetails, name='companydetails'),
    path('searchingstate', views.searchingstate, name='searchingstate'),
    path('searchingcat', views.searchingcat, name='searchingcat'),
    path('searchingsub', views.searchingsub, name='searchingsub'),
    path('searchingjob', views.searchingjob, name='searchingjob'),
    
]