from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Libro
from apps.autores.models import Autor
from django.core import serializers
from django.http import HttpResponse

class BuscarView(TemplateView):
	"""docstring for BuscarView"""
	
	def post(self, request, *args,**kwargs):
		buscar = request.POST['buscalo']
		libros = Libro.objects.filter(nombre__contains=buscar)	
		if libros:
			datos = []
			for libro in libros:
				autores = libro.autor.all()
				datos.append(dict([(libro,autores)]))
			
			return render(request,'libros/buscar.html', {'datos':datos})
		else:
			autores = Autor.objects.filter(nombre__contains=buscar)
			print autores
		return render(request, 'libros/buscar.html',{'autores':autores,'autor':True})

class BusquedaView(ListView):
	model = Autor
	template_name = 'libros/busqueda.html'
	context_object_name = 'autores'

class BusquedaAjaxView(TemplateView):
	"""docstring for BusquedaAjaxView"""
	def get(self, request, *args, **kwargs):
		id_autor = request.GET['id']
		libros = Libro.objects.filter(autor__id=id_autor)
		data = serializers.serialize('json',libros,fields=('nombre','resume'))
		print data
		return HttpResponse(data, content_type='application/json')
		
		