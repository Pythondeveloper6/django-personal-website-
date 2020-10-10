from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey('Category',related_name='project_category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'