from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('purchases/', include('purchases.urls')),
]

# En la parte de la declaración de las rutas se utiliza el operador += para 
# agregar la lista de rutas de Django Debug Toolbar a la lista de rutas de la aplicación.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
