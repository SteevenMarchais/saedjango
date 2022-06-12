from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddMachineForm, AddPersonnelForm
from requests import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
	context = {}
	return render (request, 'computerapp/index.html', context)
