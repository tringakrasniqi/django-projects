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
      book = Book.objects.get(id=book_id)
      context = {
            'book' : book,
            'authors': Author.objects.exclude(books__id = book_id)
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
            'author': Author.objects.get(id = author_id),
            'books' : Book.objects.exclude(publishers__id = author_id)
      }
      return render(request, 'show_one_author.html', context)

def add_author_book(request, book_id):
      book =  Book.objects.get(id=book_id)
      Author.objects.get(id=request.POST['new_author']).books.add(book)
      return redirect(f'/show_book/{book_id}')

def add_book_to_author(request, author_id):
      author = Author.objects.get(id = author_id)
      book = Book.objects.get(id=request.POST['new_book'])
      author.books.add(book)
      return redirect(f'/show_author/{author_id}')