from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls), name='api_v1'),
]


class DocumentationView(SpectacularAPIView):
    api_version = '1.0.0'


urlpatterns += [
    path('schema/', DocumentationView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
