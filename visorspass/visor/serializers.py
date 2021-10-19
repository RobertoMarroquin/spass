# Django
from django.urls.base import reverse_lazy
# Rest-Framework
from rest_framework import serializers
from rest_framework.filters import SearchFilter
from rest_framework.relations import ManyRelatedField, PrimaryKeyRelatedField
# Self
from .models import *

class EjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eje
        fields = '__all__'


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


class FuenteInformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteInformacion
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class ResultadoSerializer(serializers.ModelSerializer):
    eje = EjeSerializer(many=False, read_only=True, required=False)
    eje_codigo = serializers.ReadOnlyField(source='eje.codigo')
    class Meta:
        model = Resultado
        fields = '__all__'


#Hyperlinkedmodelserilizers
class H_EjeSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:eje-detalle")
    class Meta:
        model = Eje
        fields = '__all__'


class H_InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:institucion-detalle")
    class Meta:
        model = Institucion
        fields = '__all__'


class H_FuenteInformacionSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:fuenteInformacion-detalle")
    class Meta:
        model = FuenteInformacion
        fields = '__all__'


class H_DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:departamento-detalle")
    class Meta:
        model = Departamento
        fields = '__all__'


class H_FactorDesagregacionSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:factorDesagregacion-detalle")
    #valores = serializers.HyperlinkedRelatedField(view_name='visor:valorFactor-detalle',many=True, read_only=True,)
    valores = serializers.SlugRelatedField(many=True,read_only=True,slug_field='valor')
    class Meta:
        model = FactorDesagregacion
        fields ='__all__'
    

class H_ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:resultado-detalle")
    eje = H_EjeSerializer(many=False, read_only=True)#serializers.PrimaryKeyRelatedField(source='eje',read_only=True)
    #eje_url = serializers.HyperlinkedRelatedField(read_only=True,source='eje' ,view_name='visor:eje-detalle')
    class Meta:
        model = Resultado
        fields = '__all__'


class H_MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:municipio-detalle",)
    departamento = H_DepartamentoSerializer(many=False, read_only=True)
    class Meta:
        model = Municipio
        fields = '__all__'


class H_AreaSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:area-detalle")
    municipio = H_MunicipioSerializer(many=False, read_only=True)
    class Meta:
        model = Area
        fields = '__all__'


class H_ValorFactorSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:valorFactor-detalle")
    #categoria = serializers.HyperlinkedRelatedField(view_name="visor:factorDesagregacion-detalle",read_only=True)
    categoria = serializers.PrimaryKeyRelatedField(read_only=True)
    categoria_nombre = serializers.SerializerMethodField('get_nombre_from_categoria')
    
    class Meta:
        model = ValorFactor
        fields = ['pk','url','valor','codigo','categoria','categoria_nombre',]

    def get_nombre_from_categoria(self, valor):
        categoria_nombre = valor.categoria.nombre
        return f'{categoria_nombre}'


class H_UnidadMedidaSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:unidadMedida-detalle")
    class Meta:
        model = UnidadMedida
        fields = '__all__'


class H_VariableSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:variable-detalle")
    unidad = H_UnidadMedidaSerializer(many=False, read_only=True)
    class Meta:
        model = Variable
        fields = '__all__'


class H_IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:indicador-detalle")
    instituciones = H_InstitucionSerializer(many=True, read_only=True)
    resultado = H_ResultadoSerializer(many=False, read_only=True)
    fuentes_informacion = H_FuenteInformacionSerializer(many=True, read_only=True)
    variable = H_VariableSerializer(many=False, read_only=True)
    factores_desagregacion = H_FactorDesagregacionSerializer(many=True, read_only=True)
    archivo = serializers.SerializerMethodField('get_archivo')
    alcance = serializers.SerializerMethodField('get_alcance')
    periodicidad = serializers.SerializerMethodField('get_periodicidad')
    class Meta:
        model = Indicador
        fields = '__all__'

    def get_archivo(self,indicador):
        if indicador.archivo:
            archivo = reverse_lazy("visor:archivo",kwargs={"indicador":indicador.id,}) 
        else:
            archivo = ""
        return archivo
    
    def get_periodicidad(self,indicador):
        return indicador.get_periodicidad_display()

    def get_alcance(self,indicador):
        return indicador.get_alcance_display()


class H_MedicionSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:medicion-detalle")
    indicador = serializers.HyperlinkedRelatedField(view_name="visor:indicador-detalle",read_only=True)
    valores_factor = H_ValorFactorSerializer(many=True, read_only=True)
    area = H_AreaSerializer(many=False, read_only=True)
    institucion = serializers.HyperlinkedRelatedField(view_name="visor:institucion-detalle",read_only=True)
    fecha = serializers.SerializerMethodField('get_ano')

    class Meta:
        model = MedicionIndicador
        fields = [
            "pk",
            "url",
            "codigo",
            "contenido",
            'valor_medicion',
            'valor_etario_inicial',
            'valor_etario_final',
            'fecha',
            "indicador",
            "valores_factor",
            "area",
            "institucion",
        ]

    def get_ano(self,medicion):
        ano = medicion.fecha.year if medicion.fecha is not None else "" 
        return f'{ano}'


#-----------------------------------Grafica-------------------------------------#
class ValorFactorSerializers(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(read_only=True,slug_field='nombre')
    class Meta:
        model = ValorFactor
        fields = ['valor','categoria',]


class GraficaSerializer(serializers.ModelSerializer):
    indicador = serializers.PrimaryKeyRelatedField(read_only=True)
    valores_factor = ValorFactorSerializers(many=True, read_only=True)#serializers.SerializerMethodField('get_valores')
    area = serializers.SlugRelatedField(slug_field='nombre',read_only=True)
    institucion = serializers.SlugRelatedField(slug_field='codigo',read_only=True)
    class Meta:
        model = MedicionIndicador
        fields = ['indicador','contenido','valor_medicion','institucion','area','valores_factor', 'fecha','ano']
    

class FactorDesagregacionSerializer(serializers.ModelSerializer):
    valores = serializers.SlugRelatedField(slug_field='valor', many=True,read_only=True)
    class Meta:
        model = FactorDesagregacion
        fields = ['nombre','valores']


class IndicadorGrafico(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    factores_desagregacion = FactorDesagregacionSerializer(many=True, read_only=True)
    #serializers.SlugRelatedField(slug_field='nombre', many=True, read_only=True)
    class Meta:
        model = Indicador
        fields = ['pk','nombre','factores_desagregacion']