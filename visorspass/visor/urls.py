from django.urls import path, include
from django.urls.conf import re_path
from .views import *

from rest_framework.routers import DefaultRouter

app_name = 'visor'
urlpatterns = [
    #Indicadores relacionados con subindicadores
    path('indicadores_relacionados/<int:indicador>', IndicadorRelacionadosList.as_view(), name='indicadores_relacionados'),
    #Descarga de Reporte anual
    path("reporte_anual/lista", ReporteAnualListView.as_view(), name="reportes"),
    path("reporte_anual/descarga/<int:reporte>", ReporteAnualDownloadView.as_view(), name="reporte"),
    #Select de mapa
    path("mapa/", SelectMapa.as_view(), name="selectMapa"),
    #Descarga Archivo Indicador
    path("archivo/indicador/<int:indicador>", ArchivoIndicadorView.as_view(), name="archivo"),
    #Descargas documentos
    path("descarga/", IndicadorDescargaView.as_view(), name="indicador-descarga"),
    path("descarga/<int:pk>", DocumentoDescargaView.as_view(), name="documento-descarga"),
    path("descarga/documento/<int:documento>", DocumentoView.as_view(), name="documento"),
    #API Root
    path("api/", api_root, name="api_root"),
    #Eje API
    path("eje/lista/", EjeList.as_view(), name="eje-lista"),
    path("eje/detalle/<int:pk>", EjeDetail.as_view(), name="eje-detalle"),
    #Resultado API
    path("resultado/lista/", ResultadoList.as_view(), name="resultado-lista"),
    path("resultado/detalle/<int:pk>", ResultadoDetail.as_view(), name="resultado-detalle"),
    #Institucion API
    path("institucion/lista/", InstitucionList.as_view(), name="institucion-lista"),
    path("institucion/detalle/<int:pk>", InstitucionDetail.as_view(), name="institucion-detalle"),
    #Departamento API
    path("departamento/lista/", DepartamentoList.as_view(), name="departamento-lista"),
    path("departamento/detalle/<int:pk>", DepartamentoDetail.as_view(), name="departamento-detalle"),
    #FactorDesagregacion API
    path("factorDesagregacion/lista/", FactorDesagregacionList.as_view(), name="factorDesagregacion-lista"),
    path("factorDesagregacion/detalle/<int:pk>", FactorDesagregacionDetail.as_view(), name="factorDesagregacion-detalle"),
    #FuenteInformacion API
    path("fuenteInformacion/lista/", FuenteInformacionList.as_view(), name="fuenteInformacion-lista"),
    path("fuenteInformacion/detalle/<int:pk>", FuenteInformacionDetail.as_view(), name="fuenteInformacion-detalle"),
    #Municipio API
    path("municipio/lista/", MunicipioList.as_view(), name="municipio-lista"),
    path("municipio/detalle/<int:pk>", MunicipioDetail.as_view(), name="municipio-detalle"),
    #Area API
    path("area/lista/", AreaList.as_view(), name="area-lista"),
    path("area/detalle/<int:pk>", AreaDetail.as_view(), name="area-detalle"),
    #ValorFactor API
    path("valorFactor/lista/", ValorFactorList.as_view(), name="valorFactor-lista"),
    path("valorFactor/lista/<int:categoria>", ValorFactorList.as_view(), name="valorFactor-lista-filtrada"),
    path("valorFactor/detalle/<int:pk>", ValorFactorDetail.as_view(), name="valorFactor-detalle"),
    #UnidadMedida API
    path("unidadMedida/lista/", UnidadMedidaList.as_view(), name="unidadMedida-lista"),
    path("unidadMedida/detalle/<int:pk>", UnidadMedidaDetail.as_view(), name="unidadMedida-detalle"),
    #Variable API
    path("variable/lista/", VariableList.as_view(), name="variable-lista"),
    path("variable/detalle/<int:pk>", VariableDetail.as_view(), name="variable-detalle"),
    #Indicador API
    path("indicador/lista/", IndicadorList.as_view(), name="indicador-lista"),
    path("indicador/detalle/<int:pk>", IndicadorDetail.as_view(), name="indicador-detalle"),
    #MedicionIndicador API
    path("medicion/lista/", MedicionIndicadorList.as_view(), name="medicion-lista"),
    path("medicion/lista/<int:indicador>/", MedicionIndicadorList.as_view(), name="medicion-lista-indicador"),
    path("medicion/detalle/<int:pk>", MedicionIndicadorDetail.as_view(), name="medicion-detalle"),
    #Grafica API
    path("grafica/<int:indicador>", GraficaV.as_view(), name="grafica"),
    #Indicador Grafica
    path("grafica/", IndicadorG.as_view(), name="indicador-grafica"),
    #Indicador Select
    path("indicadores/select", IndicadorSelect.as_view(), name="indicador-select"),
    #Resultado Recomendacion
    path("resultado/recomendacion/<int:pk>", ResultadoRecomendacion.as_view(), name="resultado-recomendacion"),
    
]
