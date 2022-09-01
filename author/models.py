from django.db import models


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    given_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField()
