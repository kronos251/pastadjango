from django.shortcuts import render,redirect
from .models import usuario,Reservation
from django.contrib import messages
from .forms import ReservationForm
from django.http import JsonResponse
import datetime

#
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

def is_time_slot_available(selected_time_slot):
    # Converta a string do horário selecionado em um objeto de data e hora
    selected_time = datetime.strptime(selected_time_slot, '%Y-%m-%dT%H:%M')

    # Verifique se já existe uma reserva para o horário selecionado
    if Reservation.objects.filter(data=selected_time.date(), timeslots=selected_time.time()).exists():
        return False
    else:
        return True
    
#logica para fazer a reserva
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
          data = form.cleaned_data['data']
          timeslot = form.cleaned_data['timeslot']
          if is_time_slot_available(data,timeslot):
            form.save()
            redirect_url = redirect('reserva_sucess').url
            return JsonResponse({'success': True, 'message': 'deu tudo certo'})
        else:
            print(form.errors)
            return JsonResponse({'success': False, 'message': 'Dados inválidos'})
    return JsonResponse({'success': False, 'message': 'Método inválido'})


def reserva_success_view(request):
    return render(request, 'reserva_success.html')
    





