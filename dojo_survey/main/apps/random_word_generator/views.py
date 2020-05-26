from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
      if not 'counter' in request.session:
            request.session['counter'] = 0
      print("in random word generator")
      return render(request, 'random_word.html')

def generate(request):
      request.session['word'] = get_random_string(length=15)
      request.session['counter'] += 1
      return redirect('/random_word')

def reset(request):
      request.session.flush()
      return redirect('/random_word')