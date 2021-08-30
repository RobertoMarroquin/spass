from django.db import models

# Create your models here.
class Eje(models.Model):
    codigo = models.CharField("Codigo", max_length=50,blank=True, null=True)
    nombre = models.CharField("Nombre",max_length=150,blank=True, null=True)
    estrategia = models.TextField("Estrategia", blank=True, null=True)
    problematica = models.TextField("Problematica", blank=True, null=True)

    class Meta:
        verbose_name = ("Eje")
        verbose_name_plural = ("Ejes")

    def __str__(self):
        return self.codigo


class Resultado(models.Model):
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)
    resultado = models.TextField("Resultado", blank=True, null=True)
    presupuesto = models.TextField("Presupuesto", blank=True, null=True)
    eje = models.ForeignKey("visor.Eje", on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Resultado")
        verbose_name_plural = ("Resultados")

    def __str__(self):
        return self.codigo


class Indicador(models.Model):
    resultado = models.ForeignKey("visor.Resultado", on_delete=models.CASCADE,related_name='indicadores')
    codigo = models.CharField('Codigo', max_length=50, blank=True, null=True)
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    alcance = models.IntegerField(("Alcance"), choices=((1,"Corto"),(2,"Medio"),(3,"Largo")), blank=True, null=True)
    periodicidad = models.IntegerField(("Periodicidad de medicion"), choices=((1,"Anual"),(2,"Semestral"),(3,'Cuatrimestral'),(4,"Trimestral"),(5,'Mensual')), blank=True, null=True)
    fuente_verificacion = models.TextField(("Fuente de Verificacion"), blank=True, null=True)
    notas = models.TextField(("Notas Tecnicas"), blank=True, null=True)
    informacion_requerida = models.TextField(("Informacion a Requerir"), blank=True, null=True)
    formula = models.TextField(("Formula"),blank=True, null=True)
    
    variable = models.ForeignKey('visor.Variable', related_name='indicador', on_delete=models.CASCADE,blank=True, null=True)
    factores_desagregacion = models.ManyToManyField('visor.FactorDesagregacion', related_name='indicadores')
    fuentes_informacion = models.ManyToManyField('visor.FuenteInformacion', related_name='indicadores')
    instituciones = models.ManyToManyField('visor.Institucion', related_name='indicadores')
    
    class Meta:
        verbose_name = ("Indicador")
        verbose_name_plural = ("Indicadores")

    def __str__(self):
        return self.codigo


class Institucion(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return f'{self.codigo}' 


class FactorDesagregacion(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Factor Desagregacion'
        verbose_name_plural = 'Factores Desagregacion'

    def __str__(self):
        return f'{self.codigo}' 


class ValorFactor(models.Model):
    valor = models.CharField(("Valor"), max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)
    categoria = models.ForeignKey("visor.FactorDesagregacion", related_name='valores',on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Valor Factor'
        verbose_name_plural = 'Valores Factor'

    def __str__(self):


        return f'{self.valor}' 


class Variable(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    tipo = models.IntegerField(("Tipo"), choices=((1,"Cualitativo"),(2,"Cuantitativo")), default=1)
    unidad = models.ForeignKey('visor.UnidadMedida',related_name='variable', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

    def __str__(self):
        return f'{self.nombre}'


class UnidadMedida(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    simbolo = models.CharField(("Simbolo"), max_length=5, blank=True, null=True)
    class Meta:
        verbose_name = 'Unidad edida'
        verbose_name_plural = 'Unidades Medida'

    def __str__(self):
        return f'{self.nombre}'


class MedicionIndicador(models.Model):
    codigo = models.CharField('Codigo', max_length=50)
    contenido = models.TextField(("Contenido"))
    indicador = models.ForeignKey("visor.Indicador", on_delete=models.CASCADE, related_name="mediciones")
    valores_factor = models.ManyToManyField("visor.ValorFactor")
    area = models.ForeignKey('visor.Area', related_name='indicadores', on_delete=models.CASCADE)
    valor_medicion = models.CharField('Valor de Medicion', max_length=50)
    valor_etario_inicial = models.IntegerField(("Valor Etario Inicial"),blank=True, null=True)
    valor_etario_final = models.IntegerField(("Valor Etario Final"),blank=True, null=True)
    
    class Meta:
        verbose_name = 'Medicion de Indicador'
 
    def __str__(self):
        return f'{self.codigo}' 


class Area(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    descripcion = models.TextField("Descripcion", blank=True, null=True)
    municipio = models.ForeignKey('visor.municipio', related_name='areas', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return f'{self.nombre }'


class Municipio(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField('Codigo', max_length=50, blank=True, null=True)
    departamento = models.ForeignKey('visor.Departamento', related_name='municipios', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f'{self.nombre}'


class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=True, null=True)
    codigo = models.CharField(("Codigo"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.nombre}'


class FuenteInformacion(models.Model):
    nombre = models.CharField('Nombre',max_length=150, blank=True, null=True)
    codigo = models.CharField('Codigo',max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Fuente de Informacion")
        verbose_name_plural = ("Fuentes de Informacion")

    def __str__(self):
        return self.nombre

