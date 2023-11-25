from django.urls import path
from django.urls import path
from supervisorio import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sw_view, name='sw')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)