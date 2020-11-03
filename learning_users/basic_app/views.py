from basic_app.forms import UserForm, UserProfileInfoForm
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
#import for setting up logins
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


#index view
def index(request):
    return render(request,'basic_app/index.html')

@login_required  #decorator
def special(request):
    return HttpResponse("You are logged in, Nice")
#logout
@login_required  #decorator
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#register view
def register(request):

    registred = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        #Now i need to check that the both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #For hashing password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES: #manipulating files like images, csv or pdf
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registred = True
        else:
            print(user_form.errors,profile_form.errors)
    
    else:  #setting everything up
       user_form = UserForm() 
       profile_form = UserProfileInfoForm()


    #we will return the data that we need in registration.html file
    return render(request,'basic_app/registration.html',
                                {'user_form':user_form,
                                'profile_form':profile_form,
                                'registred':registred})
    
    
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') #it will get information from login.html input name 'username'
        password = request.POST.get('password')

        user = authenticate(username=username,password=password) #thankyou Django

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'basic_app/login.html',{})
