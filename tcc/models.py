from django.db import models

from advisor.models import Advisor
from author.models import Author
from course.models import Course


class Keyword(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Palavra-Chave'
        verbose_name_plural = 'Palavras-Chave'


class Tcc(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField(verbose_name="Arquivo do documento")
    title = models.CharField(max_length=300, verbose_name="Título")
    abstract = models.CharField(max_length=2500, verbose_name="Resumo")
    year = models.PositiveIntegerField(verbose_name="Ano do documento")

    keywords = models.ManyToManyField(Keyword)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'TCC'
        verbose_name_plural = "TCC's"
