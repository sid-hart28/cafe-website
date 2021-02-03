from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        email = request.POST['email']

        user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
        user.save()
        print("user_created")
        return redirect('/')
    else:
        print("else worked her")
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')