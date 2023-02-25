from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    img=models.ImageField(upload_to='catImages')
    class Meta:
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
class Products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='images')
    desc=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField()
    class Meta:
        ordering=('name',)
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])