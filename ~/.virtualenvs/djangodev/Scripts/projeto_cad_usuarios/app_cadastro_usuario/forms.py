from django import forms
from .models import Reservation

#formulario para conseguir a reserva
class ReservationForm(forms.ModelForm):
        data = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
        timeslot = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
        class Meta:
         model = Reservation
         fields = ['name','data', 'timeslot'] 

