from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True

    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural="Categorias"


class Indices(ClaseModelo):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de el indice ',
        unique=True
    )
    ponderacion = models.FloatField(
        null=True,
        blank=True,
        help_text='Valoration for the index'
    )

    def __str__(self):

        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Indices,self).save()

    class Meta:
        verbose_name_plural="Indices"
        unique_together = ('categoria','descripcion','ponderacion') 
        
        

class Ajustes(ClaseModelo):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        null=False,
        help_text='Descripcion de el tipo de ajuste',
        unique=True
    )
    ajuste = models.FloatField(
        null=False,
        max_length=3,
        help_text='Ponderacion de ajuste'
    )

    def __str__(self):

        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Ajustes,self).save()
 
    class Meta:
        verbose_name_plural="Ajustes"
        # unique_together = ('categoria','descripcion','ajuste') 