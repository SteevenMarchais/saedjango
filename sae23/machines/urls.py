from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.list_machines, name="list_machines"),
    path('machines/<pk>',views.machines_detail, name='machine-detail'),

]