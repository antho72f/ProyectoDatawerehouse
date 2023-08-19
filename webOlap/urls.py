
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('graficos', views.graficos, name='graficos'),
    path('graficos/grafico_ventas', views.grafico_ventas, name='grafico_ventas'),
    path('graficos/comparacion-ubicaciones', views.comparacion_ubicaciones, name='comparacion_ubicaciones'),
    path('graficos/grafico-impacto-facilidades', views.grafico_impacto_facilidades, name='grafico_impacto_facilidades'),
    path('graficos/comparacion-tipos-escuelas', views.comparacion_tipos_escuelas, name='comparacion_tipos_escuelas'),
    path('graficos/comparacion-tipos-facilidades', views.comparacion_tipos_facilidades, name='comparacion_tipos_facilidades'),
    path('graficos/grafico-dispersion-tiempo-transporte', views.grafico_dispersion_tiempo_transporte, name='grafico_dispersion_tiempo_transporte'),
    path('graficos/grafico-comparacion', views.grafico_comparacion, name='grafico_comparacion'),
]
