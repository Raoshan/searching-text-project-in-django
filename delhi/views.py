from .models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

def home(request):
    state = States.objects.all().values('name').distinct()   
    context = {'state':state}  
    return render(request, 'home.html', context) 

def category(request):
    c =(request.GET.keys())   
    for i in c:
        c=i    
    category= Category.objects.filter(id__icontains=c)
    if c == 'all':
        category =Category.objects.all()
    context = {
        'category':category
    }    
    return render(request, 'category.html', context)  

def subcategory(request):
    sub = request.GET.keys()
    for i in sub:
        sub = i
    subcategory = SubCategory.objects.filter(name__icontains=sub)
    if sub == 'name':
        subcategory = SubCategory.objects.all()
    context = {
        'subcategory':subcategory}
    return render(request, 'subcategory.html', context)

def job(request):
    job = request.GET.keys()
    for i in job:
        job=i  
    job = Jobs.objects.filter(jobPosition__icontains=job)
    if job == 'all':
        job = Jobs.objects.all()
    context = {
        'jobs': job
    }
    return render(request, 'jobs.html', context)

def companydetails(request):
    company = request.GET.keys()
    for i in company:
        company = i
    
    companydetails = CompanyDetails.objects.filter(name__icontains=company)
    context = {
        'companydetails':companydetails
    }
    return render(request, 'companydetails.html', context)    
  
def searchingstate(request):
    query = request.GET['query']
    states = States.objects.filter(name__icontains=query).values('name').distinct()
    print(states)
    try:
        states[0]
    except:
        return render(request, 'error.html')
    context = {
        'states':states
    }
    return render(request, 'searching.html',context)
def searchingcat(request):
    query = request.GET['query']
    category = Category.objects.filter(name__icontains=query)
    
    try:
        category[0]
    except:
        return render(request, 'error.html')
    context = {
        'category':category
    }
    return render(request, 'searching.html',context)
def searchingsub(request):
    query = request.GET['query']
    category = SubCategory.objects.filter(name__icontains=query)
    try:
        category[0]
    except:
        return render(request, 'error.html')
    context = {
        'category':category,
    }
    return render(request, 'searching.html',context)

def searchingjob(request):
    query = request.GET['query']
    jobs = Jobs.objects.filter(jobPosition__icontains=query)
    try:
        jobs[0]
    except:
        return render(request, 'error.html')
    context = {
        'jobs':jobs,
    }
    return render(request, 'searching.html',context)    


   
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirm_password = request.POST['password2']
        if password1==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():  
                messages.info(request, "Email address taken.") 
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.info(request, "Successfully Registration.")
                return redirect('login')
        else:
            messages.info(request, "Password not matching.")  
            return redirect('register')  

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Username or Password, Please Try Again.')    
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")

