from django.db import models
from .models import PointGeo

for i in range(100000):
        latitude = "%.6f" % random.uniform(55.59, 55.94)
        longitude = "%.6f" % random.uniform(37.40, 37.85)
        point = PointGeo(lat_coord=latitude, lon_coord=longitude, geometry_type="Point", feature_type="Feature", baloon_content='Балун')
        point.save()