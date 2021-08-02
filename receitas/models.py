from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.nome_receita

    def clean(self):
        self.categoria = self.categoria.capitalize()
        self.nome_receita = self.nome_receita.capitalize()

# Receita.objects.create(nome_receita="Bolo de Chocolate",
#                         ingredientes="-Farinha\n -Ovo\n Leite\n Chocolate\n Pó de arroz",
#                         modo_preparo="Mexer tudo, mexe bem até ter uma massa homogenea boa",
#                         tempo_preparo=40,
#                         rendimento="5 Pessoas",
#                         categoria="Doces")







