from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from django.views.generic import View
from django.http.response import FileResponse
from django.db.models import Q

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
        #'grafica': reverse('visor:grafica',request=request,format=format),

    })

#Vistas de Django Rest Framework
#Lista de Indicadores relacionados
class IndicadorRelacionadosList(generics.ListAPIView):
    serializer_class = IndicadorRelacionado
    def get_queryset(self):
        indicador_id = self.kwargs['indicador']
        indicador = Indicador.objects.get(id=indicador_id)
        if indicador.indicador_general:
            queryset = Indicador.objects.filter(Q(id=indicador_id)|Q(indicador_general=indicador_id)|Q(indicador_general=indicador.indicador_general.id)|Q(id=indicador.indicador_general.id))
        else :
            queryset = Indicador.objects.filter(Q(id=indicador_id)|Q(indicador_general=indicador_id))
        return queryset
    
#Descarga de Reportes Anuales
class ReporteAnualListView(generics.ListAPIView):
    serializer_class = ReporteAnualSerializer
    queryset = ReporteAnual.objects.all()

class ReporteAnualDownloadView(View):
    def get(self, request, *args, **kwargs):
        documento = ReporteAnual.objects.get(id=self.kwargs['reporte'])
        # create the HttpResponse object ...
        response = FileResponse(open(documento.archivo.path, 'rb'))
        return response

#Devuelve conjunto de indicadores que usan area
class SelectMapa(generics.ListCreateAPIView):
    serializer_class = IndicadorDescarga
    def get_queryset(self):
        indicadores = Indicador.objects.filter(mostrar=True,usa_area=True,indicador_general__isnull=True)
        return indicadores

#Descargas
class IndicadorDescargaView(generics.ListCreateAPIView):
    serializer_class = IndicadorDescarga
    def get_queryset(self):
        indicadores = Indicador.objects.filter(mostrar=True,indicador_general__isnull=True)
        return indicadores


class DocumentoDescargaView(generics.RetrieveDestroyAPIView):
    serializer_class = IndicadorDocumentoSerializer
    queryset = Indicador.objects.filter(mostrar=True,indicador_general__isnull=True)


class DocumentoView(View):
    def get(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=self.kwargs['documento'])
        # create the HttpResponse object ...
        response = FileResponse(open(documento.documento.path, 'rb'))
        return response

#Grafica
class GraficaV(generics.ListCreateAPIView):
    serializer_class = GraficaSerializer
    def get_queryset(self):
        if 'indicador' in self.kwargs:
            indicador = self.kwargs['indicador']
        else:
            indicador = None
        return MedicionIndicador.objects.all().filter(indicador__id=indicador).order_by('indicador','fecha') if indicador else MedicionIndicador.objects.all().order_by('indicador','fecha')

#detalle de Resultados para uso en recomendaciones de Ficha
class ResultadoRecomendacion(generics.RetrieveDestroyAPIView):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer2

#Lista de indicadores para uso de cualquier barra de busqueda
class IndicadorSelect(generics.ListCreateAPIView):
    serializer_class = IndicadorSerie
    queryset = Indicador.objects.filter(mostrar=True,indicador_general__isnull=True)
    


class IndicadorG(generics.ListCreateAPIView):
    serializer_class = IndicadorGrafico
    def get_queryset(self):
        indicadores = Indicador.objects.filter(mostrar=True,indicador_general__isnull=True)
        indicadores = indicadores.annotate(
            num_desagregacion = Count('mediciones__valores_factor')
        ).filter(num_desagregacion__gt=0)
        return indicadores


class ArchivoIndicadorView(View):
    def get(self, request, *args, **kwargs):
        indicador = Indicador.objects.get(id=self.kwargs['indicador'])
        # create the HttpResponse object ...
        response = FileResponse(open(indicador.archivo.path, 'rb'))
        return response


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
    serializer_class = H_ValorFactorSerializer
    def get_queryset(self):
        if 'categoria' in self.kwargs:
            categoria = self.kwargs['categoria']
        else:
            categoria = None
        return ValorFactor.objects.all().filter(categoria=categoria) if categoria else ValorFactor.objects.all().filter()


class UnidadMedidaList(generics.ListCreateAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = H_UnidadMedidaSerializer


class VariableList(generics.ListCreateAPIView):
    queryset = Variable.objects.all()
    serializer_class = H_VariableSerializer


class IndicadorList(generics.ListCreateAPIView):
    #queryset = Indicador.objects.all()
    serializer_class = H_IndicadorSerializer
    def get_queryset(self):
        indicadores = Indicador.objects.filter(mostrar=True,indicador_general__isnull=True)
        #indicadores = indicadores.annotate(
        #    num_desagregacion = Count('mediciones__valores_factor')
        #).filter(num_desagregacion__gt=0)
        return indicadores


class MedicionIndicadorList(generics.ListCreateAPIView):
    serializer_class = H_MedicionSerializer
    def get_queryset(self):
        if 'indicador' in self.kwargs:
            indicador = self.kwargs['indicador']
        else:
            indicador = None
        return MedicionIndicador.objects.filter(indicador__id=indicador).order_by('indicador','fecha') if indicador else MedicionIndicador.objects.all().order_by('indicador','fecha')


#Detalles API
class EjeDetail(generics.RetrieveDestroyAPIView):
    queryset = Eje.objects.all()
    serializer_class = EjeSerializer2


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
