from django.shortcuts import render, HttpResponse

html_base = """
<h1>Web Personal </h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contácto</a></li>
</ul>
"""
# Create your views here.
def home(request):
    return HttpResponse(html_base+"""
    <h2>Portada</h2>
    <p>Ejemplo parrafo portada</p>
    """)

def about(request):
    return HttpResponse(html_base+"""
    <h2>Acerca de</h2>
    <p>Ejemplo parrafo about-me</p>
    """)

def portfolio(request):
    return HttpResponse(html_base+"""
    <h2>Portafolio</h2>
    <p>Ejemplo parrafo portafolio</p>
    """)

def contact(request):
    return HttpResponse(html_base+"""
    <h2>Contacto</h2>
    <p>Ejemplo parrafo contacto</p>
    """)
