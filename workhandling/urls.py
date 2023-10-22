from django.urls import path
from . import views

app_name = 'workhandling'


urlpatterns = [
    path('task/<int:pk>',views.work,name='task'),
    path('task/edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
]