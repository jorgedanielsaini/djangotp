from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="producto", null=True)

    def __str__(self):
        return f"{self.nombre}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="./perfil/plantita.png", upload_to="perfil", null=True)

    def __str__(self):
        return f"Perfil de {self.user}"
    
    def seguidores(self):
        user_ids = Relacion.objects.filter(desde_user=self.user)\
                            .values_list("a_user_id", flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def seguidos(self):
        user_ids = Relacion.objects.filter(a_user=self.user)\
                            .values_list("desde_user_id", flat=True)
        return User.objects.filter(id__in=user_ids)
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    fechaPost = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

    class Meta:
        ordering = ["-fechaPost"]
    
    def __str__(self):
        return f"{self.user.username}: {self.contenido}"

class Relacion(models.Model):
    desde_user = models.ForeignKey(User, related_name="relacion", on_delete=models.CASCADE)
    a_user = models.ForeignKey(User, related_name="a_relacion", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.desde_user} a {self.a_user}"

    