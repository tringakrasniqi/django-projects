from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
      context = {
            'all_books': Book.objects.all()
      }
      return render(request, 'index.html', context)

def add_book(request):
      Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
      return redirect('/')

def show_book(request, book_id):
      context = {
            'book' : Book.objects.get(id=book_id)
      }
      return render(request, 'book_details.html', context)

def show_authors(request):
      context = {
            'authors' : Author.objects.all()
      }
      return render(request, 'show_authors.html', context)

def add_author(request):
      Author.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], note= request.POST['note'])
      return redirect('/authors')

def show_author(request, author_id):
      context = {
            'author': Author.objects.get(id = author_id)
      }
      return render(request, 'show_one_author.html', context)