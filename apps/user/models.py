from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

'''
El ORM de django funciona en dos etapas, la primera es comunicarnos con el modelo self.model luego al objects que es el object manager
es el que traduce a SQL e interactua con la BD, se pueden sobreescribir o crear managers, un modelo puede tener varios manager
objects ya esta definido en Model como objects=ObjectManager() se puede crear otro como ej: autor_manager=AutorManager()
Los manager se utilizan para consultas especificas o recurrentes
'''

class UserManager(BaseUserManager):
    def _create_user(self,email,username,names,password,is_staff,is_superuser,**extra_fields):
        if not email:
            raise ValueError('Debe tener correo electronico')
        user=self.model(
            username=username,
            email=self.normalize_email(email),
            names=names,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,email,username,names,password = None,**extra_fields):
        return self._create_user(email,username,names,password,False,False,**extra_fields)
    
    def create_superuser(self,email,username,names,password = None,**extra_fields):
        return self._create_user(email,username,names,password,True,True,**extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True,max_length=100)
    email = models.EmailField('Correo electronico', unique=True,max_length=254)
    facebook = models.URLField('facebook', null=True, blank=True)
    instagram = models.URLField('instagram', null=True, blank=True)
    twitter = models.URLField('twitter', null=True, blank=True)
    web = models.URLField('web', null=True, blank=True)
    names = models.CharField('Nombres', null=True,blank=True,max_length=200)
    last_names = models.CharField('Apellidos', null=True,blank=True,max_length=200)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', height_field=None,width_field=None,max_length=200,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_author=models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username' #es de AbstractBaseUser se utiliza para definir si username o email sera el atributo unico
    REQUIRED_FIELDS = ['email','names']    #campos que ademas de username se solicitaran al crear el user por consola

    def __str__(self):
        return f'{self.names} {self.last_names}'
    