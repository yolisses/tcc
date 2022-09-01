from django.db import models


class Course(models.Model):
    MODALITIES = [
        ('B', 'Bacharelado'),
        ('L', 'Licenciatura'),
        ('T', 'Tecnológico'),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Nome")
    modality = models.CharField(max_length=12, choices=MODALITIES, verbose_name="Modalidade")

    class Meta:
        verbose_name = 'Curso'
