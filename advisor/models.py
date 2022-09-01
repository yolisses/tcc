from django.db import models


class Advisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    lattes = models.URLField(verbose_name="Link do currículo Lattes")
    last_name = models.CharField(max_length=50, verbose_name="Último nome")
    given_name = models.CharField(max_length=50, verbose_name="Primeiro nome")

    class Meta:
        verbose_name = 'Orientador'
        verbose_name_plural = 'Orientadores'
