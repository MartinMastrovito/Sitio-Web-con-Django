from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): ##definimos el objeto post del foro/blog. el models.model hace que django identifique esto como un objeto y lo guarde en la base de datos
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link a otro modelo
    title = models.CharField(max_length=200)#texto con caracteeres limitados
    text = models.TextField() #texto sin limite
    created_date = models.DateTimeField( #fecha y hora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #metodo para publicar
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #devuelve el nombre del post
        return self.title

