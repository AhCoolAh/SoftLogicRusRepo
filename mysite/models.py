from django.db import models

class PointGeo(models.Model):
    lat_coord = models.DecimalField(max_digits=9, decimal_places=6)
    lon_coord = models.DecimalField(max_digits=9, decimal_places=6)  
    geometry_type = models.CharField(max_length=5, default='')
    feature_type = models.CharField(max_length=7, default='')
    baloon_content = models.CharField(max_length=10, default='')