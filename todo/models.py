from django.db import models
from authorization.models import *


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    user_fk = models.ForeignKey(Authorization, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
