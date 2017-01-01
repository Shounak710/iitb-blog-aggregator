from django.shortcuts import render
from django.views import generic
from .models import Items
# Create your views here.

#class IndexView(generic.ListView):
	#template_name = 'home/index.html'

def index(request):
	items = Items.objects.order_by('-id')[:5]
	return render(request, 'blog/index.html', {'items': items})