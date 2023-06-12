"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Donation API",
        default_version='1.0.0',
        description="API documentation of App"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',
            include([
                path('api_auth/', include('api_auth.urls')),
                path('api_user/', include('api_user.urls')),
                path('api_project/', include('api_project.urls', "API_PROJECT")),
                path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
                path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
            ])
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]