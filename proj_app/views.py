from django.shortcuts import render, redirect
from .forms import addmovieform, commentform, registerform, registerform2
from .models import moviemodel, commentmodel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime, timedelta


from django.contrib.auth.decorators import login_required
from django_otp.decorators import otp_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from .forms import OTPForm
import pyotp


# Create your views here.
top3movies = moviemodel.objects.order_by('-rating')[:3] 

def homepage(request):
    movies = moviemodel.objects.all()
    search_movies = 0
    if request.method == 'POST':
        requested_movie = request.POST['moviesearch']
        if requested_movie:
            movies=moviemodel.objects.filter(story__icontains=requested_movie)
            search_movies = 1
    return render(request, 'home.html', {'movies':movies,'top3movies':top3movies, 'search_movie':search_movies})



def movie_details(request, id):
    movie = moviemodel.objects.get(id=id)
    comment_count = commentmodel.objects.filter(movie=id)
    comment = commentmodel.objects.filter(movie=id).order_by('-comment_date')[:3]
    
    form = commentform(initial={'username':request.user, 'movie':id})
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = commentform(request.POST)
            if form.is_valid():
                form.save()
                form = commentform(initial={'movie':id,'username':request.user})
        else:
            messages.error(request, 'Login To Comment')
            
        
    return render(request, 'moviedetails.html', {'movie':movie, 'top3movies':top3movies, 'form':form, 'comment_count':comment_count, 'comments':comment})
    

def latestmovies(request):
    movies = moviemodel.objects.order_by('-release_date') 
    return render(request, 'latestmovies.html', {'movies':movies,'top3movies':top3movies})
    
def about(request):
    return render(request, 'about.html', {'top3movies':top3movies})


def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            name=request.POST['name']
            psw = request.POST['password']
            user = authenticate(username=name, password=psw)
            if user is not None:
                login(request, user)
                messages.success(request, ' Successfully Logged In ! ')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid credintials')
                
        return render(request, 'loginpage.html' ,{'top3movies':top3movies})
    
    else:
        messages.error(request, 'You Are Already Loggined !')
        return redirect('homepage')
    

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Succefully Loged Out !')
        return redirect('homepage')
    else:
        messages.error(request, 'Login To Access logOut ')
        return redirect('homepage')
        

# def register(request):
#     if not request.user.is_authenticated:
#         regform = registerform()
#         if request.method == 'POST':
#             regform = registerform(request.POST)
#             if regform.is_valid():
#                 email_from = settings.EMAIL_HOST_USER
#                 mail = [request.POST['email'],]
                
#                 name = request.POST['username']
#                 subject = "Welcome To Movies Ocean"
#                 messagess = f"Hello {name}, Thanks For Registering Into Movies Ocean"
#                 send_mail(subject, messagess, email_from, mail)
#                 regform.save()
#                 messages.success(request, 'Succesfully Registered ')
#                 return redirect('login')
            
               
#         return render(request, 'register.html', {'form':regform,'top3movies':top3movies})
    
#     else:
#         messages.error(request, 'You Are Already Loggined !')
#         return redirect('homepage')



def register2(request):
    if not request.user.is_authenticated:
        form = registerform2()
        if request.method == "POST":
            form = registerform2(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                
                email_from = settings.EMAIL_HOST_USER
                mail = [form.email,]
                
                name = form.username
                subject = "Welcome To Movies Ocean"
                messagess = f"Hello {name}, Thanks For Registering Into Movies Ocean"
                send_mail(subject, messagess, email_from, mail)
                
                form.password = make_password(form.password)
                form.save()
                form = registerform2()
                messages.success(request, 'Succesfully Registered ')
                return redirect('login')     
        
        return render(request, 'register2.html', {'form':form, 'top3movies':top3movies})
    
    else:
        messages.error(request, 'You Are Already Loggined !')
        return redirect('homepage')
        

def newspage(request):
    api_key = 'f3ef3329ea084653bc52170a8b649603'
    query = 'Hollywood'
    today = datetime.now().strftime('%Y-%m-%d')
    last_week = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
   
    url = f'https://newsapi.org/v2/everything?q={query}&from={last_week}&to={today}&sortBy=publishedAt&apiKey={api_key}'
        
    response = requests.get(url).json()

    return render(request, 'news.html', {'news':response,'top3movies':top3movies})
    

def addmovie(request):
    form = addmovieform()
    if request.method == 'POST':
        form = addmovieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    return render(request, 'addmovie.html', {'form':form})


################# Api Enpoints #########################################################

@api_view(['GET'])
def allcomments(request, id):
    data = commentmodel.objects.filter(movie=id).order_by('comment_date')
    data_list = list(data.values())
    return Response(data_list)


    
@api_view(['GET'])
def newsapi(request):
    api_key = 'f3ef3329ea084653bc52170a8b649603'
    query = 'movies OR film OR cinema OR Hollywood'
    today = datetime.now().strftime('%Y-%m-%d')
    last_week = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    url = f'https://newsapi.org/v2/everything?q={query}&from={last_week}&to={today}&sortBy=publishedAt&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return Response(data)







































    