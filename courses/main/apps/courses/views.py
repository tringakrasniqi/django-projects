from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
      context = {
            'all_courses': Course.objects.all()
      }
      return render(request, 'index.html', context)

def create_course(request):
      errors = Course.objects.basic_validator(request.POST)
      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
      else: 
            course_description = Description.objects.create(content=request.POST['course_description'])
            Course.objects.create(name= request.POST['course_name'], description = course_description)
                  
      return redirect('/')

def confirm_delete(request, course_id):
      context = {
            "course" : Course.objects.get(id = course_id)
      }
      return render(request, 'delete_confirmation.html', context)

def delete_course(request, course_id):
      course = Course.objects.get(id = course_id)
      Description.objects.get(id = course.description.id).delete()
      course.delete()
      return redirect('/')


def add_comment(request, course_id):
      context = {
            "course" :  Course.objects.get(id = course_id)
      }
      return render(request, 'add_comment.html', context)

def create_comment(request, course_id):
      course_obj = Course.objects.get(id = course_id)
      Comment.objects.create(content = request.POST['comment'], course = course_obj)
      return redirect(f'/courses/add_comment/{course_id}')
      
      