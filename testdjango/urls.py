"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from drinknight import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/(?P<account>[A-Za-z0-9]+)/(?P<password>[^\s]+)/$',views.login),
    url(r'^register/(?P<account>[A-Za-z0-9]+)/$',views.register),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/profile/$',views.handle_user_data),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/drinkdatas/$',views.handle_drink_data),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/drinkdatas/(?P<year>[0-9]+)/$',views.get_year_data),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/drinkdatas/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.get_month_data),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/drinkdatas/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',views.get_day_data),
    url(r'^user/(?P<account>[A-Za-z0-9]+)/rankdatas/$',views.rank_day_data),
]
