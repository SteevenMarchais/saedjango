from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.list_infra, name="list_infra"),
    path('infrastructures/<pk>', views.infra_detail, name='infra-detail'),
]