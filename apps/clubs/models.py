from django.db import models
from apps.user.models import User

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User,blank=True)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    #logo = models.ImageField(upload_to='events_img/')

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.name
    
