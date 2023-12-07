from django.shortcuts import render
from .models import Testi

def index(request):
    """The home page for Travel Journals."""
    return render(request, 'game_portfolio/index.html')

def tests(request):
    """show all Testis"""
    tests = Testi.objects.order_by('date_added')
    context = {'tests':tests}
    return render(request, 'game_portfolio/tests.html', context)