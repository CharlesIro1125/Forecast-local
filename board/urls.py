"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from forecast import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^boards/export/$', views.gridexp, name='gridexp'),
	url(r'^boards/import/$', views.gridimp, name='gridimp'),
	url(r'^boards/solar/$', views.solar, name='solar'),
	url(r'^boards/forecast/$', views.predict, name='predict'),
    path('admin/', admin.site.urls),
]
