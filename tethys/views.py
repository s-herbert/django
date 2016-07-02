from django.shortcuts import render

# Create your views here.
def container_list(request):
	return render(request, 'tethys/container_list.html', {})