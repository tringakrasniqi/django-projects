from django.db import models
from apps.authenticate.models import User

class MessageManager(models.Manager):
      def basic_validator(self, post_data):
            errors = {}
            if len(post_data['message']) < 2:
                  errors['message'] = "Please add more to your message"
            return errors

class Message(models.Model):
      message = models.TextField()
      creator = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = MessageManager()

class CommentManager(models.Manager):
      def basic_validator(self, post_data):
            errors = {}
            if len(post_data['comment']) < 2:
                  errors['comment'] = "Please add more to your comment"
            return errors

class Comment(models.Model):
      comment = models.TextField()
      creator = models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)
      of_message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = CommentManager()
