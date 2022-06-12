from django.shortcuts import render

# Create your views here.

def list_personnels(request):
    context = {}
    return render(request, 'personnels/list_personnels.html', context)