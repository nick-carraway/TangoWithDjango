from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about1/', views.about1, name='about1'), #this line is also purely experimental!

]
