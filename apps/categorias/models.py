from django.db import models
# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
