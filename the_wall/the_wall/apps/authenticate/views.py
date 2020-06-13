from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
      if 'uid' in request.session:
            return redirect('/wall')
      else:
            return render(request, 'index.html')

def register(request):
      errors = User.objects.register_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/')
      else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['uid'] = user.id
            return redirect('/')

def login(request):
      errors = User.objects.login_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/')
      else:
            user = User.objects.filter(email=request.POST["email"])
            logged_user = user[0]
            request.session['uid'] = logged_user.id
            return redirect('/')

def logout(request):
      request.session.flush()
      return redirect('/')