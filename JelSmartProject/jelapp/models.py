from django.db import models

class Kezikonyv(models.Model):
    cim = models.CharField(max_length=200)
    leiras = models.TextField()
    kategoria = models.CharField(max_length=100)
    letrehozva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cim

class Gyakorlo(models.Model):
    cim = models.CharField(max_length=200, verbose_name="Cím")
    leiras = models.TextField(verbose_name="Leírás")
    nehezseg = models.CharField(max_length=50, verbose_name="Nehézség")
    letrehozas_datum = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás dátuma")

    class Meta:
        verbose_name = "Gyakorló"
        verbose_name_plural = "Gyakorlók"

    def __str__(self):
        return self.cim

class Fogalom(models.Model):
    nev = models.CharField(max_length=100, verbose_name="Név")
    definicio = models.TextField(verbose_name="Definíció")
    kategoria = models.CharField(max_length=50, verbose_name="Kategória")
    letrehozas_datum = models.DateTimeField(auto_now_add=True, verbose_name="Létrehozás dátuma")

    class Meta:
        verbose_name = "Fogalom"
        verbose_name_plural = "Fogalmak"

    def __str__(self):
        return self.nev