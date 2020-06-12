from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
      def basic_validator(self, postData):
            errors = {}
            user = User.objects.filter(email=postData['email'])
            if user:
                  errors["email"] = "Email already registered"
            if len(postData["first_name"]) < 2:
                  errors["first_name"] = "First name should be more than 2 chars"
            if len(postData["last_name"]) < 2:
                  errors["last_name"] = "Last name should be more than 2 chars"
            if not EMAIL_REGEX.match(postData["email"]):
                  errors["email"] = "Invalid email address!"
            if len(postData["password"]) < 8:
                  errors["password"] = "Password must be more than 8 chars"
            elif postData["password"] != postData["confirm_password"]:
                  errors["password"] = "Passwords do not match"
            return errors

      def login_validator(self, postData):
            errors = {}
            if not EMAIL_REGEX.match(postData["email"]):
                  errors["email"] = "Invalid email address!"
            else :
                  user = User.objects.filter(email = postData['email'])
                  if user: 
                        logged_user = user[0]
                        if not bcrypt.checkpw(postData["password"].encode(), logged_user.password.encode()):
                              errors["password"] = "Email and password do not match"
                  else:
                        errors["email"] = "Account does not exist"
            return errors

class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=150)
      password = models.CharField(max_length=255)
      updated_at = models.DateTimeField(auto_now=True)
      created_at = models.DateTimeField(auto_now_add=True)
      objects = UserManager()