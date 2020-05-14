from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/')


    return render(request, 'register.html')
