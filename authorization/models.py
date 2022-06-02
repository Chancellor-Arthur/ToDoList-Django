from django.db import models


class Authorization(models.Model):
    user = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user
