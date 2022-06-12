from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.list_personnels, name="list_personnels"),
]