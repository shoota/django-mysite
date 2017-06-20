from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^clubs/', views.club_team_list),
]