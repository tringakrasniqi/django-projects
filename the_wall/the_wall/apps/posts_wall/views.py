from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment, Message
from apps.authenticate.models import User
import datetime

def index(request):
      if 'uid' in request.session:
            messages = Message.objects.all().order_by("-created_at")
            user = User.objects.get(id = request.session['uid'])
            context = {
                  'all_messages' : messages,
                  'user' : user
            }
            return render(request, 'wall.html', context)
      else:
            return redirect('/')

def new_message(request):
      errors = Message.objects.basic_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
      else:
            creator = User.objects.get(id=request.session['uid'])
            Message.objects.create(message = request.POST['message'], creator = creator)

      return redirect('/')

def new_comment(request, message_id):
      errors = Comment.objects.basic_validator(request.POST)
      if len(errors) == 0:
            creator = User.objects.get(id=request.session['uid'])
            message = Message.objects.get(id = message_id)
            Comment.objects.create(comment=request.POST['comment'], creator = creator, of_message = message)
      return redirect('/')

def delete_message(request, message_id):
      message = Message.objects.get(id=message_id).delete()
      return redirect('/')