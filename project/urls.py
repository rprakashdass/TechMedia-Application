from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolioPage.urls')),
    path('meta/',include('metaAPP.urls')),
    path('app_env/',include('app_env.urls')),
    path('app/',include('app.urls')),
]
