from django.urls import path
from . import views


urlpatterns =[
    path('',views.index,name='index'),
    path('tasks/<int:task_id>/', views.view_task, name='view_task'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('',views.task_list,name='task_list'),
    path('create/',views.task_create,name='task_create'),
    path('edit/<int:id>/',views.task_edit,name='task_edit'),
    path('delete/<int:id>/',views.task_delete,name='task_delete'),
    path('complete/<int:id>/',views.task_complete, name='task_complete'),
]

