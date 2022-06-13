from django.shortcuts import render

from.models import Personnel

# Create your views here.

def list_personnels(request):
    personnels=Personnel.objects.all()
    context = {'personnels' :personnels}
    return render(request, 'personnels/list_personnels.html', context)