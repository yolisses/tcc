from django.db import models


class Tcc(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    year = models.PositiveIntegerField()
    abstract = models.CharField(max_length=2500)
    file = models.FileField()
