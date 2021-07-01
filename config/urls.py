"""config URL Configuration

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
from django.urls import path
from commlion import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('notice/', views.notice, name='notice'),
    path('notice/write/', views.noticeWrite, name='noticeWrite'),
    path('session/<int:session_num>/', views.session, name='session'),
    path('session/write/<int:session_num>', views.sessionWrite, name='sessionWrite'),
    path('qna/main/', views.qnaMain, name='qnaMain'),
    path('qna/detail/', views.qnaDetail, name='qnaDetail'),
    path('qna/write/', views.qnaWrite, name='qnaWrite'),
    path('project/main/', views.projectMain, name='projectMain'),
    path('project/detail/', views.projectDetail, name='projectDetail'),
    path('project/write/', views.projectWrite, name='projectWrite'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
