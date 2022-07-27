from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TeamForm, ModalityForm
from .models import Modality, Team

from django.contrib.auth import get_user_model
User = get_user_model()

"""
Team
"""
def team_index(request):
    user = request.user
    team = Team.objects.filter(athletic=user.athletic).all()
    context = {'team': team}
    return render(request, 'team/index.html', context)

def team_add(request):  
    if request.method == "POST":  
        form = TeamForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/team/')  
            except:  
                pass  
    else:  
        form = TeamForm() 

    return render(request,'team/add.html',{'form':form}) 

def team_edit(request, team_id):
    team = Team.objects.get(id=team_id)
    form = TeamForm(initial={'athletic': team.athletic, 'modality': team.modality})
    if request.method == "POST":  
        form = TeamForm(request.POST, instance=team)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/team/')  
            except Exception as e: 
                pass    
    return render(request,'team/edit.html',{'form':form}) 
    
def team_update(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.initials = request.POST.get('initials')
    team.name = request.POST.get('name')
    team.save()
    return HttpResponseRedirect('/team/')
    
def team_delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    return HttpResponseRedirect('/team/')

"""
Team User
"""
def player(request, team_id):
    team = Team.objects.filter(id=team_id).first()
    users = User.objects.filter(athletic=team.athletic).all().exclude(id__in=team.players.all()).all()
    
    context = {'team': team, 'users' : users}
    return render(request, 'team/player_add.html', context)

def player_add(request, team_id, user_id):
    team = get_object_or_404(Team, pk=team_id)
    user = get_object_or_404(User, pk=user_id)
    
    team.players.add(user)
    team.save()
    return HttpResponseRedirect(f'/team/player/{team_id}')

def player_delete(request, team_id, user_id):
    team = get_object_or_404(Team, pk=team_id)
    user = get_object_or_404(User, pk=user_id)
    
    team.players.remove(user)
    team.save()
    return HttpResponseRedirect(f'/team/player/{team_id}')

"""
Modality
"""
def modality_index(request):
    modality = Modality.objects.all()
    context = {'modality': modality}
    return render(request, 'modality/index.html', context)
    
def modality_add(request):
    if request.method == "POST":  
        form = ModalityForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/team/modality')  
            except:  
                pass  
    else:  
        form = ModalityForm()
    
    return render(request,'modality/add.html',{'form':form})  
    
def modality_edit(request, modality_id):
    modality = Modality.objects.get(id=modality_id)
    form = ModalityForm(initial={'name': modality.name, 'genre': modality.genre})
    if request.method == "POST":  
        form = ModalityForm(request.POST, instance=modality)  
        if form.is_valid():  
            form.save() 
            model = form.instance
            return redirect('/team/modality')  
               
    return render(request,'modality/edit.html',{'form':form})

    
def modality_delete(request, modality_id):
    modality = get_object_or_404(Modality, pk=modality_id)
    modality.delete()
    return HttpResponseRedirect('/team/modality')