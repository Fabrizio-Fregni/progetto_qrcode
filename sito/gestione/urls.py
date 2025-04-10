from django.urls import path
from . import views

urlpatterns = [
    path('qr_code/<int:sede_id>/', views.qr_code_view, name='qr_code'),
]

path('sede_qr/<int:sede_id>/', views.sede_qr_page, name='sede_qr_page'),
