
from django.urls import path
from app_cadastro_usuario import views

#Urls do site para colocar na web
urlpatterns = [
   path('',views.home,name='home'),
   path('templates/',views.Usuarios,name = 'listagem_usuarios'),
   path('list/', views.reservation_list, name='reservation_list'),
   path('make_reservation/', views.make_reservation, name='make_reservation')


]
