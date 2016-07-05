from django.shortcuts import render
from .models import TethysServer,Container

# Create your views here.
def container_list(request):
	return render(request, 'tethys/container_list.html', {})