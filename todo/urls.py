from django.urls import path, include
from . views import *

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<str:id>/', TaskDetailView.as_view(), name='task_detail'),
    
]