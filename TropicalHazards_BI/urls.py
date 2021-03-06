"""TropicalHazards_BI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
    path('rest-auth/', include('rest_auth.urls'), name='rest-auth'),
    path('refresh-token/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
    path('obtain-token/', obtain_jwt_token),
    path('projects/', include('projects.urls'), name='projects'),
    path('dashboards/', include('dashboards.urls'), name='dashboards'),
    path('tags/', include('tags.urls'), name='tags'),
    path('import/', include('import_data.urls'), name='importCsv'),
    path('metabase/', include('metabase.urls'), name='metabase')
]
