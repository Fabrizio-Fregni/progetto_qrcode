from django.shortcuts import render
from django.http import HttpResponse
from .utils import genera_qr_code # type: ignore

def qr_code_view(request, sede_id):
    # Recupera la sede dal DB (oppure usa un URL personalizzato per il prodotto)
    sede_url = f"http://esempio.com/sede/{sede_id}"
    
    # Genera il QR code
    img = genera_qr_code(sede_url)
    
    # Ritorna il QR code come risposta (immagine)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
