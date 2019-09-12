from django.urls import path

from .views import Pdf
from . import views

app_name = 'generatepdf'

urlpatterns = [
    path(' ', views.index, name='index'),
    path('render/', Pdf.as_view(), name='renderpdf')

]