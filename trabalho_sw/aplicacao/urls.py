from django.urls import path
from django.urls import path
from aplicacao import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import consultar

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sw_view, name='sw'),
    path('consultar/<str:tabela>/<str:entrada>/', consultar, name='consultar'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)