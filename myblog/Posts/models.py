from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=120)
    categoria = models.CharField(max_length=30)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

   