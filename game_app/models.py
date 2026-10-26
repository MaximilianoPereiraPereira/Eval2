from django.db import models

# -------------Tablas----------------
class Categoria (models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre


class Cuenta (models.Model):
    usuario = models.CharField(max_length=80, unique= True)
    correo = models.CharField(max_length=120)
    class Meta:
        verbose_name_plural = "Cuentas"
        ordering = ["usuario"]
    def __str__(self):
        return  f"{self.usuario}${self.correo}"

class Personaje (models.Model):
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    nivel = models.PositiveIntegerField()
    ban = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    
    cuenta = models.ManyToManyField(
        Cuenta,
        related_name="Cuentas"
    )

    class Meta:
        verbose_name_plural = "Personajes"
        ordering = ["nivel"]
    def __str__(self):
        return f"{self.descripcion} ${self.nivel}"
    
class Item (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    nivel = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1)

    personaje = models.ForeignKey(Personaje.raza,on_delete=models.CASCADE,related_name="Personajes")
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="Categorias")

    class Meta:
        verbose_name_plural = "Items"
        ordering = ["nombre"]
    def __str__(self):
        return f"{self.nombre}${self.descripcion}${self.nivel}${self.cantidad}"
