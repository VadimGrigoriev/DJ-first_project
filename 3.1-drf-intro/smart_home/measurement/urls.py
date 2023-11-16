from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('sensors/', views.SensorView.as_view()),
    path('sensors/<pk>/', views.SensorDetailView.as_view()),
    path('measurements/', views.MeasurementView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
