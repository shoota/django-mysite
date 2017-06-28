from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^clubs/', views.club_teams),
	url(r'^club/(?P<pk>[0-9]+)/$', views.club_detail, name='club_detail'),
	url(r'^club/new/$', views.club_new, name='club_new'),
	url(r'^club/(?P<pk>[0-9]+)/edit/$', views.club_edit, name='club_edit'),
]