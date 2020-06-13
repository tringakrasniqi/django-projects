from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import User
import bcrypt

def index(request):
      return render(request, 'index.html')

def login(request):
      errors = User.objects.login_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/')
      else:
            logged_user = User.objects.filter(email=request.POST["email"])
            request.session['uid'] = logged_user[0].id
            return redirect('/success')

def register(request):
      errors = User.objects.basic_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/')
      else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
            print(pw_hash) 
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash, birthday=datetime.strptime(request.POST['bday'], '%Y-%M-%d'))
            request.session['uid'] = user.id
            return redirect('/success')

def success(request):
      if "uid" in request.session:
            user = User.objects.filter(id=request.session["uid"])
            context = {
                  "user" : user
            }
            return render(request, 'success.html', context)
      else:
            return redirect('/')

def logout(request):
      request.session.flush()
      return redirect('/')
