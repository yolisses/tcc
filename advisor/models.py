from django.db import models


class Advisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    given_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    lattes = models.URLField()
