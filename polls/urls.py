from django.conf.urls import url
from . import views

app_name='polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.choices, name='choices'),
    url(r'^(?P<question_id>[0-9]+)/selected/$', views.selected, name='selected'),
]

 