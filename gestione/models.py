from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Azienda(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Sede(models.Model):
    azienda = models.ForeignKey(Azienda, on_delete=models.CASCADE)
    indirizzo = models.CharField(max_length=255)
    città = models.CharField(max_length=100)
    luogo = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.luogo} - {self.indirizzo}"

class Prodotto(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    azienda = models.ForeignKey(Azienda, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome