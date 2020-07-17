from django.shortcuts import render, redirect
from .models import News, home_news
from.forms import Registrationform, RegistrationModal, loginnModal
from .models import Registrationdata
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,addUser)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials set')
            return redirect('login')

    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")


def newsp(request):
    obj = News.objects.get(id=1)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

    context= {
        "data":obj

    }
        

    return render(request,'news.html', context)

def newsdate(request, year):

    article_list = News.objects.filter(pub_date__year = year)

    context = {
        "year":year,
        "article_list":article_list
    }
    return render(request, 'newsdate.html', context)





def home(request):
    news = home_news.objects.all()
    context= {
        "name": "ALAO ADEBUKOLA NAFISAT",
        "number":8122213918,
        "hnews":news
    }
    

    return render( request,'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('accounts/login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('accounts/login')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login/')
                
       
        
    
        else:
            messages.info(request,'password not matching...')
            return redirect('signup/')
        return redirect('/')

    else:
        return render(request,'signup.html')




 

def addUser(request):
    form = Registrationform(request.POST)

    if form.is_valid():
        myregister =Registrationdata(username = form.cleaned_data['username'],
                                   password = form.cleaned_data['password'],
                                   email = form.cleaned_data['email'],
                                   phone = form.cleaned_data['phone'])
        myregister.save()
        messages.add_message(request, messages.SUCCESS, 'You have successfully registered!')                          

    return redirect ('register')

def modalform(request):
    
    context = {
        "modalform": RegistrationModal
    }
    return render(request, 'modalform.html', context) 

def addModalForm(request):
    mymodalForm = RegistrationModal(request.POST)

    if mymodalForm.is_valid():
        mymodalForm.save()
    return redirect ('modalform')


def modallogin(request):
    context={
        'modallogin': loginnModal
    }
    return render(request,'login.html', context)

def addModallogin(request):
    myloginnform = loginnModal(request.POST)

    if myloginnform.is_valid():
        myloginnform.save()
    return redirect ('/')