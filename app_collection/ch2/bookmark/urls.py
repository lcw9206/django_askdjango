"""ch1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # Class-based views
    url(r'^$', BookmarkLV.as_view(), name='index'),     # url 메서드에 name이 붙게되면 bookmark/index와 같이 url 뒤에 name이 추가된다.
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]