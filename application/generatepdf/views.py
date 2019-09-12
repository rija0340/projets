from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render


def index(request):
    auteur = Auteur.objects.all()
    return render(request, 'generatepdf/index.html', {'auteurs' : auteur })



class Pdf(View):

    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('generatepdf/pdf.html', params)