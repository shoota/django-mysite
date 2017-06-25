from django.shortcuts import render, get_object_or_404
from .models import ClubTeam

# Create your views here.

def club_teams(request):
	clubs = ClubTeam.objects.all().order_by('created_date')
	return render(request, 'club_team/club_team_list.html', {'clubs':clubs})

def club_detail(request, pk):
	club = get_object_or_404(ClubTeam, pk=pk)
	return render(request, 'club_team/club_detail.html', {'club':club})