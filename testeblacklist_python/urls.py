from django.contrib import admin
from django.urls import path, include

from testeblacklist_python import views


urlpatterns = [
    path('<str:cpfConsulta>/', views.consulta),
    path('', views.index),
    path('admin/', admin.site.urls),
]
