from django.shortcuts import render

from webOlap.models import *
from django.http import JsonResponse
from django.db import connection
import json

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def graficos(request):
    return render(request, 'graficos/graficos.html')

def grafico_ventas(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                YearBuilt,
                MonthSold,
                SUM(NumPropiedadesVendidas) AS TotalPropiedadesVendidas,
                AVG(VentaPromedio) AS PrecioPromedioVenta
            FROM HechosVentas
            INNER JOIN DimTiempo ON HechosVentas.TiempoId = DimTiempo.id
            GROUP BY YearBuilt, MonthSold
            ORDER BY YearBuilt, MonthSold;
        ''')
        data = cursor.fetchall()
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)
    return render(request, 'graficos/sales_chart.html', {'data': json_data})

def comparacion_ubicaciones(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SubwayStation,
                SUM(NumPropiedadesVendidas) AS TotalPropiedadesVendidas
            FROM HechosVentas
            INNER JOIN DimUbicacion ON HechosVentas.UbicacionId = DimUbicacion.id
            GROUP BY SubwayStation
            ORDER BY TotalPropiedadesVendidas DESC;
        ''')
        data = cursor.fetchall()
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)

    return render(request, 'graficos/location_comparison_chart.html', {'data': json_data})

def grafico_impacto_facilidades(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                N_FacilitiesNearBy_Total,
                AVG(VentaPromedio) AS PrecioPromedioVenta,
                SUM(NumPropiedadesVendidas) AS TotalPropiedadesVendidas
            FROM HechosVentas
            INNER JOIN DimFacilidades ON HechosVentas.FacilidadesId = DimFacilidades.id
            GROUP BY N_FacilitiesNearBy_Total;
        ''')
        data = cursor.fetchall()
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)

    return render(request, 'graficos/facilities_impact_chart.html', {'data': json_data})

def comparacion_tipos_escuelas(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                N_SchoolNearBy_Elementary,
                N_SchoolNearBy_Middle,
                N_SchoolNearBy_High,
                N_SchoolNearBy_University,
                SUM(NumPropiedadesVendidas) AS TotalPropiedadesVendidas
            FROM HechosVentas
            INNER JOIN DimFacilidades ON HechosVentas.FacilidadesId = DimFacilidades.id
            GROUP BY
                N_SchoolNearBy_Elementary,
                N_SchoolNearBy_Middle,
                N_SchoolNearBy_High,
                N_SchoolNearBy_University;
        ''')
        data = cursor.fetchall()
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)

    return render(request, 'graficos/school_type_comparison_chart.html', {'data': json_data})

def comparacion_tipos_facilidades(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                N_FacilitiesNearBy_PublicOffice,
                N_FacilitiesNearBy_Hospital,
                N_FacilitiesNearBy_Departmentstore,
                N_FacilitiesNearBy_Mall,
                N_FacilitiesNearBy_ETC,
                N_FacilitiesNearBy_Park,
                SUM(NumPropiedadesVendidas) AS TotalPropiedadesVendidas
            FROM HechosVentas
            INNER JOIN DimFacilidades ON HechosVentas.FacilidadesId = DimFacilidades.id
            GROUP BY
                N_FacilitiesNearBy_PublicOffice,
                N_FacilitiesNearBy_Hospital,
                N_FacilitiesNearBy_Departmentstore,
                N_FacilitiesNearBy_Mall,
                N_FacilitiesNearBy_ETC,
                N_FacilitiesNearBy_Park;
        ''')
        data = cursor.fetchall()

        # Convertir los datos a formato JSON
        json_data = json.dumps(data)


    return render(request, 'graficos/facility_type_comparison_chart.html', {'data': json_data})

def grafico_dispersion_tiempo_transporte(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                TimeToBusStop,
                AVG(VentaPromedio) AS PrecioPromedioVenta
            FROM HechosVentas
            INNER JOIN DimUbicacion ON HechosVentas.UbicacionId = DimUbicacion.id
            GROUP BY TimeToBusStop;
        ''')
        data = cursor.fetchall()
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)

    return render(request, 'graficos/time_to_transport_scatter_chart.html', {'data': json_data})

def grafico_comparacion(request):
    dimensions = ['DimUbicacion', 'DimTamaño', 'DimTiempo', 'DimFacilidades']  # Agrega los nombres de las tablas de dimensiones que correspondan

    with connection.cursor() as cursor:
        data = {}
        for dimension in dimensions:
            cursor.execute(f'''
                SELECT
                    *
                FROM {dimension};
            ''')
            dimension_data = cursor.fetchall()
            data[dimension] = dimension_data
        
        # Convertir los datos a formato JSON
        json_data = json.dumps(data)

    return render(request, 'graficos/comparison_chart.html', {'data': json_data, 'dimensions': dimensions})

