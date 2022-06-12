from django.shortcuts import render

# Create your views here.

def list_machines(request):
    context = {}
    return render(request, 'machines/list_machines.html', context)