from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
      def register_validator(self, post_data):
            errors ={}
            user = User.objects.filter(email=post_data["email"])
            if user:
                  errors["email"] = "This email already exists"
            elif not EMAIL_REGEX.match(post_data['email']):  
                  errors['email'] = "Invalid email address!"
            if len(post_data['first_name']) < 2:
                  errors['first_name'] = "First name should be more than 2 chars"
            if len(post_data['last_name']) < 2:
                  errors['last_name'] = "Last name should be more than 2 chars"
            if len(post_data['password']) < 8:
                  errors['password'] = "Password must be longer than 8 chars"
            return errors
      def login_validator(self, post_data):
            errors = {}
            if not EMAIL_REGEX.match(post_data['email']):  
                  errors['email'] = "Invalid email address!"
            else :
                  user = User.objects.filter(email=post_data["email"])
                  if user:
                        logged_user = user[0]
                        if not bcrypt.checkpw(post_data['password'].encode(), logged_user.password.encode()):
                              errors['password'] = "Email and password do not match"
                  else:
                        errors["email"] = "This account is not crated yet"
            return errors


class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = UserManager()
