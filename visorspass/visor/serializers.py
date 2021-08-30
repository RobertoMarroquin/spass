from rest_framework import serializers

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


class FactorDesagregacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorDesagregacion
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
    #valores = H_ValorFactorSerializer(many=True, read_only=True)
    class Meta:
        model = FactorDesagregacion
        fields = '__all__'


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
    url = serializers.HyperlinkedIdentityField(view_name="visor:municipio-detalle")
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
    categoria = H_FactorDesagregacionSerializer(many=False, read_only=True)
    class Meta:
        model = ValorFactor
        fields = '__all__'


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

    class Meta:
        model = Indicador
        fields = '__all__'


class H_MedicionSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="visor:medicion-detalle")
    indicador = H_IndicadorSerializer(many=False, read_only=True)
    valores_factor = H_ValorFactorSerializer(many=True, read_only=True)
    area = H_AreaSerializer(many=False, read_only=True)
    class Meta:
        model = Variable
        fields = '__all__'
