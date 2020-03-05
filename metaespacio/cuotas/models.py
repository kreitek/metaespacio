from django.db import models
from espacios.models import Espacio, Miembro


class FormaPago(models.Model):

    "Efectivo, Cuenta corriente, Stripe?, Otras"
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    porcentaje_comision = models.FloatField(default=0.0)
    comision_fija = models.FloatField(default=0.0)
    liquido = models.BooleanField(default=True)
    color = models.CharField(max_length=30, default="", blank=True)
    posicion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('posicion', )
        verbose_name = "forma de pago"
        verbose_name_plural = "formas de pago"


class CuotaPeriodica(models.Model):

    "Cantidad mensual a aportar por miembro"
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} euros/mes [{}-{}]".format(
            self.cantidad,
            self.fecha_inicial.strftime("%m/%y"),
            self.fecha_final.strftime("%m/%y") if self.fecha_final else "-")

    class Meta:
        verbose_name = "cuota periódica"
        verbose_name_plural = "cuotas periódicas"


class Pago(models.Model):
    tiposDePago = ((1, 'Ingresos'),
                   (2, 'Neutro'),
                   (3, 'Gastos'), )

    pagador = models.ForeignKey(Miembro, blank=True, null=True, on_delete=models.SET_NULL)
    fecha = models.DateField()
    cantidad = models.FloatField()
    tipo = models.IntegerField(choices=tiposDePago, default=1)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{} pagó {:.2f} € el dia {} por {}".format(
            self.pagador,
            self.cantidad,
            self.fecha,
            self.forma_pago)

    class Meta:
        ordering = ('fecha', )


class CategoriaPago(models.Model):

    "Cuotas, Cursos, , Extra"
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=30, default="", blank=True)
    posicion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('posicion', )
        verbose_name = "categoría de pago"
        verbose_name_plural = "categoríasde de pago"


class Mensualidad(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(CategoriaPago, default=1, on_delete=models.CASCADE)
    cantidad = models.FloatField()

    class Meta:
        ordering = ('-fecha', )
        verbose_name = "mensualidad"
        verbose_name_plural = "mensualidades"
