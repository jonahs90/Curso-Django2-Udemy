from django.shortcuts import render, HttpResponse

html_base = """
<h1>Web Personal </h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
"""
# Create your views here.
def home(request):
    return HttpResponse(html_base+"<h2>Portada</h2><p>Ejemplo parrafo portada</p>")

def about(request):
    return HttpResponse("<h1>Web Personal </h1><h2>Acerca de</h2>")
