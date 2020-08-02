from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.TextField(max_length = 100)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  date = models.DateField(auto_now = True)

  def __str__(self):
    return(self.title + "\nID: " + str(self.pk))