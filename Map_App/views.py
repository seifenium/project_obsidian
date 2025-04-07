from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = 'Map_App/landing.html'