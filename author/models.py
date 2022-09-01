from django.db import models


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    picture = models.ImageField(verbose_name="Foto")
    last_name = models.CharField(max_length=50, verbose_name="Último nome")
    given_name = models.CharField(max_length=50, verbose_name="Primeiro nome")

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
