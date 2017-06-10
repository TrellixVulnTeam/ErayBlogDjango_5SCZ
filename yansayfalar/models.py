from django.db import models

# Create your models here.
class YanSayfalar(models.Model):
    yanSayfaBaslik = models.CharField(max_length=100)
    yanSayfaResim = models.ImageField(upload_to='media/')
    yanSayfaGovde = models.TextField()
    yanSayfaLink = models.CharField(max_length=200)

    def __str__(self):
        return self.yanSayfaBaslik
