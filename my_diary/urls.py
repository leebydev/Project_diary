"""lecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from diary_main import views

app_name = 'my_diary'
# ROOT_URLConf
# 여기까지의 경로는 => http://127.0.0.1:8000/
urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='home'),  # main page
    path('admin/', admin.site.urls),    # Admin page
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('howtouse/', TemplateView.as_view(template_name='howtouse.html'), name='howtouse'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('diary_main/', include('diary_main.urls')),
    # http://127.0.0.1:8000/bbs/ 로 시작하면 include()를 이용해서
    # application 안의 URLConf로 이동
    # path('bbs/', include('bbs.urls')),  # 기본으로 잡힌 url에서 bbs/로 끝나서 앞부분 url과 맵핑이 되면 bbs.url로 넘겨준다는 의미
    path('users/', include('users.urls')), # users로 시작하면 users밑에있는 users.urls.py에서 처리하겠다는 의미
]+ static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)