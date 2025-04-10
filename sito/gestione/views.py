import qrcode
import base64
from django.shortcuts import render
from django.http import HttpResponse
from .utils import genera_qr_code
from io import BytesIO
from .models import Sede


def qr_code_view(request, sede_id):
    # Recupera la sede dal DB (oppure usa un URL personalizzato per il prodotto)
    sede_url = f"http://esempio.com/sede/{sede_id}"
    
    # Genera il QR code
    img = genera_qr_code(sede_url)
    
    # Ritorna il QR code come risposta (immagine)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "gestione/qr_page.html", {
        "sede": sede,
        "qr_code": img_str
    })
