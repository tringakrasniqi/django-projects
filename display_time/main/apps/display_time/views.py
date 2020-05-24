from django.shortcuts import render
from time import strftime, localtime

def index(request):
      context = {
            "time": strftime("%A %d %B %Y- %H:%M %Z", localtime())
      }
      return render(request, "index.html", context)