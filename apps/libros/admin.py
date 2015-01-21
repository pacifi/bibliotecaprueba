from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'resume', 'imagen_portadas')
	list_filter = ('autor',)
	search_fields = ('nombre', 'autor__nombre')
	list_editable = ('nombre','resume')
	filter_horizontal = ('autor',)

	def imagen_portadas(self, libro):
		url = libro.traer_url_portadas()
		tag = "<img src='%s' width='100' eight='100' />" %url
		return tag

	imagen_portadas.allow_tags = True

admin.site.register(Libro,LibroAdmin)	