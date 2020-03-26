from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')
