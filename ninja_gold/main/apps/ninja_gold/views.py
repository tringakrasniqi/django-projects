from django.shortcuts import render, redirect

def index(request):
      if not 'gold' in request.session:
            request.session['gold'] = 0

      if not 'activity' in request.session:
            request.session['activity'] = []
      return render(request, 'index.html')

def process_money(request):
      request.session['gold'] += 10
      print(request.POST)
      return redirect('/')