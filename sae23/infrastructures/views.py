from django.shortcuts import render

from .models import Infrastructures

# Create your views here.

def list_infra(request):
    infras=Infrastructures.objects.all()
    context = {'infras' :infras}
    return render(request, 'infrastructures/list_infra.html', context)