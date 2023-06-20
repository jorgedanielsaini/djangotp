from django.shortcuts import render
from django.http import HttpResponse
from .forms import contacto_form
from django.contrib import messages
from .models import Producto
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def club(request):
    return render(request, 'publica/club.html')

def productos(request):
    listado_productos = Producto.objects.all()
    
    return render(request, 'publica/productos.html', {"productos":listado_productos})

def contacto(request):
    mensaje = None #Ver clase 17
    #Si recibe la URL por POST toma los datos del formulario
    if request.method == "POST":
        formContacto = contacto_form(request.POST)
        #Se valida los datos is_valid()
        if formContacto.is_valid():
            messages.info(request,"El formulario se ha enviado con exito!")
            mjs = f'De: {formContacto.cleaned_data["nombre"]}, mail: {formContacto.cleaned_data["mail"]}, asunto: {formContacto.cleaned_data["asunto"]}, mensaje: {formContacto.cleaned_data["mensaje"]}'
            mjs_html = f"""
                <p>De: {formContacto.cleaned_data["nombre"]} <a href="mailto:{formContacto.cleaned_data["mail"]}">
                {formContacto.cleaned_data["mail"]}</a></p>
                <p>Asunto: {formContacto.cleaned_data["asunto"]}</p>
                <p>mensaje: {formContacto.cleaned_data["mensaje"]}</p>
            """  
            asunto = f"CONSULTA DE LA PÁGINA: {formContacto.cleaned_data['asunto']}"
            send_mail(
                asunto,
                mjs,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mjs_html
            )
            formContacto = contacto_form()      
        else:
          messages.info(request,"Error: verificar los campos del formulario")           
    #Si la URL es recibida por el metodo GET crea un formulario en blanco (sin datos)
    else:
        formContacto = contacto_form()
    return render(request, "publica/contacto.html", {"formContacto": formContacto})
    

