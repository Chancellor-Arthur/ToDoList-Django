from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('path_reg', views.path_reg, name='path_reg'),
    path('authorize', views.authorize, name='authorize'),
    path('registrate', views.registrate, name='registrate'),
]
