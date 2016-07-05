from django.shortcuts import render, get_object_or_404
from .models import TethysServer,Container

# Create your views here.
def container_list(request):
	containers = Container.objects.all().order_by('name')
	content_dict = {
					'containers':containers,
					}
	return render(request, 'tethys/container_list.html', content_dict)
	
def refresh_container(container):
	container.refresh()
	
def container_detail(request,name):
	container = get_object_or_404(Container,name=name)
	content_dict = {
					'container':container,
					}
	return render(request,'tethys/container_detail.html',content_dict)
	
