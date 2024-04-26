from django.shortcuts import render
from .models import usuario,Reservation

def home(request):
    return render(request,'home.html')
def Usuarios(request):
    #salvamento da pagina html para o banco de dados
    novo_usuario = usuario()
    novo_usuario.Prontuario = request.POST.get('Prontuario')
    novo_usuario.save()
    #exibir todos os usuarios ja cadastrados em uma nova pagina

    usuarios = {
        'usuarios':usuario.objects.all()
    }

    #retornar os dados 
    return render(request,'usuarios.html',usuarios)


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def make_reservation(request):
    # Lógica para criar uma reserva
    pass
    





