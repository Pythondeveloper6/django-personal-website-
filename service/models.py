from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=25)
    icon = models.CharField(max_length=20)
    description = models.TextField(max_length=110)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    
class Facts(models.Model):
    projects_compelted = models.IntegerField(default=0)
    clients = models.IntegerField(default=0)
    coffe = models.IntegerField(default=0)
    real_professionals = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)