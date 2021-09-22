# Django
from django.contrib import admin
# Self
from .models import *
# Terceros

class ResultadoInline(admin.StackedInline):
    '''Tabular Inline View for Resultado'''

    model = Resultado
    min_num = 1
    extra = 0
    #raw_id_fields = ('eje',)


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    '''Admin View for Resultado'''

    list_display = (
        "codigo",
        "resultado",
        "presupuesto",
        'id',
        "eje",
    )
    search_fields = list_display[:4]
    ordering = ('codigo',)


@admin.register(Eje)
class EjeAdmin(admin.ModelAdmin):
    list_display = ('nombre','codigo','id')
    inlines = [
        ResultadoInline,
    ]
    search_fields = list_display
    ordering = ('nombre',)


class VariableInline(admin.StackedInline):
    model = Variable
    min_num = 3
    extra = 0


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    autocomplete_fields = ('resultado',)
    list_display = (
        "nombre",
        "codigo",
        "alcance",
        "periodicidad",
        'id',
        "resultado",
        'variable',
    )
    search_fields = list_display[:5]+('variable__nombre',)
    autocomplete_fields = ['variable','resultado']
    list_filter = ['alcance',]
    filter_horizontal = [
        "factores_desagregacion",
        "fuentes_informacion",
        "instituciones",
        ]
    ordering = ('nombre',)
    

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo', 'id']
    search_fields = list_display


class ValorFactorInline(admin.StackedInline):
    '''Stacked Inline View for ValorFactor'''
    model = ValorFactor
    min_num = 1
    extra = 0


@admin.register(FactorDesagregacion)
class FactorDesagregacionAdmin(admin.ModelAdmin):
    '''Admin View for FactorDesagregacion'''

    list_display = (
        "nombre",
        "codigo",
    )
    search_fields = list_display
    inlines = [ValorFactorInline,]


@admin.register(ValorFactor)
class ValorFactorAdmin(admin.ModelAdmin):
    '''Admin View for ValorFactor'''
    autocomplete_fields = ['categoria',]
    list_display = (
        "valor",
        "codigo",
        'categoria'
    )
    search_fields = list_display[:2]+('categoria__nombre',)


class UnidadMedidaInline(admin.StackedInline):
    model = UnidadMedida
    min_num = 1
    extra = 0


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    '''Admin View for Variable'''
    list_display = (
        "nombre",
        "tipo",
        'unidad',
    )
    search_fields = list_display[:2]
    autocomplete_fields =['unidad']


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "simbolo",
        )
    search_fields = list_display


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "codigo",
        "departamento",
    )
    search_fields = list_display[:2] + ('departamento__nombre',)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "codigo",
    )
    search_fields = list_display


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
        "municipio",
        )
    search_fields = list_display[:2]
    autocomplete_fields = ['municipio',]


@admin.register(MedicionIndicador)
class MedicionIndicadorAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'contenido',
        'indicador',
        'fecha',
        'valor_medicion',
        'valor_etario_inicial',
        'valor_etario_final',
        'area',
    )
    autocomplete_fields = ['indicador','area']
    filter_horizontal = ['valores_factor']
    search_fields = list_display[:6]


@admin.register(FuenteInformacion)
class FuenteInformacionAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "codigo",
    )
    search_fields = list_display
