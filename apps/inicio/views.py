# from django.shortcuts import render_to_response
from django.views.generic import TemplateView, FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles
# from django.template import RequestContext

# def index(request):
# 	#en el context instance se le manda el contexto y dentro del contexto se va el css
# 	#por lo tanto si no lo enviamos no se asigna el css las vistas basadas en clases ya eredan este 
# 	#metodo por lo que no es necesario enviarle el contexto
# 	return render_to_response('inicio/index.html', context_instance = RequestContext(request))



# class Index2(TemplateView):
# 	template_name = 'inicio/cla.html'

class Registrarse(FormView):
	template_name = "inicio/registrarse.html"
	form_class = UserForm
	success_url = reverse_lazy('registrarse')
	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario=user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse, self).form_valid(form)
