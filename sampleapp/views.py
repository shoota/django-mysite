from django.shortcuts import render, get_object_or_404, redirect
from .models import ClubTeam
from .forms import ClubTeamForm

# Create your views here.

def club_teams(request):
	clubs = ClubTeam.objects.all().order_by('created_date')
	return render(request, 'club_team/club_team_list.html', {'clubs':clubs})

def club_detail(request, pk):
	club = get_object_or_404(ClubTeam, pk=pk)
	return render(request, 'club_team/club_detail.html', {'club':club})

def club_new(request):
	if request.method == "POST":
		form = ClubTeamForm(request.POST)
		if form.is_valid():
			club = form.save(commit=False)
			club.author = request.user
			club.save()
			return redirect('club_detail', pk=club.pk)
	else:
		form = ClubTeamForm()
	return render(request, 'club_team/club_edit.html', {'form': form})

def club_edit(request, pk):
	club = get_object_or_404(ClubTeam, pk=pk)
	if request.method == "POST":
		form = ClubTeamForm(request.POST, instance=club)
		if form.is_valid():
			club = form.save(commit=False)
			club.author = request.user
			club.save()
			return redirect('club_detail', pk=club.pk)
	else:
		form = ClubTeamForm(instance=club)
	return render(request, "club_team/club_edit.html", {'form':form})
