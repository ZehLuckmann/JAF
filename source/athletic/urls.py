from django.urls import path

from . import views

app_name = 'athletic'

urlpatterns = [
    path('', views.athletic_index, name='index'), 
    path('add/', views.athletic_add, name='add'),
    path('edit/<int:athletic_id>/', views.athletic_edit, name='edit'),
    path('delete/<int:athletic_id>/', views.athletic_delete, name='delete'),
    path('users/<int:athletic_id>/', views.athletic_users, name='users'),
    
    path('users/approve/<int:user_id>/', views.athletic_approve, name='approve'),
    path('users/disapprove/<int:user_id>/', views.athletic_disapprove, name='disapprove'),
    path('users/promove/<int:user_id>/', views.athletic_promove, name='promove'),
]
