from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .forms import RegisterForm , LoginForm

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/accounts/login')
    else:
        lform = LoginForm()
        return render(request, 'login.html',{'lform':lform})

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/accounts')
                #err = "Username already taken"
                #return render(request, 'register.html', {'err': err})
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Username already taken")
                return redirect('/accounts')
                #err = "Email Name already taken"
                #return render(request, 'register.html', {'err': err})

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created")
                return redirect('/accounts/login')
                #return render(request,'register.html')
        else:
            messages.info(request, "Password Doesn't Matched")
            #err = "Password Doesn't Matched"
            #return render(request, 'register.html',{'err':err})
            return redirect('/accounts')

    else:
        rform = RegisterForm()
        return render(request,'register.html',{'rform':rform})

def logout(request):
    auth.logout(request)
    return redirect('/')
