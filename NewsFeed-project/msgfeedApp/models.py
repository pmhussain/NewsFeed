from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phno = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     def __str__(self):
#         return self.name

class Message(models.Model):
    person =models.CharField(max_length=500, null=True)
    message = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to = 'media', blank=True)
    no_of_likes = models.IntegerField(null=True, default=0)
    no_of_comments = models.IntegerField(null=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    # tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.message

class Like(models.Model):
    Like_id=models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.username

class Comment(models.Model):
    comment_id=models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=500, null=True)
    comment = models.CharField(max_length=500, null=True)
    # def __str__(self):
    #     return self.username
