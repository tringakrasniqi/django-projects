from django.db import models

class CourseManager(models.Manager):
      def basic_validator(self, postData):
            errors = {}
            if len(postData["course_name"]) < 5:
                  errors["course_name"] = "Name should be at least 5 charaters"
            if len(postData["course_description"]) < 15:
                  errors["course_description"] = "Description should be at least 15 characters"
            return errors

class Description(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
      name = models.CharField(max_length=255)
      description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="of_course")
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = CourseManager()

class Comment(models.Model):
      content = models.TextField()
      course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

