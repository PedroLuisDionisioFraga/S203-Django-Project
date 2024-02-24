from django.db import models

# Create your models here.
class Message(models.Model):
  title = models.CharField(max_length=100, blank=False)
  data = models.DateTimeField(auto_now_add=True)
  text = models.TextField
  author = models.ForeignKey('auth.User', related_name='recados', on_delete=models.CASCADE)

class Follower(models.Model):
  follower_user = models.ForeignKey('auth.User', related_name='+', on_delete=models.CASCADE)
  followed_user = models.ForeignKey('auth.User', related_name='+', on_delete=models.CASCADE)