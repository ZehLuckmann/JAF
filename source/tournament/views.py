from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TournamentForm, GameForm
from .models import Tournament, Game

"""
Tournament
"""
def tournament_index(request):
    tournament = Tournament.objects.all()
    context = {'tournament': tournament}
    return render(request, 'tournament/index.html', context)


def tournament_add(request):  
    if request.method == "POST":  
        form = TournamentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tournament')  
            except:  
                pass  
    else:  
        form = TournamentForm() 

    return render(request,'tournament/add.html',{'form':form}) 

def tournament_edit(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    form = TournamentForm(initial={'name': tournament.name, 'start': tournament.start, 'end': tournament.end, 'modalities': tournament.modalities})
    if request.method == "POST":  
        form = TournamentForm(request.POST, instance=tournament)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tournament')  
            except Exception as e: 
                pass    
    return render(request,'tournament/edit.html',{'form':form}) 
    
def tournament_update(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    tournament.initials = request.POST.get('initials')
    tournament.name = request.POST.get('name')
    tournament.save()
    return HttpResponseRedirect('/tournament/')
    
def tournament_delete(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    tournament.delete()
    return HttpResponseRedirect('/tournament/')

"""
Game
"""
def game_index(request):
    game = Game.objects.all()
    context = {'game': game}
    return render(request, 'game/index.html', context)


def game_add(request):  
    if request.method == "POST":  
        form = GameForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tournament/game')  
            except:  
                pass  
    else:  
        form = GameForm() 

    return render(request,'game/add.html',{'form':form}) 

def game_edit(request, game_id):
    game = Game.objects.get(id=game_id)
    form = GameForm(initial={'tournament': game.tournament, 'modality': game.modality, 'team_1': game.team_1, 'team_2': game.team_2, 'date_time': game.date_time})
    if request.method == "POST":  
        form = GameForm(request.POST, instance=game)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tournament/game')  
            except Exception as e: 
                pass    
    return render(request,'game/edit.html',{'form':form}) 
    
def game_update(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.initials = request.POST.get('initials')
    game.name = request.POST.get('name')
    game.save()
    return HttpResponseRedirect('/tournament/game')
    
def game_delete(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    return HttpResponseRedirect('/tournament/game')