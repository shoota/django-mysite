from django.shortcuts import render
from .models import ClubTeam

# Create your views here.

def club_team_list(request):
	clubs = ClubTeam.objects.all().order_by('created_date')
	return render(request, 'club_team/club_team_list.html', {'clubs':clubs})