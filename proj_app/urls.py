from django.urls import path
from . import views 

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('latestmovies/', views.latestmovies, name='latestmovies'),
    path('about/', views.about, name='about'),
    path('movie_details/<int:id>', views.movie_details, name='movie_details'),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    # path('register', views.register, name='register'),
    path('register2', views.register2, name='register2'),
    path('newspage', views.newspage, name='newspage' ),
    path('otppage/', views.otpview, name='otppage'),
    
    # api endpoint
    path('movie_details/<int:id>/comments', views.allcomments, name='allcomments'),
    path('newsapi/', views.newsapi, name='newsapi')
    
    
]