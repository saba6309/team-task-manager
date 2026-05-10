from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/', views.create_project, name='project'),
    path('task/', views.create_task, name='task'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update-status/<int:task_id>/<str:status>/', views.update_status, name='update_status'),
]