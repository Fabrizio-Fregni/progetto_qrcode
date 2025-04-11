from django.urls import path
from . import views

urlpatterns = [
    path('qr_code/<int:sede_id>/', views.qr_code_view, name='qr_code'),
]
