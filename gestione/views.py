from django.http import HttpResponse
import qrcode
import base64
from io import BytesIO
from django.shortcuts import render
from .models import Sede
from .utils import genera_qr_code

def qr_code_view(request, sede_id):

    # Recupera la sede dal DB (oppure usa un URL personalizzato per il prodotto)
    sede_url = f"http://esempio.com/sede/{sede_id}"
    
    # Genera il QR code
    img = genera_qr_code(sede_url)
    
    # Ritorna il QR code come risposta (immagine)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return HttpResponse("Benvenuto nella sezione gestione!");

def home(request):
    return HttpResponse("per admin: https://literate-pancake-pj997jvjqpqjhq44-8000.app.github.dev/admin/")

def sede_qr_page(request, sede_id):
    sede = Sede.objects.get(pk=sede_id)
    url = f"http://esempio.com/sede/{sede_id}"

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "gestione/qr_page.html", {
        "sede": sede,
        "qr_code": img_str
    })

def lista_aziende(request):
    aziende = aziende.objects.all()
    return render(request, 'gestione/aziende.html', {'aziende': aziende})

def lista_sedi(request):
    sedi = Sede.objects.select_related('azienda').all()
    return render(request, 'gestione/sede_list.html', {'sedi': sedi})

def qr_code_view(request):
    url = "https://literate-pancake-pj997jvjqpqjhq44-8000.app.github.dev/gestione/"
    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")