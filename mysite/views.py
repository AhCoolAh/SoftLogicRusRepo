from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import random
from django.shortcuts import render

from .models import PointGeo

#  Метод для получения пар координат всех точек
#  из DB и их форматирования под API
@require_http_methods(['GET'])
def get_all_points(request):
    points_list = list(PointGeo.objects.all())
    serialized_points_list= {
        "type": "FeatureCollection",
        "features": [
            {
                "type": point.feature_type,
                "id": point.id,
                "geometry": {
                    "type": point.geometry_type,
                    "coordinates": [float(point.lat_coord), float(point.lon_coord)],
                },
                "properties": {
                    "balloonContent": point.baloon_content,
                } 
            } for point in points_list
        ],
    }
    return JsonResponse({
        "code": 200,
        "data": serialized_points_list
    })

# Метод для генерации случайных пар координат
# в прямоугольном полигоне Москвы и записи их в DB
@require_http_methods(['HEAD'])
def generate_points(request):
    print('Check')
    for i in range(100000):
        latitude = "%.6f" % random.uniform(55.59, 55.94)
        longitude = "%.6f" % random.uniform(37.40, 37.85)
        point = PointGeo(lat_coord=latitude, lon_coord=longitude, geometry_type="Point", feature_type="Feature", baloon_content='Балун')
        point.save()
    return HttpResponse('Success', content_type="text/plain")

# Рендеринг страницы
def home(request):
    return render(request, 'home.html')