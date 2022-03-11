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

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from diary_main import views

app_name = 'diary_main'
# ROOT_URLConf
# 여기까지의 경로는 => http://127.0.0.1:8000/diary_main/
urlpatterns = [
    path('create/', views.b_create, name='b_create'),
    # http://127.0.0.1:8000/bbs/ 로 시작하면 include()를 이용해서
    # application 안의 URLConf로 이동
    # path('bbs/', include('bbs.urls')),  # 기본으로 잡힌 url에서 bbs/로 끝나서 앞부분 url과 맵핑이 되면 bbs.url로 넘겨준다
                  # 는 의미
    # path('users/', include('users.urls')), # users로 시작하면 users밑에있는 users.urls.py에서 처리하겠다는 의미
    path('list/', views.b_list, name='b_list'),
    path('<int:board_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:board_id>/update/', views.b_update, name='b_update'),
    path('like/', views.b_like, name='b_like'),
    path('delete/', views.b_delete, name='b_delete'),
    path('createComment/', views.create_comment, name='create_comment'),
    path('commentDelete/', views.comment_delete, name='comment_delete'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)