from django.shortcuts import render , HttpResponse , redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
def index(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Msg = request.POST.get('msg')
        Inq = inq(name=Name, email=Email, msg=Msg)
        Inq.save()
        messages.add_message(request, messages.INFO, "Query sent Succefully")
    return render(request , 'index.html')
    #return HttpResponse('Hi')
def about(request):
    return render(request , 'about.html')
def form(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pswd = request.POST.get('password')
        user = User.objects.create_user(username=username , password=pswd)
        user.save()
        messages.add_message(request, messages.INFO, "Welcome! Now you can Sign In Using Your Username and Password")
    return render(request , 'form.html')

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pswd = request.POST.get('password')
        user = authenticate(username=username , password=pswd)
        if user is not None:
            login(request , user)
            return redirect("/index")
        else:
            messages.add_message(request, messages.INFO, "Incorrect Credentials")
    return render(request , 'signin.html')

def signout(request):
    logout(request)
    return redirect('/')

def blogg(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        text= request.POST.get('text')
        pic= request.FILES.get('img')
        print(name)
        print(text)
        print(pic)
        blogger = blog.objects.create(name=name,text=text,pic=pic)
        return redirect('blog')
    queryset = blog.objects.all()
    context = {'blogs': queryset}
    return render(request, 'blog.html' , context )

def delete_b(request , id):
    queryset = blog.objects.get(id=id)
    queryset.delete()
    return redirect('/blog')