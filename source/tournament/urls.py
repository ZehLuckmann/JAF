from django.urls import path

from . import views

app_name = 'tournament'

urlpatterns = [
    path('', views.tournament_index, name='index'), 
    path('add/', views.tournament_add, name='add'),
    path('edit/<int:tournament_id>/', views.tournament_edit, name='edit'),
    path('delete/<int:tournament_id>/', views.tournament_delete, name='delete'),

    path('game/', views.game_index, name='game_index'), 
    path('game/add/', views.game_add, name='game_add'),
    path('game/edit/<int:game_id>/', views.game_edit, name='game_edit'),
    path('game/delete/<int:game_id>/', views.game_delete, name='game_delete'),
]
