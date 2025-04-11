"""
URL configuration for azienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect



urlpatterns = [
    path('', lambda request: redirect('gestione/', permanent=False)),
    path('admin/', admin.site.urls),
    path('gestione/', include('gestione.urls')),
    path('sedi/', views.lista_sedi, name='lista_sedi'),
]

def qr_code_view(request, sede_id):
    # Recupera la sede dal DB (oppure usa un URL personalizzato per il prodotto)
    sede_url = f"http://esempio.com/sede/{sede_id}"
    
    # Genera il QR code
    img = genera_qr_code(sede_url)
    
    # Ritorna il QR code come risposta (immagine)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
