from django.shortcuts import render, HttpResponse, redirect

def index(request):
      return render(request, 'index.html')

def result(request):
      print(request.POST.getlist('language'))
      context = {
            "name" : request.POST['name'],
            "location" : request.POST['location'],
            "language" : request.POST.getlist('language'),
            "comment" : request.POST['comment']
      }
      return render(request, "result.html", context)