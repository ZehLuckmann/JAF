from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team_index, name='index'), 
    path('player/<int:team_id>/', views.player, name='player'),
    path('player_add/<int:team_id>/<int:user_id>', views.player_add, name='player_add'),
    path('player_delete/<int:team_id>/<int:user_id>', views.player_delete, name='player_delete'),
    
    path('add/', views.team_add, name='add'),
    path('edit/<int:team_id>/', views.team_edit, name='edit'),
    path('delete/<int:team_id>/', views.team_delete, name='delete'),
    
    path('modality/', views.modality_index, name='modality_index'), 
    path('modality/add/', views.modality_add, name='modality_add'),
    path('modality/edit/<int:modality_id>/', views.modality_edit, name='modality_edit'),
    path('modality/delete/<int:modality_id>/', views.modality_delete, name='modality_delete'),
]
