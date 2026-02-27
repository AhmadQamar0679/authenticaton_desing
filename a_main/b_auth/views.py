from django.shortcuts import render,redirect
from .models import Patients
from . models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def add_patient(request):
    if request.method=='POST':
        data=request.POST
        patient_name=data.get('patient_name')
        patient_age=data.get('patient_age')
        gender=data.get('gender')
        content=data.get('content')
        address=data.get('address')


        # print('patient_name:',patient_name)
        # print('patient_age:',patient_age)
        # print('patient_gender:',gender)
        # print('patient_contect:',content)
        # print('patient_address:',address)

        Patients.objects.create(
            patient_name=patient_name,
            patient_age=patient_age,
            gender=gender,
            address=address,
            content=content,

        )
        return redirect('/')





    return render(request,'add_patient.html')


@login_required(login_url='/login/')
def view_patient(request):
    queryset=Patients.objects.all()
    context={'patients':queryset}
    return render(request,'view_patients.html',context)


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid User')
            return redirect('/login/')
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        # Check both passwords are same
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/register/')

        # Check unique email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('/register/')

        # Check unique username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('/register/')

        # ✅ Pass first_name directly inside create_user
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,   # ✅ pass here directly to avoid NOT NULL error
        )
        user.save()
        user.set_password(password)
        user.save()

        messages.success(request, 'Account successfully created! Please login.')
        return redirect('/login/')

    return render(request, 'register.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')