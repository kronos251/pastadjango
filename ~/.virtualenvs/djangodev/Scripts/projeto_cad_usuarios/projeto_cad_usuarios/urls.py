
from django.urls import path
from app_cadastro_usuario import views

urlpatterns = [
   path('',views.home,name='home'),
   path('templates/',views.Usuarios,name = 'listagem_usuarios'),
   path('list/', views.reservation_list, name='reservation_list'),

]
