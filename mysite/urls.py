from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('points/', views.get_all_points, name="points"),
    path('points/generate/', views.generate_points),
    path('', views.home)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)