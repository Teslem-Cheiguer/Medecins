from django.db import models

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.specialite}"
