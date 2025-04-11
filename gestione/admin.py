from django.contrib import admin
from .models import Cliente, Azienda, Sede, Prodotto

class SedeInline(admin.TabularInline):
    model = Sede
    extra = 1

class AziendaAdmin(admin.ModelAdmin):
    inlines = [SedeInline]
    list_display = ("nome", "cliente")
    search_fields = ("nome",)

class ProdottoAdmin(admin.ModelAdmin):
    list_display = ("nome", "prezzo", "azienda")
    list_filter = ("azienda",)

admin.site.register(Cliente)
admin.site.register(Azienda, AziendaAdmin)
admin.site.register(Sede)
admin.site.register(Prodotto, ProdottoAdmin)
