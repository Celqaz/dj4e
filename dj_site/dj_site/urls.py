"""dj_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('home/', include('home.urls')),
    path('hello/', include('hello.urls')),
    path('session/', include('session.urls')),
    path('getpost/', include('getpost.urls')),
    path('polls/', include('polls.urls')),
    path('route/', include('route.urls', namespace='nsroute')),
    path('gview/', include('gview.urls')),
    path('admin/', admin.site.urls),
    # 验证，默认搜索app registration目录下的login.html
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls',namespace='cats')),
]