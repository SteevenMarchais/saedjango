from django.shortcuts import render

# Create your views here.

def list_infra(request):
    context = {}
    return render(request, 'infrastructures/list_infra.html', context)