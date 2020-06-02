"""
TODO:Refactor your code so the location is being passed in the URL rather than via a form
TODO:Have the user specify the win conditions before starting, and then implement them in the game (# of moves, goal for gold)
"""


from django.shortcuts import render, redirect
import random
from time import strftime, localtime

def index(request):
      if not 'gold' in request.session:
            request.session['gold'] = 0

      if not 'activity' in request.session:
            request.session['activity'] = []
      return render(request, 'index.html')

def process_money(request):
      place = request.POST['place']
      gold_amount = calculate_gold(place)
      timestamp = strftime("%A %d %B %Y- %H:%M %Z", localtime())
      data = get_text(gold_amount)

      request.session['gold'] += gold_amount
      request.session['activity'].append({
            'text' : f"{data['text']} from the {place}! ({timestamp})",
            'earned' : data['earned']
      })
      return redirect('/')


def calculate_gold(place):
       # cave
      minNumber = 5
      maxNumber = 10
      
      if place == 'house':
            minNumber = 2
            maxNumber = 5
      elif place == 'farm': 
            minNumber = 10
            maxNumber = 20
      elif place == 'casino':
            minNumber = -50 
            maxNumber = 50
      goldEarned = random.randint(minNumber, maxNumber)
      return goldEarned


def get_text(amount):
      values = {}
      if amount > 0:
            values['text'] = f"Earned {amount}"
            values['earned'] = True
      else:
            values['text'] = f"Lost {abs(amount)}"
            values['earned'] = False
      return values

def reset(request):
      request.session.flush()
      return redirect('/')