from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_control.urls')),
    path('app/', include('app_control.urls')),
    path('inventory_app_control/', include('inventory_app_control.urls'))
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
     