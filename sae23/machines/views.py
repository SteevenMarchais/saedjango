from django.shortcuts import render

from .models import Machine

# Create your views here.

def list_machines(request):
    machines=Machine.objects.all()
    context = {'machines' :machines}
    return render(request, 'machines/list_machines.html', context)