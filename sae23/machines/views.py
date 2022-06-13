from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect


from .models import Machine

# Create your views here.

def list_machines(request):
    machines=Machine.objects.all()
    context = {'machines' :machines}
    return render(request, 'machines/list_machines.html', context)


def machines_detail(request, pk):
	machines = get_object_or_404 (Machine, id=pk)
	context={'machines': machines}
	return render(request, 'machines/machines_detail.html', context)