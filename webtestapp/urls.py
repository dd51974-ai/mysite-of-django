from django.urls import path

from . import views

app_name = 'webtestapp'
urlpatterns = [
    #path('', views.index, name='index'),
    # ex: /webtestapp/
    path('info', views.info, name='info'),
    #path('create', views.create, name='create'),
]