from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .models import Infrastructures

# Create your views here.

def list_infra(request):
    infras=Infrastructures.objects.all()
    context = {'infras' :infras}
    return render(request, 'infrastructures/list_infra.html', context)

def infra_detail(request, pk):
	infra = get_object_or_404 (Infrastructures, nom=pk)
	context={'infra': infra}
	return render(request, 'infrastructures/infra_detail.html', context)