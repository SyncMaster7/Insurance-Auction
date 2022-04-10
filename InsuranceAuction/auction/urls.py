from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home_view),
    path('vehicles/', views.vehicles_view),
    path('motorcycles/', views.motorcycles_view),
    path('trailers/', views.trailers_view),
    path('parts/', views.parts_view),
    path('others/', views.other_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
