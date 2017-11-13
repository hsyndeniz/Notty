from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    category = models.CharField(max_length=100, verbose_name="Category")
    created_at = models.DateField(verbose_name="Yayın Tarihi")


    def __str__(self):
        return self.title

