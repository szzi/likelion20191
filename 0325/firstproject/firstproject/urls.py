"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#현재 장고프로그램의 url 저장하는 용돈
from django.contrib import admin
from django.urls import path
import wordcounter.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcounter.views.home, name="home"),
    path('about/',wordcounter.views.about, name="about"),
    path('count/',wordcounter.views.count, name="count"),
    path('select/',wordcounter.views.select, name="select"), 
    #(번호)는 각 인자를 의미.
    #(3)select라는 이름으로 html 파일에서 정보가 왔을 때, (1) url은 127.0.0.1/select로 보내고
    #(2)views.py에 있는 select 함수를 실행시킨다.
]
