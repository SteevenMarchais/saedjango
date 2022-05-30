from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine,Personnel
from .forms import AddMachineForm, AddPersonnelForm
from requests import post

def index(request):
	context = {}
	return render (request, 'index.html', context)
	
def machine_list_view(request):
	machines = Machine.objects.all()
	context={'machines': machines}
	return render(request, 'computerapp/machine_list.html', context)

def machine_detail_view(request, pk):
	machine = get_object_or_404 (Machine, id=pk)
	context={'machine': machine}
	return render(request, 'computerapp/machine_detail.html', context)


def personnel_list_view(request):
	personnels = Personnel.objects.all()
	context={'personnels': personnels}
	return render(request, 'computerapp/personnel_list.html', context)

def personnel_detail_view(request, pk):
	personnel = get_object_or_404 (Personnel, secu=pk)
	context={'personnel': personnel}
	return render(request, 'computerapp/personnel_detail.html', context)

def machine_add_form(request):
	if request.method == 'POST':
		form = AddMachineForm(request.Post or None)
		if form.is_valid():
			new_machine = Machine(nom=form.cleaned_data['nom'])
			new_machine.save()
			return redirect('machines')
	else :
		form = AddMachineForm()
	context = {'form': form }
	return render(request, 'computerapp/machine_add.html', context)

def personnel_add_form(request):
	if request.method == 'POST':
		form = AddPersonnelForm(request.POST or None)
		if form.is_valid():
			new_personnel = Personnel(nom=form.cleaned_data['nom'])
			new_personnel.save()
			return redirect('personnels')
	else :
		form = AddPersonnelForm()
	context = {'form': form }
	return render(request, 'computerapp/personnel_add.html', context)