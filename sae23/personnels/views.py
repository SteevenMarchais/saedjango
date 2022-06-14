from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from.models import Personnel

# Create your views here.

def list_personnels(request):
    personnels=Personnel.objects.all()
    context = {'personnels' :personnels}
    return render(request, 'personnels/list_personnels.html', context)

def personnels_detail(request, pk):
	personnel = get_object_or_404 (Personnel, secu=pk)
	context={'personnel': personnel}
	return render(request, 'personnels/personnel_detail.html', context)