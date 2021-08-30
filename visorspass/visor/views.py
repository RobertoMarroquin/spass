from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import *
from .serializers import *

# Create your views here.
#API root
@api_view(['GET'])
def api_root(request, format=None, **kwargs):
    return Response({
        'ejes': reverse('visor:eje-lista',request=request,format=format),
        'resultados': reverse('visor:resultado-lista',request=request,format=format),
        'instituciones': reverse('visor:institucion-lista',request=request,format=format),
        'fuentesInformacion': reverse('visor:fuenteInformacion-lista',request=request,format=format),
        'factoresDesagregacion': reverse('visor:factorDesagregacion-lista',request=request,format=format),
        'departamento': reverse('visor:departamento-lista',request=request,format=format),
        'municipio': reverse('visor:municipio-lista',request=request,format=format),
        'area': reverse('visor:area-lista',request=request,format=format),
        'valorFactor': reverse('visor:valorFactor-lista',request=request,format=format),
        'unidadMedida': reverse('visor:unidadMedida-lista',request=request,format=format),
        'variable': reverse('visor:variable-lista',request=request,format=format),
        'indicador': reverse('visor:indicador-lista',request=request,format=format),
        'medicion': reverse('visor:medicion-lista',request=request,format=format),

    })


#Listas API
class EjeList(generics.ListCreateAPIView):
    queryset = Eje.objects.all()
    serializer_class = H_EjeSerializer


class InstitucionList(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = H_InstitucionSerializer


class FuenteInformacionList(generics.ListCreateAPIView):
    queryset = FuenteInformacion.objects.all()
    serializer_class = H_FuenteInformacionSerializer


class DepartamentoList(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = H_DepartamentoSerializer


class FactorDesagregacionList(generics.ListCreateAPIView):
    queryset = FactorDesagregacion.objects.all()
    serializer_class = H_FactorDesagregacionSerializer


class ResultadoList(generics.ListCreateAPIView):
    queryset = Resultado.objects.all()
    serializer_class = H_ResultadoSerializer


class MunicipioList(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = H_MunicipioSerializer


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = H_AreaSerializer


class ValorFactorList(generics.ListCreateAPIView):
    queryset = ValorFactor.objects.all()
    serializer_class = H_ValorFactorSerializer


class UnidadMedidaList(generics.ListCreateAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = H_UnidadMedidaSerializer


class VariableList(generics.ListCreateAPIView):
    queryset = Variable.objects.all()
    serializer_class = H_VariableSerializer


class IndicadorList(generics.ListCreateAPIView):
    queryset = Indicador.objects.all()
    serializer_class = H_IndicadorSerializer

class MedicionIndicadorList(generics.ListCreateAPIView):
    queryset = MedicionIndicador.objects.all()
    serializer_class = H_MedicionSerializer


#Detalles API
class EjeDetail(generics.RetrieveDestroyAPIView):
    queryset = Eje.objects.all()
    serializer_class = H_EjeSerializer


class InstitucionDetail(generics.RetrieveDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = H_InstitucionSerializer


class FuenteInformacionDetail(generics.RetrieveDestroyAPIView):
    queryset = FuenteInformacion.objects.all()
    serializer_class = H_FuenteInformacionSerializer


class DepartamentoDetail(generics.RetrieveDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = H_DepartamentoSerializer


class FactorDesagregacionDetail(generics.RetrieveDestroyAPIView):
    queryset = FactorDesagregacion.objects.all()
    serializer_class = H_FactorDesagregacionSerializer


class ResultadoDetail(generics.RetrieveDestroyAPIView):
    queryset = Resultado.objects.all()
    serializer_class = H_ResultadoSerializer


class MunicipioDetail(generics.RetrieveDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = H_MunicipioSerializer


class AreaDetail(generics.RetrieveDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = H_AreaSerializer    


class ValorFactorDetail(generics.RetrieveDestroyAPIView):
    queryset = ValorFactor.objects.all()
    serializer_class = H_ValorFactorSerializer


class UnidadMedidaDetail(generics.RetrieveDestroyAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = H_UnidadMedidaSerializer


class VariableDetail(generics.RetrieveDestroyAPIView):
    queryset = Variable.objects.all()
    serializer_class = H_VariableSerializer


class IndicadorDetail(generics.RetrieveDestroyAPIView):
    queryset = Indicador.objects.all()
    serializer_class = H_IndicadorSerializer

class MedicionIndicadorDetail(generics.RetrieveDestroyAPIView):
    queryset = MedicionIndicador.objects.all()
    serializer_class = H_MedicionSerializer    


#ViewSets CRUDS Completos
class EjeViewSet(viewsets.ModelViewSet):
    queryset = Eje.objects.all()
    serializer_class = EjeSerializer


class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class FuenteInformacionViewSet(viewsets.ModelViewSet):
    queryset = FuenteInformacion.objects.all()
    serializer_class = FuenteInformacionSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class FactorDesagregacionViewSet(viewsets.ModelViewSet):
    queryset = FactorDesagregacion.objects.all()
    serializer_class = FactorDesagregacionSerializer


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer


#Pruebas de serializacion django puro
def indicadores_list(request):
    MAX_OBJECTS = 100
    indicadores = Indicador.objects.all()
    data = {'results':list(indicadores.values())}
    return JsonResponse(data)


def indicador_detail(request, pk):
    indicador = get_object_or_404(Indicador, pk=pk)
    data = {"results": {
        "nombre": indicador.nombre,
        "codigo": indicador.codigo,
        "periodicidad": indicador.get_periodicidad_display()
    }}
    return JsonResponse(data)

