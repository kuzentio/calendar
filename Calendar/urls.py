from Calendar.calendar import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.main),
    url(r'^admin/', include(admin.site.urls)),
)
