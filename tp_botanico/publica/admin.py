from django.contrib import admin
from .models import Producto, Perfil, Post, Relacion

# Register your models here.
admin.site.register(Producto)
admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(Relacion)
