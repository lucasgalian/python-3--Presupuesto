from django.db import models
from django.utils import timezone
# Create your models here.
# Create your models here.
class Presupuesto(models.Model):
       titulo = models.CharField(
       max_length=50,
       verbose_name='Nombre'
       )
       materiaPrima = models.CharField(max_length= 50)
       manoDeObra = models.IntegerField()
       fecha = models.DateTimeField(blank=True, null=True)
       precio = models.IntegerField(
            max_length=50, verbose_name='PrecioTotal')
       
       def __str__(self):
        return self.titulo 
       
       def publico(self):
             self.fecha = timezone.now()
             self.save()


#class Meta:
 #      ordering= ["-titulo"]  

 
# Create your models here.
