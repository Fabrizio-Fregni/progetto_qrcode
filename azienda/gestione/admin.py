from django.contrib import admin
from .models import Cliente, Azienda, Sede, Prodotto

admin.site.register(Cliente)
admin.site.register(Azienda)
admin.site.register(Sede)
admin.site.register(Prodotto)
