from django.db import models


class Library(models.Model):
    nomeLivro = models.CharField(max_length=60)
    anoLivro = models.IntegerField()
    autorLivro = models.CharField(max_length=50)
    paginasLivro = models.IntegerField()

    def __str__(self):
        return self.nomeLivro
