from django.db import models

# Create your models here.



class usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome  = models.TextField(max_length=255)
    idade = models.IntegerField()


class Reservation(models.Model):
    user = models.ForeignKey(usuario, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time}"
    

