from django.db import models

# Create your models here.
class Post(models.Model):
    baslik = models.CharField(max_length=250)
    tarih = models.DateTimeField()
    resim = models.ImageField(upload_to='media/')
    govde = models.TextField()

    def __str__(self):
        return self.baslik

    def ozet(self):
        return self.govde[:150]

    def tarihDuzelt(self):
        return self.tarih.strftime('%b %d %Y')
