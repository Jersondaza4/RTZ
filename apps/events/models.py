from django.db import models
#from django.contrib.postgres.fields import ArrayField
from tinymce.models import HTMLField


# Create your models here.
class Event(models.Model):
    tittle = models.CharField(max_length=200)
    description = HTMLField()
    event_date = models.DateField()
    place = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('carrera', 'Carrera'), ('encuentro', 'Encuentro')])
    image = models.ImageField(upload_to='events_img/')  # Para imágenes del evento
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.tittle


class EventGalery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #images = ArrayField(models.ImageField(upload_to='galeria_eventos/'), blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'

    def __str__(self):
        return f"Galería de {self.event.titulo}"    


class EventOrganizer(models.Model):
    TIPOS_ORGANIZADOR = (
        ('persona', 'Persona'),
        ('empresa', 'Empresa'),
    )

    type = models.CharField(max_length=10, choices=TIPOS_ORGANIZADOR)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='organizadores/', blank=True, null=True)

    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    web_site = models.URLField()
    #logo = ArrayField(models.ImageField(upload_to='patrocinadores/'))

    class Meta:
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'

    def __str__(self):
        return self.name


class EventCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.evento.titulo}"


class ContactUs(models.Model):
    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Correo')
    subject = models.CharField('Asunto', max_length=200)
    message = models.TextField('Mensaje')
    created_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f"Mensaje de {self.name} ({self.email})"
