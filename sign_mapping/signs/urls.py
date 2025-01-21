from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignViewSet, upload_sign
from django.conf import settings
from django.conf.urls.static import static




router = DefaultRouter()
router.register(r'signs', SignViewSet)

urlpatterns = [
    path('', include('router.urls')),  
    path('upload/', upload_sign, name='upload_sign'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)