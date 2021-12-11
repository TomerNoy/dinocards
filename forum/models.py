from django.contrib.auth.models import User
from django.db import models


class Thread(models.Model):
    subject = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} by {self.creator.username}'


class Comment(models.Model):
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.user.username}'
