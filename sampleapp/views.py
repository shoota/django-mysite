from django.shortcuts import render

# Create your views here.

def club_team_list(request):
	return render(request, 'club_team/club_team_list.html', {})