
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('ads/', include('ads.urls'))
    # path('autos/', include('autos.urls')),
    # path('cats/', include('cats.urls')),
]
