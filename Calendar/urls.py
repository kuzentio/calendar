from Calendar.calendar import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.main),
    url(r'^events/', views.events, name='events'),
    url(r'^add_event/', views.add_event, name='add_event'),

    url(r'^admin/', include(admin.site.urls)),
)
