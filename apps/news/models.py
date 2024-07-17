from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from apps.user.models import User

class Category(models.Model):
    name = models.CharField('Nombre de la categoría', max_length=100, null=False, blank=False)
    is_active = models.BooleanField('Esta activa', default=True)
    created_at = models.DateField('Creado el', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name
    

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_trainee = models.BooleanField('Esta en prueba', default=True)
    is_active = models.BooleanField('Esta activa', default=True)

    '''def clean(self): #se ejecuta siempre que se haga un cambio al modelo
        if self.names.lower == 'carlos':
            raise ValidationError('no puedes agregar a carlos')'''
    
    '''def save(self,*args,**kwargs): #se ejecuta siempre evalua si es get, post, delete, update
        if self.names.lower == 'carlos':
            raise ValidationError('no puedes agregar a carlos')
        super(Author,self).save(*args,**kwargs)'''

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.user.names
    

class News(models.Model):
    title = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField('Descripción', max_length=110, blank=False, null=False)
    content = RichTextField('Contenido')
    image = models.ImageField(upload_to='news_img/')  # Portada
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField('Esta activo', default=True)
    created_at = models.DateField('Creado en',auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.title
    

    '''signal es como un triguer que se ejecuta de cierta accion como eliminar, guardar, etc
    def quitar_relacion_author_libor(sender,instance,**kwargs):
        if instance.status == False:
            author=instance.id
            libros=Libro.objcets.filter(author_id=author)
            for libro in libros:
                libro.author_id.remove(author)
    
    post_save.connect(quitar_relacion_author_libor,sender=Author)
    '''

    '''
    def reducir_cantidad_libro(sender,instance,**kwargs):
        libro=instance.libro
        if libro.cantidad >0:
            libro.cantidad=libro.cantidad-1
            libro.save()

    def validar_creacion_reserva(sender,instance,**kwargs):
        libro=instance.libro
        if libro.cantidad <1:
            raise Exception('no se puede realizar')

    post_save.connect(reducir_cantidad_libro,sender=Reserva) 
    pre_save.connect(validar_creacion_reserva,sender=Reserva) 
    '''