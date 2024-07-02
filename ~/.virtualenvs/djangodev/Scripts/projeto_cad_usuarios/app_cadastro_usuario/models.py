from django.db import models
import datetime
# Create your models here.


#banco de dados para o usuario
class usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome  = models.TextField(max_length=255)
    idade = models.IntegerField()

#banco de dados para a reserva
class Reservation(models.Model):
    name = models.CharField(max_length= 100,null=False)
    data = models.DateTimeField(null=False,default=datetime.date.today)
    timeslot = models.DateTimeField(null=False)

    class Meta:
        unique_together = ('data','timeslot')

    def __str__(self):
        return f"{self.nome}"
    

