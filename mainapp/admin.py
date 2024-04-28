from django.contrib import admin
from .models import TipoDocumento, Personas

# Register your models here.
class TipoDocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    search_fields = ('nombre', 'Personas__cedula')
    list_display=('nombre', 'creado', 'actualizado' )
    ordering = ('-creado',)
    
class PersonasAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'creado', 'actualizado')
    search_fields = ('tipoDocumento', 'cedula', 'user__username', 'fNacimiento')
    list_filter = ('publico',)
    list_display=('cedula', 'publico', 'creado', 'actualizado' )
    ordering = ('-creado',)
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()
    
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Personas, PersonasAdmin)