from django.urls import path, include
from . views import *

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('tasks/<str:id>/', TaskDetailView.as_view(), name='task_detail'),
    path('categories/<str:id>/', CategoryDetailView.as_view(), name='category_detail'),
    
]