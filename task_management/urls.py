from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Administration Django
    path('admin/', admin.site.urls),
    
    # URLs des applications
    path('api/tasks/', include('tasks.urls')),
    path('api/users/', include('users.urls')),
    
    # Documentation API (optionnel)
    path('api-docs/', include('rest_framework.urls', namespace='rest_framework')),
]

# Servir les fichiers media et static en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)